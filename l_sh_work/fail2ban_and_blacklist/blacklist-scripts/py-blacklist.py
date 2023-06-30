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

json_file = pathlib.Path('/etc/blacklist-scripts/ip-blacklist.json').resolve()
json_ignore = pathlib.Path('/etc/blacklist-scripts/ip-whitelist.json').resolve()
#json_file = pathlib.Path('./ip-blacklist.json').resolve()
#json_ignore = pathlib.Path('./ip-whitelist.json').resolve()

json_out=''

class Arguments:
	
	def __getattr__(self, attrname):
		''' Access to a non-existent variable. '''
		return None
	
	def __repr__(self):
		''' For Debug Function output paramters '''
		return f"{self.__class__}:\n" + \
				f"\tadd: {self.add},\n" + \
				f"\tdelete: {self.delete},\n" + \
				f"\tignore: {self.ignore},\n" + \
				f"\tshow: {self.show},\n" + \
				f"\tcount: {self.count},\n" + \
				f"\tquantity: {self.quantity},\n" + \
				f"\tip: {self.ip},\n" + \
				f"\tnetmask: {self.netmask},\n" + \
				f"\tjson: {self.json},\n" + \
				f"\toutfile: {self.outfile},\n" + \
				f"\tinfile: {self.infile},\n" + \
				f""

def createParser():
	parser = argparse.ArgumentParser(prog=progname,description='The Fail2Ban blacklist in Python.')
	parser.add_argument ('-v', '--version', action='version', version=f'{progname} {__version__}',  help='Version.')
	parser.add_argument ('-a', '--add', action='store_true', default=False, help='Add to the blacklist.')
	parser.add_argument ('-d', '--delete', action='store_true', default=False, help='Remove from the blacklist.')
	parser.add_argument ('-s', '--show', action='store_true', default=False, help='Read the blacklist..')
	parser.add_argument ('-i', '--ignore', action='store_true', default=False, help='Whitelist address.')
	
	group1 = parser.add_argument_group('address', 'Entering the address.')
	group1.add_argument("-c", '--count', dest="count", metavar='COUNT', type=int, default=0, help='The number of locks after which the address is entered in IPTABLES.')
	group1.add_argument("-q", '--quantity', dest="quantity", metavar='QUANTITY', type=int, default=0, help='How many times the address has been banned.')
	group1.add_argument("-ip", '--ip', metavar='IP', type=str, default=['17.253.144.10/32'], nargs='+', help='IP address.')
	group1.add_argument("-n", '--netmask', dest="netmask", metavar='NETMASK', type=int, default=[], nargs='+', help='The network mask.')
	group2 = parser.add_argument_group('Files', 'Working with files.')
	group2.add_argument ('-j', '--json', action='store_true', default=False, help='Show in json format.')
	group2.add_argument("-if", '--infile', dest="infile", metavar='INFILE', type=str, default='', help='Input file.')
	group2.add_argument("-of", '--outfile', dest="outfile", metavar='OUTFILE', type=str, default='', help='Output file.')
	
	return parser, group1, group2

def read_write_json(jfile, typerw, data = dict()):
	with open(jfile, typerw) as fp:
		if typerw == 'r':
			data = json.load(fp)
			return data
		else:
			json.dump(data, fp, indent=2)

def read_write_text(outfile, typerw, data = ""):
	with open(outfile, typerw) as fp:
		fp.write(data)

def ip_to_net(in_ip, in_mask = 32):	
	net_ip = str(in_ip).split('/', 1)[0]
	if '/' in str(in_ip):
		net_mask = str(in_ip).split('/', 1)[1]
	else:
		net_mask = str(in_mask)
	out_ip = net_ip + '/' + net_mask
	my_host = ipaddress.ip_interface(out_ip)
	out_ip = f"{my_host.network}"
	return out_ip

def main():
	global json_file
	global json_ignore
	
	parser, gr1, gr2 = createParser()
	args = Arguments()
	parser.parse_args(namespace=Arguments)
	
	if args.infile != '':
		json_in = pathlib.Path(args.infile).resolve()
	else:
		if args.ignore:
			json_in = json_ignore
		else:
			json_in = json_file
	
	if not json_in.parent.exists():
		json_in.parent.mkdir(parents=True)
	
	if args.outfile != '':
		json_out = pathlib.Path(args.outfile).resolve()
	else:
		if args.ignore:
			json_out = json_ignore
		else:
			json_out = json_file
	
	if not json_out.parent.exists():
		json_out.parent.mkdir(parents=True)
	
	json_data = dict()
	if not json_in.exists():
		json_in.touch(mode=0o755, exist_ok=True)
	else:
		json_data = read_write_json(json_in, 'r', dict())
	
	if args.add:
		ipnetip = ""
		for elem in range(len(args.ip)):
			if len(args.netmask) > elem:
				ipnetip = ip_to_net(args.ip[elem], args.netmask[elem])
			else:
				ipnetip = ip_to_net(args.ip[elem])
			if json_data.get(ipnetip, '-') != '-':
				if args.quantity == 0:
					count = json_data[ipnetip]
					json_data[ipnetip] = count + 1
				else:
					json_data[ipnetip] = args.quantity
			else:
				if args.quantity == 0:
					json_data[ipnetip] = 1
				else:
					json_data[ipnetip] = args.quantity
		read_write_json(json_out, 'w', json_data)
		sys.exit(0)
	if args.delete:
		ipnetip = ""
		for elem in range(len(args.ip)):
			if len(args.netmask) > elem:
				ipnetip = ip_to_net(args.ip[elem], args.netmask[elem])
			else:
				ipnetip = ip_to_net(args.ip[elem])
			if json_data.get(ipnetip):
				del json_data[ipnetip]
		read_write_json(json_out, 'w', json_data)
		sys.exit(0)
	if args.show:
		if args.json:
			if args.outfile == '':
				print(json.dumps(json_data, indent=2))
			else:
				data2 = json.dumps(json_data, indent=2)
				read_write_text(pathlib.Path(args.outfile).resolve(), 'w', f"{data2}")
		else:
			if args.outfile == '':
				if args.count == 0:
					print('\n'.join(tuple(f"{k}: {v}" for k,v in json_data.items() if v >= 1)))
				else:
					print('\n'.join(tuple(k for k,v in json_data.items() if v >= args.count)))
			else:
				if args.count == 0:
					data2 = '\n'.join(tuple(f"{k}: {v}" for k,v in json_data.items() if v >= 1))
					read_write_text(pathlib.Path(args.outfile).resolve(), 'w', f"{data2}")
				else:
					data2 = '\n'.join(tuple(k for k,v in json_data.items() if v >= args.count))
					read_write_text(pathlib.Path(args.outfile).resolve(), 'w', f"{data2}")
		sys.exit(0)
	
	

if __name__ == '__main__':
	main()
else:
	main()
