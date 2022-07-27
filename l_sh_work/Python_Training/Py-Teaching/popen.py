#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess

def main():
	cmds = ['chcp 1252', 'net user', 'whoami', 'wmic printer list brief', 'ping -n 2 ya.ru']
	
	p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True) # encoding='utf-8'
		
	for cmd in cmds:
		sys.stdout.flush()
		p.stdin.write(cmd + "\n")
	p.stdin.close()
	with open('logfile.txt', 'w') as logfile:
		logfile.write(p.stdout.read())
	p.terminate()
	p.kill()

if __name__ == '__main__':
	main()
