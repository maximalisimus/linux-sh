#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from pathlib import Path

from enum import Enum

class NoValue(Enum):

	def __repr__(self):
		return f"{self.__class__}: {self.name}"
	
	def __str__(self):
		return f"{self.name}"
	
	def __call__(self):
		return f"{self.value}"

class TypeDisk(NoValue):
	Local = 'Local Fixed Disk'
	USB = 'Removable Disk'
	Network = 'Network Connection'
	CDROM = 'CD-ROM Disk'

def PsysicalDisk(DiskType: TypeDisk = TypeDisk.Local) -> list:
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	drives = [f'{d}:' for d in letters if Path(f"{d}:").exists()]
	raw_disk = ''
	data = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
	sys.stdout.flush()
	data.stdin.write('chcp 1252' + "\n")
	sys.stdout.flush()
	data.stdin.write('wmic logicaldisk get description,name' + "\n")
	data.stdin.close()
	# Debug
	# print(data.stdout.read())
	raw_disk = data.stdout.read().strip().split('\n')
	data.terminate()
	data.kill()
	data_disk = []
	for x in drives: 
		for y in raw_disk: 
			if x in y and DiskType().lower() in y.lower():
				data_disk.append(x)
	return list(set(data_disk))

def main():
	drives = PsysicalDisk()
	print(drives)

if __name__ == '__main__':
	main()
