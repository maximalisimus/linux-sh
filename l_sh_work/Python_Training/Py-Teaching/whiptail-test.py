#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import whiptail
import pathlib

# pip install whiptail-dialogs

def main():
	pass
	# Whiptail title backtitle height width auto_exit
	#
	# Methods
	# checklist(self, msg: str = '', items: Union[Sequence[str], Sequence[Iterable[str]]] = (), prefix: str = ' - ') -> Tuple[List[str], int]
	# inputbox(self, msg: str, default: str = '', password: bool = False) -> Tuple[str, int]
	# menu(self, msg: str = '', items: Union[Sequence[str], Sequence[Iterable[str]]] = (), prefix: str = ' - ') -> Tuple[str, int]
	# msgbox(self, msg: str) -> None
	# radiolist(self, msg: str = '', items: Union[Sequence[str], Sequence[Iterable[str]]] = (), prefix: str = ' - ') -> Tuple[List[str], int]
	# textbox(self, path: Union[str, pathlib.Path, os.PathLike]) -> int
	# yesno(self, msg: str, default='yes') -> bool
	# 
	MyList = [['1', 'Grilled Spicy Sausage'], ['2', 'Grilled Halloumi Cheese'], ['3', 'Charcoaled Chicken Wings'], ['4', 'Fried Aubergine']]
	title = 'Test Menu Dialog'
	menu = 'Choose your option'
	message = 'Text dialog'
	default_text = 'Default text'
	width = 0
	height = 0
	backtitle = 'MyDialogs'
	mydialog = whiptail.Whiptail(title=title, backtitle=backtitle, height=height, width=width)
	select, code = mydialog.menu(msg = menu, items=MyList)
	print(code)
	print(select, '\n')
	MyList = [['1', 'Grilled Spicy Sausage', 'OFF'], ['2', 'Grilled Halloumi Cheese', 'OFF'], ['3', 'Charcoaled Chicken Wings', 'OFF'], ['4', 'Fried Aubergine', 'ON']]
	select, code = mydialog.checklist(msg = menu, items = MyList)
	print(code)
	print(' '.join(select), '\n')
	select, code = mydialog.inputbox(msg = message, default = default_text, password = False)
	print(code)
	print(select, '\n')
	select, code = mydialog.inputbox(msg = 'Password Input', default = default_text, password = True)
	print(code)
	print(select, '\n')
	code = mydialog.yesno(msg = 'How to yes?', default='yes')
	print(code)
	code = mydialog.textbox(str(pathlib.Path('./test.py').resolve()))
	print(code)
	mydialog.msgbox(msg = message)

if __name__ == '__main__':
	main()
