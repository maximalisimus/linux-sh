#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pathlib
import sys

json_file = pathlib.Path('/etc/blacklist-scripts/ip-blacklist.json').resolve()
#json_file = pathlib.Path('./ip-blacklist.json').resolve()

def main():
	with open(json_file, 'r') as fp:
		json_data = json.load(fp)
	if len(sys.argv) == 1:
		print('\n'.join(tuple(f"{k}: {v}" for k,v in json_data.items() if v >= 1)))
	elif len(sys.argv) > 1:
		print('\n'.join(tuple(k for k,v in json_data.items() if v >= int(sys.argv[1]))))
		

if __name__ == '__main__':
	main()
