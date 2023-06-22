#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pathlib
import sys
import ipaddress

json_file = pathlib.Path('/etc/blacklist-scripts/ip-blacklist.json').resolve()
#json_file = pathlib.Path('./ip-blacklist.json').resolve()

def main():
	with open(json_file, 'r') as fp:
		json_data = json.load(fp)
	if len(sys.argv) > 1:
		myip = str(sys.argv[1]).split('/', 1)[0] + "/24"
		print(myip)
		myhost = ipaddress.ip_interface(myip)
		mynet = f"{myhost.network}"
		if json_data.get(mynet):
			del json_data[mynet]
			with open(json_file, 'w') as fp:
				json.dump(json_data, fp, indent=2)

if __name__ == '__main__':
	main()
