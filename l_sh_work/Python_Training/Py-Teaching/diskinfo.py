#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

# from os import environ

class ByteSize(int):

	_kB = 1024
	_suffixes = 'B', 'kB', 'MB', 'GB', 'PB'

	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, *args, **kwargs):
		self.bytes = self.B = int(self)
		self.kilobytes = self.kB = self / self._kB**1
		self.megabytes = self.MB = self / self._kB**2
		self.gigabytes = self.GB = self / self._kB**3
		self.petabytes = self.PB = self / self._kB**4
		*suffixes, last = self._suffixes
		suffix = next((
			suffix
			for suffix in suffixes
				if 1 < getattr(self, suffix) < self._kB
		), last)
		self.readable = suffix, getattr(self, suffix)

		super().__init__()

	def __str__(self):
		return self.__format__('.2f')

	def __repr__(self):
		return '{}({})'.format(self.__class__.__name__, super().__repr__())

	def __format__(self, format_spec):
		suffix, val = self.readable
		return '{val:{fmt}} {suf}'.format(val=val, fmt=format_spec, suf=suffix)

	def __sub__(self, other):
		return self.__class__(super().__sub__(other))

	def __add__(self, other):
		return self.__class__(super().__add__(other))

	def __mul__(self, other):
		return self.__class__(super().__mul__(other))

	def __rsub__(self, other):
		return self.__class__(super().__sub__(other))

	def __radd__(self, other):
		return self.__class__(super().__add__(other))
    
	def __rmul__(self, other):
		return self.__class__(super().__rmul__(other))

def get_folder_size(folder):
	return ByteSize(sum(file.stat().st_size for file in Path(folder).rglob('*')))

def size_format(in_size):
	if in_size < 1000:
		return f"{in_size} B"
	elif 1000 <= in_size < 1000000:
		#return '%.1f' % float(in_size/1000) + ' KB'
		return f"{float(in_size/1000):.1f} KB"
	elif 1000000 <= in_size < 1000000000:
		#return '%.1f' % float(in_size/1000000) + ' MB'
		return f"{float(in_size/1000000):.1f} MB"
	elif 1000000000 <= in_size < 1000000000000:
		# return '%.1f' % float(in_size/1000000000) + ' GB'
		return f"{float(in_size/1000000000):.1f} GB"
	elif 1000000000000 <= in_size:
		#return '%.1f' % float(in_size/1000000000000) + ' TB'
		return f"{float(in_size/1000000000000):.1f} TB"

def main():
	total, used, free = shutil.disk_usage("/") # C:
	#print("Total: %d GiB" % (total // (2**30)))
	#print("Used: %d GiB" % (used // (2**30)))
	#print("Free: %d GiB" % (free // (2**30)))
	print(f"Total: {total // (2**30)} GiB")
	print(f"Used: {used // (2**30)} GiB")
	print(f"Free: {free // (2**30)} GiB")
	
	#tmp_dir = environ.get('temp')
	tmp_dir = '/home/mikl/003/'
	#tmp_dir = '/run/media/mikl/ADATA UFD/'
	nbytes = sum(f.stat().st_size for f in Path(tmp_dir).rglob('*') if f.is_file())
	print(f"{size_format(nbytes)}.")
	size = get_folder_size(tmp_dir)
	print(size)

if __name__ == '__main__':
	main()
