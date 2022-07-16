#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shlex

def main():
	# command_line = input()
	command_line = '/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd \'echo "$MONEY"\''
	args = shlex.split(command_line)
	print(args, '\n')
	# ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', 'echo "$MONEY"']
	text = """This string has embedded "double quotes" and
'single quotes' in it, and even "a 'nested example'"."""
	lexer = shlex.shlex(text)
	for token in lexer:
		print('{!r}'.format(token))
	filename = 'somefile; rm -rf ~'
	command = f'ls -l {filename}'
	print('\n', command)
	# or
	command = f'ls -l {shlex.quote(filename)}'
	print(command, '\n')
	#
	import pprint
	pprint.pprint(args, width='60')

if __name__ == '__main__':
	main()
