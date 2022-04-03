#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

def int_r(num):
	num = int(num + (0.5 if num > 0 else -0.5))
	return num

def genrand(sizes):
	s1 = int(sizes)
	s2 = s1 - 1
	if (int(s1) >= 512):
		sz = int_r(s1/18)+232-32
		s1-=sz
		s2-=sz
		a = random.randint(1 << s2, (1 << s1) - 1)
	return a

def main():
	numb = genrand(1024+512+256) # 1792
	print(numb)
	print(sys.getsizeof(numb)*8)

if __name__ == '__main__':
	main()
