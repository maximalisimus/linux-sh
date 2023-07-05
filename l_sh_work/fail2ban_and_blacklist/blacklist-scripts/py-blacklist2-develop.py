#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The Fail2Ban blacklist in Python.

Artamonov Mikhail [https://github.com/maximalisimus]
maximalis171091@yandex.ru
# License: GPL3
"""

__author__ = 'Mikhail Artamonov'

try:
	from .version import version, progname
except ImportError:
	version = "1.0.0"
	progname = 'py-blacklist.py'

__version__ = version

import argparse
import json
import pathlib
import sys
import ipaddress
import socket
import subprocess

workdir = str(pathlib.Path(sys.argv[0]).resolve().parent)
if workdir.endswith('/'):
		workdir = workdir[:-1]
blacklist_name = 'ip-blacklist.json'
whitelist_name = 'ip-whitelist.json'
json_black = pathlib.Path(f"{workdir}/{blacklist_name}").resolve()
json_white = pathlib.Path(f"{workdir}/{whitelist_name}").resolve()

class Arguments:
	''' Class «Arguments».
	
		Info: A class designed to store command-line values 
				by entering parameters through the «Argparse» module.
		
		Variables: All parameters are entered using the «createParser()» 
					method.
		
		Methods: 
			__getattr__(self, attrname):
				Access to a non-existent variable.
				Used when trying to get a parameter that does not exist. 
				In this case, «None» is returned to the user, instead 
				of an error.
			
			__str__(self):
				For STR Function output paramters.
			
			__repr__(self):
				For Debug Function output paramters.
	'''
	
	__slots__ = ['__dict__']
	
	def __getattr__(self, attrname):
		''' Access to a non-existent variable. '''
		return None

	def __str__(self):
		''' For STR Function output paramters. '''
		except_list = ['']
		return '\t' + '\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))

	def __repr__(self):
		''' For Debug Function output paramters. '''
		except_list = ['']
		return f"{self.__class__}:\n\t" + \
				'\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))

def createParser():
	''' The function of creating a parser with a certain hierarchy 
		of calls. Returns the parser itself and the sub-parser, 
		as well as groups of parsers, if any. '''
	global json_black
	global json_white
	global workdir
	parser = argparse.ArgumentParser(prog=progname,description='The Fail2Ban blacklist in Python.')
	parser.add_argument ('-v', '--version', action='version', version=f'{progname} {__version__}',  help='Version.')
	
	subparsers = parser.add_subparsers(title='Management', description='Management commands.', help='commands help.')
	
	parser_service = subparsers.add_parser('service', help='Program management.')
	parser_service.add_argument ('-start', '--start', action='store_true', default=False, help='Launching the blacklist.')
	parser_service.add_argument ('-stop', '--stop', action='store_true', default=False, help='Stopping the blacklist.')
	parser_service.add_argument ('-nostop', '--nostop', action='store_true', default=False, help='Stopping the blacklist without clearing IPTABLES.')
	parser_service.add_argument ('-reload', '--reload', action='store_true', default=False, help='Restarting the blacklist.')
	parser_service.set_defaults(onlist='service')	
	
	parser_blist = subparsers.add_parser('black', help='Managing blacklists.')
	parser_blist.add_argument ('-ban', '--ban', action='store_true', default=False, help='Block the entered ip addresses in IPTABLES.')
	parser_blist.add_argument ('-unban', '--unban', action='store_true', default=False, help='Unlock the entered ip addresses in IPTABLES.')
	parser_blist.add_argument ('-a', '--add', action='store_true', default=False, help='Add to the blacklist.')
	parser_blist.add_argument ('-d', '--delete', action='store_true', default=False, help='Remove from the blacklist.')
	parser_blist.add_argument ('-s', '--show', action='store_true', default=False, help='Read the blacklist.')
	parser_blist.add_argument ('-j', '--json', action='store_true', default=False, help='JSON fromat show.')
	parser_blist.add_argument ('-save', '--save', action='store_true', default=False, help='Save show info.')
	parser_blist.add_argument("-o", '--output', dest="output", metavar='OUTPUT', type=str, default=f"{json_black}", help='Output blacklist file.')
	parser_blist.set_defaults(onlist='black')	
	
	parser_wlist = subparsers.add_parser('white', help='Managing whitelists.')
	parser_wlist.add_argument ('-ban', '--ban', action='store_true', default=False, help='Allow entered ip addresses in IPTABLES.')
	parser_wlist.add_argument ('-unban', '--unban', action='store_true', default=False, help='Remove the permission of the entered ip addresses in IPTABLES.')
	parser_wlist.add_argument ('-a', '--add', action='store_true', default=False, help='Add to the whitelist.')
	parser_wlist.add_argument ('-d', '--delete', action='store_true', default=False, help='Remove from the whitelist.')
	parser_wlist.add_argument ('-s', '--show', action='store_true', default=False, help='Read the whitelist.')
	parser_wlist.add_argument ('-j', '--json', action='store_true', default=False, help='JSON fromat show.')
	parser_wlist.add_argument ('-save', '--save', action='store_true', default=False, help='Save show info.')
	parser_wlist.add_argument("-o", '--output', dest="output", metavar='OUTPUT', type=str, default=f"{json_white}", help='Output whitelist file.')
	parser_wlist.set_defaults(onlist='white')	
	
	group1 = parser.add_argument_group('Addressing', 'IP address management.')
	group1.add_argument("-c", '--count', dest="count", metavar='COUNT', type=int, default=0, help='The number of locks after which the address is entered in IPTABLES (default 0).')
	group1.add_argument("-q", '--quantity', dest="quantity", metavar='QUANTITY', type=int, default=0, help='How many times the address has been banned (default 0).')
	group1.add_argument("-ip", '--ip', metavar='IP', type=str, default=[''], nargs='+', help='IP address.')
	group1.add_argument("-m", '--mask', dest="mask", metavar='MASK', type=int, default=[], nargs='+', help='The network mask.')
	
	group2 = parser.add_argument_group('Files', 'Working with files.')
	group2.add_argument("-wd", '--workdir', dest="workdir", metavar='WORKDIR', type=str, default=f"{workdir}", help='Working directory.')
	group2.add_argument("-b", '--blacklist', dest="blacklist", metavar='BLACKLIST', type=str, default=f"{json_black}", help='Input blacklist file.')
	group2.add_argument("-w", '--whitelist', dest="whitelist", metavar='WHITELIST', type=str, default=f"{json_white}", help='Input whitelist file.')
	
	group3 = parser.add_argument_group('Settings', 'Configurations.')
	group3.add_argument ('-ipv6', '--ipv6', action='store_true', default=False, help='Select IP6TABLES.')
	group3.add_argument("-con", '--console', dest="console", metavar='CONSOLE', type=str, default='sh', help='Enther the console name (Default: "sh").')
	
	return parser, subparsers, parser_service, parser_blist, parser_wlist, group1, group2, group3

def read_write_json(jfile, typerw, data = dict()):
	''' The function of reading and writing JSON objects. '''
	with open(jfile, typerw) as fp:
		if typerw == 'r':
			data = json.load(fp)
			return data
		else:
			json.dump(data, fp, indent=2)

def read_write_text(onfile, typerw, data = ""):
	''' The function of reading and writing text files. '''
	with open(onfile, typerw) as fp:
		if typerw == 'r':
			data = fp.read()
		else:
			fp.write(data)
	return data

def ip_to_hostname(ip: str) -> str:
	''' Convert an ip address to a domain name. '''
	return socket.getfqdn(ip_no_mask(ip))

def ip_to_net(in_ip, in_mask = 32):	
	''' Convert an ip address to a network address with 
		a subnet via a backslash. '''
	net_ip = ip_no_mask(in_ip)
	out_ip = net_ip + '/' + mask_no_ip(in_ip, in_mask)
	my_host = ipaddress.ip_interface(out_ip)
	out_ip = f"{my_host.network}"
	return out_ip

def ip_no_mask(in_ip) -> str:
	''' Convert an ip address to an address without a network mask. '''
	return str(in_ip).split('/', 1)[0]

def mask_no_ip(in_ip, in_mask = 32) -> str:
	''' Get an ip address mask or assign a predefined value 
		or default value. '''
	if '/' in str(in_ip):
		net_mask = str(in_ip).split('/', 1)[1]
	else:
		net_mask = in_mask
	return str(net_mask)

def shell_run(shell: str, cmd: str) -> str:
	''' Execute the command in the specified command shell. 
		Returns the result of executing the command, if any.'''
	proc = subprocess.Popen(shell, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
	sys.stdout.flush()
	proc.stdin.write(cmd + "\n")
	proc.stdin.close()
	out_data = f"{proc.stdout.read()}"
	# Close the 'Popen' process correctly
	proc.terminate()
	proc.kill()
	return out_data

def switch_iptables(case = None, table = 'iptables', ip = None):
	''' Selecting a command to execute in the command shell. '''
	return {
			'add-white': f"sudo {table} -t filter -A INPUT -s {ip} -j ACCEPT",
			'del-white': f"sudo {table} -t filter -D INPUT -s {ip} -j ACCEPT",
			'add-black': f"sudo {table} -t filter -A INPUT -s {ip} -j DROP",
			'del-black': f"sudo {table} -t filter -D INPUT -s {ip} -j DROP",
			'read': 'sudo {table} -L'
	}.get(case, f"sudo {table} -L")

def switch_cmds(case = None):
	return {
			'black': {
					'True': 'add-black',
					'False': 'del-black'
					},
			'white': {
					'True': 'add-white',
					'False': 'del-white'
					},
	}.get(case, dict())

def switch_messages(case = None):
	return {
			'black': {
					'True': 'Ban',
					'False': 'Unban'
				},
			'white': {
					'True': 'Ignore',
					'False': 'Del ignore'
				},
	}.get(case, dict())

def read_list(args: Arguments):
	''' Read the input json files, if they are missing, 
		replace them with an empty dictionary. '''
	if args.blacklist.exists():
		args.blacklist_json = read_write_json(args.blacklist, 'r')
	else:
		args.blacklist_json = dict()
	if args.whitelist.exists():
		args.whitelist_json = read_write_json(args.whitelist, 'r')
	else:
		args.whitelist_json = dict()

def show_json(jobj: dict, counter: int = 0):
	''' Viewing a json object according to the specified criteria. '''
	if counter == 0:
		return tuple(f"{x}: {y}" for x, y in jobj.items())
	else:
		return tuple(f"{x}" for x,y in jobj.items() if y >= counter)

def ban_unban_one(args: Arguments):
	''' Ban or unban one ip address. '''
	# args.iptables_info
	# args.current_ip
	pass

def servicework(args: Arguments):
	''' Processing of service commands. '''
	
	def service_start_stop(args: Arguments):
		''' Launching or stopping the blacklist service. '''
		pass

	if args.start:
		pass
		sys.exit(0)
	if args.stop:
		pass
		sys.exit(0)
	if args.nostop:
		pass
		sys.exit(0)
	if args.reload:
		pass
		sys.exit(0)

def listwork(args: Arguments):
	''' Working with lists. '''
	
	def show_list(args: Arguments):
		''' Displaying information on the screen, 
			according to the specified criteria. '''
		data = ''
		if not args.json:
			data = '\n'.join(show_json(args.blacklist_json if args.onlist == 'black' else args.whitelist_json, args.count))
			print(data)
		else:
			data = json.dumps(args.blacklist_json if args.onlist == 'black' else args.whitelist_json, indent=2)
			print(data)
		if args.save:
			read_write_text(args.output, 'w', data + '\n')
	
	def ban_unban_full(args: Arguments):
		''' Ban or unban all entered ip addresses. '''
		pass
	
	def add_del_one(args: Arguments):
		''' Add or remove one ip address. '''
		pass
	
	def add_dell_full(args: Arguments):
		''' Adding or deleting all entered ip addresses. '''
		pass
	
	if args.ban:
		args.iptables_info = shell_run(args.console, switch_iptables('read', args.iptables))
		pass
		sys.exit(0)
	if args.unban:
		args.iptables_info = shell_run(args.console, switch_iptables('read', args.iptables))
		pass
		sys.exit(0)
	if args.add:
		read_list(args)
		pass
		sys.exit(0)
	if args.delete:
		read_list(args)
		pass
		sys.exit(0)
	if args.show:
		read_list(args)
		show_list(args)
		sys.exit(0)

def main():	
	''' The main cycle of the program. '''
	global workdir
	global json_black
	global json_white
	global blacklist_name
	global whitelist_name
	parser, sb1, psб, pbl, pwl, gr1, gr2, gr3 = createParser()
	args = Arguments()
	parser.parse_args(namespace=Arguments)
	
	if workdir != args.workdir:
		workdir = args.workdir
		json_black = pathlib.Path(f"{workdir}/{blacklist_name}").resolve()
		json_white = pathlib.Path(f"{workdir}/{whitelist_name}").resolve()
		if blacklist_name in args.blacklist:
			args.blacklist = json_black
		if whitelist_name in args.whitelist:
			args.whitelist = json_white
		if args.onlist == 'black':
			if blacklist_name in args.output:
				args.output = json_black
		elif args.onlist == 'white':
			if whitelist_name in args.output:
				args.output = json_white
	
	args.blacklist = pathlib.Path(f"{args.blacklist}").resolve()
	args.whitelist = pathlib.Path(f"{args.whitelist}").resolve()
	if str(args.output) != '':
		if args.output != None:
			args.output = pathlib.Path(f"{args.output}").resolve()
	
	if not args.ipv6:
		args.iptables = "iptables"
	else:
		args.iptables = 'ip6tables'
	
	func = {
			'service': servicework,
			'black': listwork,
			'white': listwork
			}
	
	if not pathlib.Path(str(workdir)).resolve().exists():
		pathlib.Path(str(workdir)).resolve().mkdir(parents=True)
	
	if args.onlist != None:
		func.get(args.onlist)(args)
	else:
		parser.parse_args(['-h'])
	
if __name__ == '__main__':
	main()
else:
	main()
