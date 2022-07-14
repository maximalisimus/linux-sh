#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def switch(case):
	return {
		"param1": 1,
		"param2": 2,
		"param3": 3
	}.get(case, None)

def main():
	for count in range(len(sys.argv)):
		if switch(sys.argv[count]) == 1: print('Param 1')
		if switch(sys.argv[count]) == 2: print('Param 2')
		if switch(sys.argv[count]) == 3: print('Param 3')
	#
	# or
	#
	print('\n')
	params = 'param1'
	if switch(params) == 1: print('Param 1')
	params = 'param2'
	if switch(params) == 2: print('Param 2')
	params = 'param3'
	if switch(params) == 3: print('Param 3')

if __name__ == '__main__':
	main()
