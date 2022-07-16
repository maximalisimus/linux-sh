#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shlex

def main():
	# command_line = input()
	command_line = '/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd \'echo "$MONEY"\''
	args = shlex.split(command_line)
	print(args)
	# ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', 'echo "$MONEY"']

if __name__ == '__main__':
	main()
