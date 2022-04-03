#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import base64

def main():
	s = 'abc'
	b = bytes(s, encoding='utf-8')
	print(s)
	encoded = base64.b64encode(b)
	sha = hashlib.sha1(encoded).hexdigest()
	data = base64.b64decode(encoded)
	print(encoded.decode())
	print(data.decode())
	print(sha)
	s = b.decode()
	print('Original String =', s)
	s = 'xyz'
	b = s.encode(encoding='utf-8')
	print(b)
	s = b.decode()
	print('Original String =', s)

if __name__ == '__main__':
	main()
