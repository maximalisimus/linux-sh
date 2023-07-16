#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The Fail2Ban black and white list in Python.

Artamonov Mikhail [https://github.com/maximalisimus]
maximalis171091@yandex.ru
# License: GPL3
"""

__author__ = 'Mikhail Artamonov'
__progname__ = 'py-blacklist.py'
__copyright__ = f"© The «{__progname__}». Copyright  by 2023."
__credits__ = ["Mikhail Artamonov"]
__license__ = "GPL3"
__version__ = "1.0.0"
__maintainer__ = "Mikhail Artamonov"
__email__ = "maximalis171091@yandex.ru"
__status__ = "Production"
__date__ = '09.07.2023'
__contact__ = 'VK: https://vk.com/shadow_imperator'

infromation = f"Author: {__author__}\nProgname: {__progname__}\nVersion: {__version__}\nDate: {__date__}\n" + \
			f"License: {__license__}\nCopyright: {__copyright__}\nCredits: {__credits__}\n" + \
			f"Maintainer: {__maintainer__}\nStatus: {__status__}\n" + \
			f"E-Mail: {__email__}\nContacts: {__contact__}"

import argparse
import json
import pathlib
import sys
import ipaddress
import socket
import subprocess
import re
from datetime import datetime

workdir = str(pathlib.Path(sys.argv[0]).resolve().parent)
if workdir.endswith('/'):
		workdir = workdir[:-1]
blacklist_name = 'ip-blacklist.json'
whitelist_name = 'ip-whitelist.json'
json_black = pathlib.Path(f"{workdir}").resolve().joinpath(blacklist_name)
json_white = pathlib.Path(f"{workdir}").resolve().joinpath(whitelist_name)

script_name = pathlib.Path(sys.argv[0]).resolve().name
script_full = f"{workdir}/{script_name}"
script_tmp = f"{workdir}/tmpfile"

log_name = 'blacklist_log.txt'
log_file = pathlib.Path(f"{workdir}").resolve().joinpath(log_name)

service_text = ''
st1 = '''[Unit]
Description=Blacklist service for banning and unbanning ip addresses of subnets.
Wants=fail2ban.service
After=fail2ban.service

[Service]
Type=oneshot
RemainAfterExit=yes'''
st2 = "\nExecStart=blacklist"
st3 = " -nft"
st4 = " -c %i service -start\n"
st5 = "ExecStop=blacklist"
st6 = " -c %i service -stop\n"
st7 = "ExecReload=blacklist"
st8 = " -c %i service -reload\n"
st9 = "[Install]\n"
st10 = "WantedBy=multi-user.target\n"

timer_text = '''[Unit]
Description=Blacklist timer for banning and unbanning ip addresses of subnets.
Wants=fail2ban.service
After=fail2ban.service

[Timer]
Unit=blacklist@%i.service
OnBootSec=20s
AccuracySec=1s

[Install]
WantedBy=timers.target'''

systemd_service_file = pathlib.Path('/etc/systemd/system/blacklist@.service').resolve()
systemd_timer_file = pathlib.Path('/etc/systemd/system/blacklist@.timer').resolve()

parser = ""

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
		#return '\t' + '\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))
		return '\t' + '\n\t'.join(f"{x}: {getattr(self, x)}" for x in dir(self) if not x in except_list and '__' not in x)
	
	def __repr__(self):
		''' For Debug Function output paramters. '''
		except_list = ['']
		return f"{self.__class__}:\n\t" + \
				'\n\t'.join(f"{x}: {getattr(self, x)}" for x in dir(self) if not x in except_list and '__' not in x)
				#'\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))

def createParser():
	''' The function of creating a parser with a certain hierarchy 
		of calls. Returns the parser itself and the sub-parser, 
		as well as groups of parsers, if any. '''
	global json_black, json_white, workdir, log_file
	
	parser = argparse.ArgumentParser(prog=__progname__,description='The Fail2Ban black and white list in Python.')
	parser.add_argument ('-v', '--version', action='version', version=f'{__progname__} {__version__}',  help='Version.')
	parser.add_argument ('-info', '--info', action='store_true', default=False, help='Information about the author.')
	
	subparsers = parser.add_subparsers(title='Management', description='Management commands.', help='commands help.')
	
	parser_systemd = subparsers.add_parser('systemd', help='Systemd management.')
	parser_systemd.add_argument ('-create', '--create', action='store_true', default=False, help='Create «blacklist@.service» and «blacklist@.timer».')
	parser_systemd.add_argument ('-delete', '--delete', action='store_true', default=False, help='Delete «blacklist@.service» and «blacklist@.timer».')
	parser_systemd.add_argument ('-status', '--status', action='store_true', default=False, help='Status «blacklist@.service».')
	parser_systemd.add_argument ('-enable', '--enable', action='store_true', default=False, help='Enable «blacklist@.timer».')
	parser_systemd.add_argument ('-disable', '--disable', action='store_true', default=False, help='Disable «blacklist@.timer».')
	parser_systemd.add_argument ('-start', '--start', action='store_true', default=False, help='Start «blacklist@.service».')
	parser_systemd.add_argument ('-stop', '--stop', action='store_true', default=False, help='Stop «blacklist@.service».')
	parser_systemd.add_argument ('-starttimer', '--starttimer', action='store_true', default=False, help='Start «blacklist@.timer».')
	parser_systemd.add_argument ('-stoptimer', '--stoptimer', action='store_true', default=False, help='Stop «blacklist@.timer».')
	parser_systemd.set_defaults(onlist='systemd')	
	
	parser_service = subparsers.add_parser('service', help='Program management.')
	parser_service.add_argument ('-start', '--start', action='store_true', default=False, help='Launching the blacklist.')
	parser_service.add_argument ('-stop', '--stop', action='store_true', default=False, help='Stopping the blacklist.')
	parser_service.add_argument ('-nostop', '--nostop', action='store_true', default=False, help='Stopping the blacklist without clearing {IP,IP6,NF}TABLES.')
	parser_service.add_argument ('-reload', '--reload', action='store_true', default=False, help='Restarting the blacklist.')
	parser_service.add_argument ('-show', '--show', action='store_true', default=False, help='Show the service blacklist and iptables.')
	parser_service.add_argument ('-link', '--link', action='store_true', default=False, help='Symlink to program on «/usr/bin/».')
	parser_service.add_argument ('-unlink', '--unlink', action='store_true', default=False, help='Unlink to program on «/usr/bin/».')
	parser_service.set_defaults(onlist='service')
	
	parser_blist = subparsers.add_parser('black', help='Managing blacklists.')
	parser_blist.add_argument ('-ban', '--ban', action='store_true', default=False, help='Block the entered ip addresses in {IP,IP6,NF}TABLES.')
	parser_blist.add_argument ('-unban', '--unban', action='store_true', default=False, help='Unlock the entered ip addresses in {IP,IP6,NF}TABLES.')
	parser_blist.add_argument ('-a', '--add', action='store_true', default=False, help='Add to the blacklist.')
	parser_blist.add_argument ('-d', '--delete', action='store_true', default=False, help='Remove from the blacklist.')
	parser_blist.add_argument ('-s', '--show', action='store_true', default=False, help='Read the blacklist.')
	parser_blist.add_argument ('-j', '--json', action='store_true', default=False, help='JSON fromat show.')
	parser_blist.add_argument ('-save', '--save', action='store_true', default=False, help='Save show info.')
	parser_blist.add_argument("-o", '--output', dest="output", metavar='OUTPUT', type=str, default=f"{json_black}", help='Output blacklist file.')
	parser_blist.set_defaults(onlist='black')
	
	pgroup1 = parser_blist.add_argument_group('Addressing', 'IP address management.')
	pgroup1.add_argument("-ip", '--ip', metavar='IP', type=str, default=[''], nargs='+', help='IP address.')
	pgroup1.add_argument("-m", '--mask', dest="mask", metavar='MASK', type=int, default=[], nargs='+', help='The network mask.')
	
	parser_wlist = subparsers.add_parser('white', help='Managing whitelists.')
	parser_wlist.add_argument ('-ban', '--ban', action='store_true', default=False, help='Allow entered ip addresses in {IP,IP6,NF}TABLES.')
	parser_wlist.add_argument ('-unban', '--unban', action='store_true', default=False, help='Remove the permission of the entered ip addresses in {IP,IP6,NF}TABLES.')
	parser_wlist.add_argument ('-a', '--add', action='store_true', default=False, help='Add to the whitelist.')
	parser_wlist.add_argument ('-d', '--delete', action='store_true', default=False, help='Remove from the whitelist.')
	parser_wlist.add_argument ('-s', '--show', action='store_true', default=False, help='Read the whitelist.')
	parser_wlist.add_argument ('-j', '--json', action='store_true', default=False, help='JSON fromat show.')
	parser_wlist.add_argument ('-save', '--save', action='store_true', default=False, help='Save show info.')
	parser_wlist.add_argument("-o", '--output', dest="output", metavar='OUTPUT', type=str, default=f"{json_white}", help='Output whitelist file.')
	parser_wlist.set_defaults(onlist='white')
	
	pgroup2 = parser_wlist.add_argument_group('Addressing', 'IP address management.')
	pgroup2.add_argument("-ip", '--ip', metavar='IP', type=str, default=[''], nargs='+', help='IP address.')
	pgroup2.add_argument("-m", '--mask', dest="mask", metavar='MASK', type=int, default=[], nargs='+', help='The network mask.')
	
	group1 = parser.add_argument_group('Parameters', 'Settings for the number of bans.')
	group1.add_argument("-c", '--count', dest="count", metavar='COUNT', type=int, default=0, help='The number of locks after which the ip-address is entered in {IP,IP6,NF}TABLES (default 0).')
	group1.add_argument("-q", '--quantity', dest="quantity", metavar='QUANTITY', type=int, default=0, help='The number of ip address locks to be saved (default 0).')
	
	group2 = parser.add_argument_group('Files', 'Working with files.')
	group2.add_argument("-wd", '--workdir', dest="workdir", metavar='WORKDIR', type=str, default=f"{workdir}", help='Working directory.')
	group2.add_argument("-b", '--blacklist', dest="blacklist", metavar='BLACKLIST', type=str, default=f"{json_black}", help='Input blacklist file.')
	group2.add_argument("-w", '--whitelist', dest="whitelist", metavar='WHITELIST', type=str, default=f"{json_white}", help='Input whitelist file.')
	
	group3 = parser.add_argument_group('{IP,IP6,NF}TABLES', 'Configuration {IP,IP6,NF}TABLES.')
	group3.add_argument ('-ipv6', '--ipv6', action='store_true', default=False, help='Select {IP6/NF}TABLES.')
	group3.add_argument ('-nft', '--nftables', action='store_true', default=False, help='Select the NFTABLES (IP,IP6) framework (Default {IP,IP6}TABLES).')
	group3.add_argument("-protocol", '--protocol', default='ip', choices=['ip', 'ip6', 'inet'], help='Select the protocol ip-addresses (Auto ipv4 on "ip" or -ipv6 to "ip6").')
	group3.add_argument("-nftproto", '--nftproto', default='ip', choices=['ip', 'ip6', 'inet'], help='Select the protocol NFTABLES, before rule (Auto ipv4 on "ip" or -ipv6 to "ip6").')
	group3.add_argument("-table", '--table', dest="table", metavar='TABLE', type=str, default='filter', help='Select the table for NFTABLES (Default "filter").')
	group3.add_argument("-chain", '--chain', dest="chain", metavar='CHAIN', type=str, default='INPUT', help='Choosing a chain of rules (Default: "INPUT").')
	group3.add_argument ('-newtable', '--newtable', action='store_true', default=False, help='Add a new table in NFTABLES. Use carefully!')
	group3.add_argument ('-newchain', '--newchain', action='store_true', default=False, help='Add a new chain in {IP,IP6,NF}TABLES. Use carefully!')
	group3.add_argument ('-Deltable', '--Deltable', action='store_true', default=False, help='Del the table in NFTABLES. Use carefully!')
	group3.add_argument ('-Delchain', '--Delchain', action='store_true', default=False, help='Del the chain in {IP,IP6,NF}TABLES. Use carefully!')
	group3.add_argument ('-cleartable', '--cleartable', action='store_true', default=False, help='Clear the table in NFTABLES. Use carefully!')
	group3.add_argument ('-clearchain', '--clearchain', action='store_true', default=False, help='Clear the chain in {IP,IP6,NF}TABLES. Use carefully!')
	group3.add_argument ('-personal', '--personal', action='store_true', default=False, help='Personal settings of {IP,IP6,NF}TABLES tables, regardless of the data entered.')
	group3.add_argument ('-fine', '--fine', action='store_true', default=False, help='Full clearing {IP,IP6,NF}TABLES tables from all settings. Use carefully!')
	group3.add_argument ('-e', '-exit', '--exit', action='store_true', default=False, help='Finish creating the table/chain.')
	
	group4 = parser.add_argument_group('Settings', 'Configurations.')
	group4.add_argument("-con", '--console', dest="console", metavar='CONSOLE', type=str, default='sh', help='Enther the console name (Default "sh").')
	group4.add_argument("-logfile", '--logfile', dest="logfile", metavar='LOGFILE', type=str, default=f"{log_file}", help='Log file.')
	group4.add_argument ('-nolog', '--nolog', action='store_false', default=True, help="Don't keep a log file.")
	group4.add_argument ('-limit', '--limit', action='store_true', default=False, help='Limit the log file. Every day the contents of the log will be completely erased.')
	group4.add_argument ('-viewlog', '--viewlog', action='store_true', default=False, help='View the log file.')
	group4.add_argument ('-resetlog', '--resetlog', action='store_true', default=False, help='Reset the log file.')
	
	return parser, subparsers, parser_service, parser_systemd, parser_blist, parser_wlist, pgroup1, pgroup2, group1, group2, group3, group4

def AppExit(args: Arguments):
	''' Shutting down the application. '''
	
	# switch_nftables(args, case)
	# 'del-table' 'del-chain' 'flush-table' 'flush-chain'
	#
	# switch_iptables(args, case)
	# 'del-input' 'flush-chain' 'del-chain'
	# args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
	# service_info, args.err = shell_run(args.console, switch_systemd('start-timer', args.count))
	# args.nftproto = 'ip' / 'ip6' args.table = 'filter'  args.chain = 'INPUT'
	# print('Close the blacklist ...')
	# print('Exit the blacklist ...')
	
	if args.nftables:
		if args.clearchain:
			if (args.table != 'filter') ^ (args.chain != 'INPUT'):
				pass
		if args.Delchain:
			if (args.table != 'filter') ^ (args.chain != 'INPUT'):
				pass
		if args.cleartable:
			if args.table != 'filter':
				pass
		if args.Deltable:
			if args.table != 'filter':
				pass
	else:
		if args.clearchain:
			if args.chain != 'INPUT':
				pass
		if args.Delchain:
			if args.chain != 'INPUT':
				pass
	if args.nolog:
		if args.log_txt:
			ondatetime = datetime.now().strftime("%a %d %b %Y %H:%M:%S %Z")
			read_write_text(args.logfile, 'a', f"\n{ondatetime}\n")
			read_write_text(args.logfile, 'a', '\n'.join(args.log_txt) + '\n')
	sys.exit(0)

def service_build(args: Arguments):
	global service_text, st1, st2, st3, st4, st5, st6, st7, st8, st9, st10
	
	if args.nftables:
		if args.personal:
			pass
		else:
			pass
	else:
		if args.personal:
			pass
		else:
			pass

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
	err_data = f"{proc.stderr.read()}"
	# Close the 'Popen' process correctly
	proc.terminate()
	proc.kill()
	return out_data, err_data

def switch_iptables(args: Arguments, case = None):
	''' Selecting a command to execute in the command shell. '''
	return {
			'add-white': f"sudo {args.protocol} -t {args.table} -A {args.chain} -s {args.current_ip} -j ACCEPT",
			'del-white': f"sudo {args.protocol} -t {args.table} -D {args.chain} -s {args.current_ip} -j ACCEPT",
			'add-black': f"sudo {args.protocol} -t {args.table} -A {args.chain} -s {args.current_ip} -j DROP",
			'del-black': f"sudo {args.protocol} -t {args.table} -D {args.chain} -s {args.current_ip} -j DROP",
			'read': f"sudo {args.protocol} -L {args.chain}",
			'create-chain': f"sudo {args.protocol} -N {args.chain}",
			'create-return': f"sudo {args.protocol} -A {args.chain} -j RETURN",
			'create-input': f"sudo {args.protocol} -I INPUT -j {args.chain}",
			'del-input': f"sudo {args.protocol} -D INPUT -j {args.chain}",
			'flush-chain': f"sudo {args.protocol} -F {args.chain}",
			'del-chain': f"sudo {args.protocol} -X {args.chain}"
	}.get(case, f"sudo {args.protocol} -L {args.chain}")

def switch_nftables(args: Arguments, case = None, handle = None):
	''' Selecting a command to execute NFTABLES in the command shell. '''
	return {
			'add-white': f"sudo nft 'add rule {args.nftproto} {args.table} {args.chain} {args.protocol} saddr {args.current_ip} counter accept'",
			'del-white': f"sudo nft delete rule {args.nftproto} {args.table} {args.chain} handle {handle}",
			'add-black': f"sudo nft 'add rule {args.nftproto} {args.table} {args.chain} {args.protocol} saddr {args.current_ip} counter drop'",
			'del-black': f"sudo nft delete rule {args.nftproto} {args.table} {args.chain} handle {handle}",
			'read': f"sudo nft list table {args.nftproto} {args.table}",
			'search': f"sudo nft --handle --numeric list chain {args.nftproto} {args.table} {args.chain} | grep -Ei 'ip saddr|# handle'" + \
			''' | sed 's/^[ \t]*//' | awk '!/^$/{print $0}' ''',
			'create-chain': f"nft add chain {args.nftproto} {args.table} {args.chain}" + ''' '{ type filter hook input priority 0; policy accept; }\'''',
			'create-table': f"nft add table {args.nftproto} {args.table}",
			'del-table': f"sudo nft delete table {args.nftproto} {args.table}",
			'del-chain': f"sudo nft delete chain {args.nftproto} {args.table} {args.chain}",
			'flush-table': f"sudo nft flush table {args.nftproto} {args.table}",
			'flush-chain': f"sudo nft flush chain {args.nftproto} {args.table} {args.chain}"
	}.get(case, f"sudo nft list table {args.nftproto} {args.table}")

def switch_cmds(case = None):
	''' Selecting a command for the «switch_iptables» method. '''
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
	''' Selecting a message to display on the screen. '''
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

def switch_systemd(case = None, counter = 3):
	''' Systemd control selection. '''
	return {
			'status': f"sudo systemctl status blacklist@{counter}.service",
			'start-service': f"sudo systemctl start blacklist@{counter}.service",
			'stop-service': f"sudo systemctl stop blacklist@{counter}.service",
			'enable': f"sudo systemctl enable blacklist@{counter}.timer",
			'disable': f"sudo systemctl disable blacklist@{counter}.timer",
			'start-timer': f"sudo systemctl start blacklist@{counter}.timer",
			'stop-timer': f"sudo systemctl stop blacklist@{counter}.timer"
	}.get(case, f"sudo systemctl status blacklist@{counter}.service")

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

def search_handle(text: str, in_ip):
	count = 0
	rez = -1
	nomask = ip_no_mask(in_ip)
	for elem in text.split('\n'):
		if nomask in elem:
			rez = count
		count += 1
	if rez != -1:
		return text.split('\n')[rez].split(' ')[-1]
	else:
		return None

def systemdwork(args: Arguments):
	''' Systemd management. '''
	global service_text, timer_text, systemd_service_file, systemd_timer_file, parser
	
	if args.count == 0:
		args.count = 3
	
	if args.delete:
		print('Delete systemd «blacklist@.service» and «blacklist@.timer» ...')
		shell_run(args.console, switch_systemd('stop-timer', args.count))
		shell_run(args.console, switch_systemd('stop-service', args.count))
		shell_run(args.console, switch_systemd('disable', args.count))
		systemd_service_file.unlink(missing_ok=True)
		systemd_timer_file.unlink(missing_ok=True)
		print('Exit the blacklist ...')
		if args.nolog:
			args.log_txt.append(f"Delete systemd «blacklist@.service» and «blacklist@.timer» ...")
			args.log_txt.append(f"Exit the blacklist ...")
		AppExit(args)
	if args.create:
		print('Create systemd «blacklist@.service» and «blacklist@.timer» ...')
		service_build(args)
		shell_run(args.console, switch_systemd('stop-timer', args.count))
		shell_run(args.console, switch_systemd('stop-service', args.count))
		shell_run(args.console, switch_systemd('disable', args.count))
		read_write_text(systemd_service_file, 'w', service_text)
		read_write_text(systemd_timer_file, 'w', timer_text)
		print('Exit the blacklist ...')
		if args.nolog:
			args.log_txt.append(f"Create systemd «blacklist@.service» and «blacklist@.timer» ...")
			args.log_txt.append(f"Exit the blacklist ...")
		AppExit(args)
	if systemd_service_file.exists() and systemd_timer_file.exists():
		if args.status:
			service_info, err = shell_run(args.console, switch_systemd('status', args.count))
			args.log_txt.append(f"----- Systemd Info -----\n{service_info}\n----- Systemd Info -----")
			args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			print(f"----- Systemd Info -----\n{service_info}\n----- Systemd Info -----")
			print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			sys.exit(0)
		if args.enable:
			print(f"Enable «blacklist@{args.count}.timer» ...")
			service_info, args.err = shell_run(args.console, switch_systemd('enable', args.count))
			print(service_info)
			print(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
			print('Exit the blacklist ...')
			if args.nolog:
				args.log_txt.append(f"Enable «blacklist@{args.count}.timer» ...")
				args.log_txt.append(service_info)
				args.log_txt.append(f"Exit the blacklist ...")
				args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
			AppExit(args)
		if args.disable:
			print(f"Disable «blacklist@{args.count}.timer» ...")
			service_info, err = shell_run(args.console, switch_systemd('disable', args.count))
			print(service_info)
			print('Exit the blacklist ...')
			print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			if args.nolog:
				args.log_txt.append(f"Disable «blacklist@{args.count}.timer» ...")
				args.log_txt.append(service_info)
				args.log_txt.append(f"Exit the blacklist ...")
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			AppExit(args)
		if args.start:
			print(f"Start «blacklist@{args.count}.service» ...")
			service_info, err = shell_run(args.console, switch_systemd('start-service', args.count))
			print(service_info)
			print('Exit the blacklist ...')
			print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			if args.nolog:
				args.log_txt.append(f"Start «blacklist@{args.count}.service» ...")
				args.log_txt.append(service_info)
				args.log_txt.append(f"Exit the blacklist ...")
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			AppExit(args)
		if args.stop:
			print(f"Stop «blacklist@{args.count}.service» ...")
			service_info, err = shell_run(args.console, switch_systemd('stop-service', args.count))
			print(service_info)
			print('Exit the blacklist ...')
			print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			if args.nolog:
				args.log_txt.append(f"Stop «blacklist@{args.count}.service» ...")
				args.log_txt.append(service_info)
				args.log_txt.append(f"Exit the blacklist ...")
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			AppExit(args)
		if args.starttimer:
			print(f"Start «blacklist@{args.count}.timer» ...")
			service_info, err = shell_run(args.console, switch_systemd('start-timer', args.count))
			print(service_info)
			print('Exit the blacklist ...')
			print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			if args.nolog:
				args.log_txt.append(f"Start «blacklist@{args.count}.timer» ...")
				args.log_txt.append(service_info)
				args.log_txt.append(f"Exit the blacklist ...")
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			AppExit(args)
		if args.stoptimer:
			print(f"Stop «blacklist@{args.count}.timer» ...")
			service_info, err = shell_run(args.console, switch_systemd('stop-timer', args.count))
			print(service_info)
			print('Exit the blacklist ...')
			print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			if args.nolog:
				args.log_txt.append(f"Stop «blacklist@{args.count}.timer» ...")
				args.log_txt.append(service_info)
				args.log_txt.append(f"Exit the blacklist ...")
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
			AppExit(args)
	else:
		print(f"\nSystemd file «{systemd_service_file.name}» and «{systemd_timer_file.name}» not found!")
		print(f"Please enter «-create» to create systemd files!\n")
	if not args.log_txt:
		parser.parse_args(['systemd', '-h'])
		sys.exit(0)

def servicework(args: Arguments):
	''' Processing of service commands. '''
	global script_full, script_name, script_tmp, parser
	
	def service_start_stop(args: Arguments):
		''' Launching or stopping the blacklist service. '''
		args.onlist = 'white'
		data_white = show_json(args.whitelist_json, 1)
		data_black = show_json(args.blacklist_json, args.count)
		for elem in range(len(data_white)):
			args.current_ip = f"{data_white[elem]}"
			if not args.nftables:
				ban_unban_one(args)
			else:
				nft_ban_unban_one(args)
		args.current_ip = None
		args.onlist = 'black'
		for elem in range(len(data_black)):
			args.current_ip = f"{data_black[elem]}"
			if not args.nftables:
				ban_unban_one(args)
			else:
				nft_ban_unban_one(args)
		args.current_ip = None
		args.onlist = None
		args.add = None
	
	read_list(args)
	args.add = args.start
	if args.count == 0:
		args.count = 3
	
	if args.link:
		print('Cryate the symlink to program on «/usr/bin/» ...')
		script_full = pathlib.Path(f"{script_full}").resolve()
		script_usr_bin = pathlib.Path('/usr/bin/blacklist').resolve()
		shell_run(args.console, f"sudo ln -s {script_full} {script_usr_bin}")
		shell_run(args.console, f"sudo chmod +x {script_usr_bin}")
		print('Exit the blacklist ...')
		if args.nolog:
			args.log_txt.append('Cryate the symlink to program on «/usr/bin/» ...')
			args.log_txt.append(f"Exit the blacklist ...")
		AppExit(args)
	if args.unlink:
		print('Delete the symlink to program on «/usr/bin/» ...')
		src1 = pathlib.Path(script_full).resolve()
		src2 = pathlib.Path(script_tmp).resolve()
		src1.rename(src2)
		shell_run(args.console, f"rm -rf /usr/bin/blacklist")
		src2.rename(src1)
		print('Exit the blacklist ...')
		if args.nolog:
			args.log_txt.append('Delete the symlink to program on «/usr/bin/» ...')
			args.log_txt.append(f"Exit the blacklist ...")
		AppExit(args)
	if args.show:
		if not args.nftables:
			args.iptables_info, args.err = shell_run(args.console, switch_iptables(args, 'read'))
			print(f"\n----- IPTABLES Info -----\n{args.iptables_info}\n----- IPTABLES Info -----")
			print(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
		else:
			args.iptables_info, args.err = shell_run(args.console, switch_nftables(args, 'read'))
			args.log_txt.append(f"\n----- NFTABLES Info -----\n{args.iptables_info}\n----- NFTABLES Info -----")
			args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
			print(f"\n----- NFTABLES Info -----\n{args.iptables_info}\n----- NFTABLES Info -----")
			print(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
		sys.exit(0)
	if args.start:
		print('Start the blacklist ...')
		if not args.nftables:
			args.iptables_info, args.err = shell_run(args.console, switch_iptables(args, 'read'))
		else:
			args.iptables_info, args.err = shell_run(args.console, switch_nftables(args, 'search'))
		if args.nolog:
			args.log_txt.append('Start the blacklist ...')
		service_start_stop(args)
		print('Exit the blacklist ...')
		print(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
		if args.nolog:
			args.log_txt.append(f"Exit the blacklist ...")
			args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
		AppExit(args)
	if args.stop:
		print('Stopping the blacklist ...')
		if not args.nftables:
			args.iptables_info, args.err = shell_run(args.console, switch_iptables(args, 'read'))
		else:
			args.iptables_info, args.err = shell_run(args.console, switch_nftables(args, 'search'))
		if args.nolog:
			args.log_txt.append('Stopping the blacklist ...')
		service_start_stop(args)
		print('Exit the blacklist ...')
		print(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
		if args.nolog:
			args.log_txt.append(f"Exit the blacklist ...")
			args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
		AppExit(args)
	if args.nostop:
		print('No stopped the blacklist.')
		print('Exit the blacklist ...')
		sys.exit(0)
	if args.reload:
		print('Reload the blacklist ...')
		if not args.nftables:
			args.iptables_info, args.err = shell_run(args.console, switch_iptables(args, 'read'))
		else:
			args.iptables_info, args.err = shell_run(args.console, switch_nftables(args, 'search'))
		if args.nolog:
			args.log_txt.append('Reload the blacklist ...')
			args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
		args.add = False
		service_start_stop(args)
		args.add = True
		if not args.nftables:
			args.iptables_info, args.err = shell_run(args.console, switch_iptables(args, 'read'))
		else:
			args.iptables_info, args.err = shell_run(args.console, switch_nftables(args, 'search'))
		service_start_stop(args)
		print('Exit the blacklist ...')
		if args.nolog:
			args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
			args.log_txt.append(f"Exit the blacklist ...")
		AppExit(args)
	if not args.log_txt:
		parser.parse_args(['service', '-h'])
		sys.exit(0)

def nft_ban_unban_one(args: Arguments):
	''' NFTABLES ban or unban one ip address. '''
	
	def banunban_nohost(not_found: str):
		''' A single team is banned and disbanded. '''
		nonlocal comm
		nonlocal mess
		nonlocal on_handle
		nonlocal args
		comm = switch_cmds(args.onlist).get(str(args.add), not_found)
		mess = switch_messages(args.onlist).get(str(args.add), not_found)
		on_handle = search_handle(args.iptables_info, args.current_ip)
		shell_run(args.console, switch_nftables(args, comm, on_handle))
		print(f"* {mess} {args.current_ip}")
		if args.nolog:
			args.log_txt.append(f"* {mess} {args.current_ip}")
	
	nomask = ip_no_mask(args.current_ip)
	comm = ''
	mess = ''
	on_handle = ''
	if args.add:
		if not nomask in args.iptables_info:
			banunban_nohost('add-black')
	else:
		if nomask in args.iptables_info:
			banunban_nohost('del-black')

def ban_unban_one(args: Arguments):
	''' Ban or unban one ip address. '''
	
	def banunban_host_nohost(not_found: str, ishostname: bool):
		''' A single team is banned and disbanded. '''
		nonlocal hostname
		nonlocal nomask
		nonlocal args
		nonlocal hostname
		nonlocal comm
		comm = switch_cmds(args.onlist).get(str(args.add), not_found)
		mess = switch_messages(args.onlist).get(str(args.add), not_found)
		shell_run(args.console, switch_iptables(args, comm))
		if ishostname:
			args.old = args.current_ip
			args.current_ip = hostname
			shell_run(args.console, switch_iptables(args, comm))
			args.current_ip = args.old
			args.old = None
		print(f"* {mess} {args.current_ip} / {hostname}")
		if args.nolog:
			args.log_txt.append(f"* {mess} {args.current_ip} / {hostname}")
	
	def quastion_hostname_nomask(not_found: str):
		''' The issue of processing a domain name 
			during a ban or unban. '''
		nonlocal hostname
		nonlocal nomask
		nonlocal args
		nonlocal hostname
		nonlocal comm
		if hostname != nomask:
			if not hostname in args.iptables_info:
				banunban_host_nohost(not_found, True)
		else:
			banunban_host_nohost(not_found, False)
	
	nomask = ip_no_mask(args.current_ip)
	hostname = ip_to_hostname(nomask)
	comm = ''
	if args.add:
		if not nomask in args.iptables_info:
			quastion_hostname_nomask('add-black')
	else:
		if nomask in args.iptables_info:
			quastion_hostname_nomask('del-black')
		else:
			if hostname != nomask:
				if hostname in args.iptables_info:
					banunban_host_nohost('del-black', True)

def listwork(args: Arguments):
	''' Working with lists. '''
	
	global parser
	
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
		if not args.nftables:
			args.iptables_info, args.err = shell_run(args.console, switch_iptables(args, 'read'))
		else:
			args.iptables_info, args.err = shell_run(args.console, switch_nftables(args, 'search'))
		for elem in range(len(args.ip)):
			args.current_ip = ip_to_net(args.ip[elem], args.mask[elem]) if len(args.mask) > elem else ip_to_net(args.ip[elem], args.maxmask)
			if not args.nftables:
				ban_unban_one(args)
			else:
				nft_ban_unban_one(args)
		args.current_ip = None
	
	def add_del_one(args: Arguments):
		''' Add or remove one ip address. '''
		if args.delete:
			if args.json_data.get(args.current_ip):
				del args.json_data[args.current_ip]
				if args.nolog:
					args.log_txt.append(f"del {args.current_ip}")
		else:
			if args.json_data.get(args.current_ip, '-') != '-':
				args.json_data[args.current_ip] = args.json_data[args.current_ip] + 1 if args.quantity == 0 else args.quantity
				if args.nolog:
					args.log_txt.append(f"add {args.current_ip} = {args.json_data[args.current_ip]}")
			else:
				args.json_data[args.current_ip] = 1 if args.quantity == 0 else args.quantity
				if args.nolog:
					args.log_txt.append(f"add {args.current_ip} = {args.json_data[args.current_ip]}")
	
	def add_dell_full(args: Arguments):
		''' Adding or deleting all entered ip addresses. '''
		args.json_data = args.blacklist_json if args.onlist == 'black' else args.whitelist_json
		for elem in range(len(args.ip)):
			args.current_ip = ip_to_net(args.ip[elem], args.mask[elem]) if len(args.mask) > elem else ip_to_net(args.ip[elem], args.maxmask)
			add_del_one(args)
		if args.save:
			read_write_json(args.output, 'w', args.json_data)
		args.current_ip = None
		args.json_data = None
	
	print('Launching the blacklist ...')
	if args.nolog:
		args.log_txt.append(f"Launching the blacklist ...")
	
	if args.show:
		print('Viewing a blacklist or whitelist of ip addresses ...')
		args.log_txt.append('Viewing a blacklist or whitelist of ip addresses ...')
		args.log_txt.append('Exit the blacklist ...')
		read_list(args)
		show_list(args)
		print('Exit the blacklist ...')
		sys.exit(0)
	if args.ban:
		print('Ban the blacklist or ignore the whitelist ip addresses ...')
		if args.nolog:
			args.log_txt.append(f"Ban the blacklist or ignore the whitelist ip addresses ...")
		args.old = args.add
		args.add = True
		ban_unban_full(args)
		args.add = args.old
		args.old = None
		args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
	if args.unban:
		print('Unban the blacklist or delete ignored the whitelist ip addresses ...')
		if args.nolog:
			args.log_txt.append(f"Unban the blacklist or delete ignored the whitelist ip addresses ...")
		args.old = args.add
		args.add = False
		ban_unban_full(args)
		args.add = args.old
		args.old = None
		args.log_txt.append(f"----- ERROR Info -----\n{args.err}\n----- ERROR Info -----")
	if args.add:
		print('Adding the blacklist or whitelist ip addresses ...')
		if args.nolog:
			args.log_txt.append(f"Adding the blacklist or whitelist ip addresses ...")
		read_list(args)
		add_dell_full(args)
	if args.delete:
		print('Deleting the blacklist or whitelist ip addresses ...')
		if args.nolog:
			args.log_txt.append(f"Deleting the blacklist or whitelist ip addresses ...")
		read_list(args)
		add_dell_full(args)
	print('Exit the blacklist ...')
	if args.nolog:
		rez = args.show + args.ban + args.unban + args.add + args.delete
		if rez == 0:
			if args.onlist == 'black':
				parser.parse_args(['black', '-h'])
			if args.onlist == 'white':
				parser.parse_args(['white', '-h'])
			sys.exit(0)
		args.log_txt.append(f"Exit the blacklist ...")
	AppExit(args)

def PersonalParam(args: Arguments):
	''' Uses personal standart {IP,IP6,NF}TABLES Params. '''
	if args.personal:
		if args.nftables:
			args.nftproto = 'inet'
			args.table = 'blackwhite'
			args.chain = 'INPUT'
		else:
			args.table = 'filter'
			args.chain = 'blackwhite'
	if args.fine:
		args.clearchain = True
		args.delchain = True
		args.cleartable = True
		args.deltable = True
	
	if args.nftables:
		if args.newtable:
			if args.table != 'filter':
				print('Start the blacklist ...')
				args.log_txt.append('Start the blacklist ...')
				args.log_txt.append(f"New table in NFTABLES  = {args.table}")
				print(f"New table in NFTABLES  = {args.table}")
				service_info, err = shell_run(args.console, switch_nftables(args, 'create-table'))
				args.log_txt.append(service_info)
				print(service_info)
				args.log_txt.append('Exit the blacklist ...')
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print('Exit the blacklist ...')
				if args.exit:
					AppExit(args)
		if args.newchain:
			if (args.table != 'filter') ^ (args.chain != 'INPUT'):
				print('Start the blacklist ...')
				args.log_txt.append('Start the blacklist ...')
				args.log_txt.append(f"New chain in NFTABLES  = {args.chain}")
				print(f"New chain in NFTABLES  = {args.chain}")
				service_info, err = shell_run(args.console, switch_nftables(args, 'create-chain'))
				args.log_txt.append(service_info)
				print(service_info)
				args.log_txt.append('Exit the blacklist ...')
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print('Exit the blacklist ...')
				if args.exit:
					AppExit(args)
	else:
		if args.newchain:
			if args.chain != 'INPUT':
				print('Start the blacklist ...')
				args.log_txt.append('Start the blacklist ...')
				args.log_txt.append(f"New chain in IP(6)TABLES  = {args.chain}")
				print(f"New chain in IP(6)TABLES  = {args.chain}")
				service_info, err = shell_run(args.console, switch_iptables(args, 'create-chain'))
				args.log_txt.append(service_info)
				print(service_info)
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print('Next the blacklist ...')
				args.log_txt.append('Next the blacklist ...')
				args.log_txt.append(switch_iptables(args, 'create-return'))
				print(switch_iptables(args, 'create-return'))
				service_info, err = shell_run(args.console, switch_iptables(args, 'create-return'))
				args.log_txt.append(service_info)
				print(service_info)
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print('Next the blacklist ...')
				args.log_txt.append('Next the blacklist ...')
				args.log_txt.append(switch_iptables(args, 'create-input'))
				print(switch_iptables(args, 'create-input'))
				service_info, err = shell_run(args.console, switch_iptables(args, 'create-input'))
				args.log_txt.append(service_info)
				print(service_info)
				args.log_txt.append(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print(f"----- ERROR Info -----\n{err}\n----- ERROR Info -----")
				print('Exit the blacklist ...')
				args.log_txt.append('Exit the blacklist ...')
				if args.exit:
					AppExit(args)

def EditTableParam(args: Arguments):
	''' Edit online param on {IP,IP6,NF}TABLES. '''
	if not args.nftables:
		args.protocol = 'iptables' if not args.ipv6 else 'ip6tables'
		args.table = 'filter'
	else:
		if args.protocol == 'ip':
			args.protocol = 'ip' if not args.ipv6 else 'ip6'
		if args.nftproto == 'ip':
			args.nftproto = 'ip' if not args.ipv6 else 'ip6'
	
	if not args.ipv6:
		args.minmask = 1
		args.maxmask = 32
	else:
		args.minmask = 1
		args.maxmask = 128
	
	if args.mask != None:
		if len(args.mask) > 1:
			for elem in range(len(args.mask)):
				if args.mask[elem] < args.minmask:
					args.mask[elem] = args.minmask
				elif args.mask[elem] > args.maxmask:
					args.mask[elem] = args.maxmask
	
	PersonalParam(args)

def EditDirParam(args: Arguments):
	''' Edit online directoryes Params. '''	
	
	global workdir
	global json_black
	global json_white
	global blacklist_name
	global whitelist_name
	
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
	
	if args.logfile != '':
		if args.logfile != None:
			args.logfile = pathlib.Path(f"{args.logfile}").resolve()
	
	if not pathlib.Path(str(workdir)).resolve().exists():
		pathlib.Path(str(workdir)).resolve().mkdir(parents=True)

def EditLogParam(args: Arguments):
	''' Edit online Log Params. '''
	
	def stampToStr(timeStamp: int, strFormat = "%d.%m.%Y-%H:%M:%S") -> str:
		dateTime = datetime.fromtimestamp(timeStamp)
		datestr = dateTime.strftime(strFormat)
		return datestr
	
	if not args.logfile.exists():
		args.logfile.touch(mode=0o744)
	else:
		if args.limit:
			file_date = stampToStr(args.logfile.stat().st_mtime, "%d.%m.%Y")
			ondate = datetime.now().strftime("%d.%m.%Y")
			if file_date != ondate:
				read_write_text(args.logfile, 'w', '\n')
		if args.viewlog:
			print(read_write_text(args.logfile, 'r'))
			sys.exit(0)
		if args.resetlog:
			read_write_text(args.logfile, 'w', '\n')
			sys.exit(0)

def test_arguments(args: Arguments):
	''' Test arguments and edit online parameters... '''
	
	if args.count < 0:
		print("The number of locks to display cannot be a negative number (from 0 and above.)!")
		args.count = 0
	if args.quantity < 0:
		print("The number of locks to save cannot be a negative number (from 0 and above.)!")
		args.quantity = 0
	
	EditDirParam(args)
	EditLogParam(args)
	EditTableParam(args)

def main():	
	''' The main cycle of the program. '''
	
	global infromation, service_text, parser
	
	parser, sb1, psvc, psd, pbl, pwl, pgr1, pgr2, gr1, gr2, gr3, gr4 = createParser()
	args = Arguments()
	parser.parse_args(namespace=Arguments)
	
	if args.nolog:
		args.log_txt = []
		args.log_txt.clear()
	
	test_arguments(args)
	
	func = {
			'service': servicework,
			'systemd': systemdwork,
			'black': listwork,
			'white': listwork
			}
	
	if args.info:
		print(infromation)
		sys.exit(0)
	
	if args.onlist != None:
		func.get(args.onlist)(args)
	else:
		if args.exit:
			AppExit(args)
		parser.parse_args(['-h'])

if __name__ == '__main__':
	main()
else:
	main()
