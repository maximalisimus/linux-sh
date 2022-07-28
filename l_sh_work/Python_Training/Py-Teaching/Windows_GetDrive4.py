#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import win32api
import win32file

# pip install pywin32 pywin32-ctypes

from enum import Enum

class NoValue(Enum):

	def __repr__(self):
		return f"{self.__class__}: {self.name}"
	
	def __str__(self):
		return f"{self.name}"
	
	def __call__(self):
		return f"{self.value}"

class TypeDisk(NoValue):
	def __init__(self, on_type: win32file = win32file.DRIVE_UNKNOWN, on_value: str = ''):
		self.on_type = on_type
		self.on_value = on_value
	Unknown = (win32file.DRIVE_UNKNOWN, "Unknown Drive type can't be determined.")
	Local = (win32file.DRIVE_FIXED, "Fixed Drive has fixed (nonremovable) media. This includes all hard drives, including hard drives that are removable.")
	USB = (win32file.DRIVE_REMOVABLE, "Removable Drive has removable media. This includes all floppy drives and many other varieties of storage devices.")
	Network = (win32file.DRIVE_REMOTE, "Remote Network drives. This includes drives shared anywhere on a network.")
	CDROM = (win32file.DRIVE_CDROM, "CDROM Drive is a CD-ROM. No distinction is made between read-only and read/write CD-ROM drives.")
	RAM = (win32file.DRIVE_RAMDISK, "RAMDisk Drive is a block of random access memory (RAM) on the local computer that behaves like a disk drive.")
	NO_ROOT = (win32file.DRIVE_NO_ROOT_DIR, "The root directory does not exist.")
	
	@classmethod
	def GetTypeDisk(cls, value: int):
		for item in cls:
			if item.on_type == value:
				return item
	
	def __call__(self):
		return f"{self.on_value}"

def main():
	drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
	for device in drives:
		diskinfo = TypeDisk.GetTypeDisk(win32file.GetDriveType(device))
		print("Drive: %s" % device)
		print(diskinfo)
		print(diskinfo())
		print("-"*72)

if __name__ == '__main__':
	main()
