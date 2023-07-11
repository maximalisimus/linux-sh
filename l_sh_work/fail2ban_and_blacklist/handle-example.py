#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def ip_no_mask(in_ip) -> str:
	''' Convert an ip address to an address without a network mask. '''
	return str(in_ip).split('/', 1)[0]

def mask_no_ip(in_ip) -> str:
	''' Get an ip address mask or assign a predefined value 
		or default value. '''
	if '/' in str(in_ip):
		net_mask = str(in_ip).split('/', 1)[1]
	else:
		net_mask = None
	return str(net_mask)

def search_handle(lines: str, in_ip):
	nomask = ip_no_mask(in_ip)
	pattern = f"{nomask}"
	search = re.search(pattern, lines)
	if search != None:
		lines = lines[search.span()[0]:].split('\n')[0]
	else:
		return None
	pattern = '# handle '
	search = re.search(pattern, lines).span()
	if search != None:
		lines = lines[search[1]:]
	else:
		return None
	try:
		return int(lines)
	except:
		return None

def main():
	with open('./nftables-example.txt', 'r') as fp:
		lines = fp.read()
	ip = '10.10.10.0/24'
	nomask = ip_no_mask(ip)
	mask = mask_no_ip(ip)
	maxmask = 32
	minmask = 0
	mask = maxmask if mask == 'None' else mask
	mask = minmask if int(mask) == 0 else mask
	if nomask in lines:
		handle = search_handle(lines, ip)
		print(type(handle), handle)

if __name__ == '__main__':
	main()
