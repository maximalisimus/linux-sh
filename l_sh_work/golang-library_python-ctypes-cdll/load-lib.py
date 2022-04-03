#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import *

def main():
	lib = cdll.LoadLibrary("./genrsa_lib.so")
	lib.GenRsa.argtypes = [c_longlong]
	lib.GenRsa(4096)

if __name__ == '__main__':
	main()
