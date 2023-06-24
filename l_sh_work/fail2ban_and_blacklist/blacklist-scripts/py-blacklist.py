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
#json_file = pathlib.Path('./ip-blacklist.json').resolve()

class Arguments:
	
	def __getattr__(self, attrname):
		''' Access to a non-existent variable. '''
		return None
	
	def __repr__(self):
		''' For Debug Function output paramters '''
		return f"{self.__class__}:\n" + \
				f"\tadd: {self.add},\n" + \
				f"\tdelete: {self.delete},\n" + \
				f"\tshow: {self.show},\n" + \
				f"\tcount: {self.count},\n" + \
				f"\tip: {self.ip},\n" + \
				f"\tnetmask: {self.netmask},\n" + \
				f""

def createParser():
	parser = argparse.ArgumentParser(prog=progname,description='The Fail2Ban blacklist in Python.')
	parser.add_argument ('-v', '--version', action='version', version=f'{progname} {__version__}',  help='Version.')
	parser.add_argument ('-a', '--add', action='store_true', default=False, help='Add to the blacklist.')
	parser.add_argument ('-d', '--delete', action='store_true', default=False, help='Remove from the blacklist.')
	parser.add_argument ('-s', '--show', action='store_true', default=False, help='Read the blacklist..')
	group1 = parser.add_argument_group('extend', 'Entering the address.')
	group1.add_argument("-c", '--count', dest="count", metavar='COUNT', type=int, default=0, help='The number of locks after which the address is entered in IPTABLES.')
	group1.add_argument("-ip", '--ip', dest="ip", metavar='IP', type=str, default='17.253.144.10', help='IP address (single or network).')
	group1.add_argument("-n", '--netmask', dest="netmask", metavar='NETMASK', type=int, default=24, help='The network mask.')
	return parser, group1

def read_write_json(jfile, typerw, data = dict()):
	with open(jfile, typerw) as fp:
		if typerw == 'r':
			data = json.load(fp)
			return data
		else:
			json.dump(data, fp, indent=2)

def main():
	global json_file
	json_data = dict()
	json_data = read_write_json( json_file, 'r')
	
	parser, gr1 = createParser()
	args = Arguments()
	parser.parse_args(namespace=Arguments)
	
	myip = args.ip.split('/', 1)[0] + '/' + str(args.netmask)
	myhost = ipaddress.ip_interface(myip)
	mynet = f"{myhost.network}"
	
	if args.add:
		if not json_data.get(mynet):
			json_data[mynet] = 1
			read_write_json(json_file, 'w', json_data)
		else:
			count = json_data[mynet]
			json_data[mynet] = count + 1
			read_write_json(json_file, 'w', json_data)
		sys.exit(0)
	if args.delete:
		if json_data.get(mynet):
			del json_data[mynet]
			read_write_json(json_file, 'w', json_data)
		sys.exit(0)
	if args.show:
		if args.count == 0:
			print('\n'.join(tuple(f"{k}: {v}" for k,v in json_data.items() if v >= 1)))
		else:
			print('\n'.join(tuple(k for k,v in json_data.items() if v >= args.count)))
		sys.exit(0)

if __name__ == '__main__':
	main()
else:
	main()