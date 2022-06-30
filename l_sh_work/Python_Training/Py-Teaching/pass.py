#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import getpass
import keyring

# Объявляем дефолтные переменные
systemname = 'MyDBPass'
username = 'mikl'

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", "--newpass", required=False, help="Set new password", action="store_true")
	parser.add_argument("-d", "--delpass", required=False, help="Del the password", action="store_true")
	arguments = parser.parse_args()
	return arguments

def fake_db_connection():
	passwd = keyring.get_password(systemname, username)
	print('Using very secret password from vault: {}'.format(passwd))
	print('Task completed')

def main():
	args = parse_arguments()
	# Записываем в хранилище пароль, если активирован параметр --newpass
	if args.newpass:
		# Безопасно запрашиваем ввод пароля в CLI
		password = getpass.getpass(prompt="Enter secret password:")

		# Пишем полученный пароль в хранилище ключей
		try:
			keyring.set_password(systemname, username, password)
		except Exception as error:
			print('Error: {}'.format(error))
	if args.delpass:
		passwd = keyring.delete_password(systemname, username)
		print('Delete secret password from vault: {}'.format(passwd))
	# Подключаемся к базе с помощью пароля из системного хранилища
	fake_db_connection()

if __name__ == '__main__':
	main()
