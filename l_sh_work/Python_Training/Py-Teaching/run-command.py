#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def main():
	#process = subprocess.run(['ls', '-l', '-a'])
	process = subprocess.run(['ls', '-l', '-a'], capture_output=True)
	print(process.returncode)
	print(process.stdout.decode('UTF-8'),'\n')
	process = subprocess.run('ls -al $HOME/005', shell=True, capture_output=True)
	print(process.returncode)
	print(process.stderr.decode('UTF-8'))
	print(process.stdout.decode('UTF-8'))

if __name__ == '__main__':
	main()
