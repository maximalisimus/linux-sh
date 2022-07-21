#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

def main():
	path = pathlib.Path('/home/mikl/003/Primer/pkg/compatible/')
	secondparent = path.parent.parent
	homedir = pathlib.Path('/home/mikl/')
	print(str(path.relative_to(secondparent)))
	print(str(path.relative_to(homedir)))

if __name__ == '__main__':
	main()
