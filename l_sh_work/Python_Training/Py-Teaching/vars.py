#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def remove_var(variable):
	try:
		del(variable)
	except NameError:
		pass
	except Exception as e:
		print(e)

def main():
	#s = "s1,s2;s2,s1;s2,s3;s3,s2;s3,s4;s4,s3"
	s = "s1,s2;s2,s1;s1,s3;s3,s1;s2,s4;s4,s2;s3,s4;s4,s3"
	lst = list(tuple(str(item).split(',')) for item in s.split(';'))
	print(lst)
	s2 = s.replace(';',',')
	print(s2)
	el = list(set(s2.split(',')))
	remove_var(s)
	remove_var(s2)
	el.sort()
	print(el)
	print(el[0])
	s = "s1,s2;s2,s1;s2,s3;s3,s2;s3,s4;s4,s3"
	s2 = s.replace(';',',')
	print(s2)
	el = list(set(s2.split(',')))
	remove_var(s)
	remove_var(s2)
	el.sort()
	print(el)
	print(el[0])

if __name__ == '__main__':
	main()
