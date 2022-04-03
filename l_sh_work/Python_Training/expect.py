#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect
import pathlib

def main():
	# Init str and command
	mypass = "pass"
	# Auto password confirmation, otherwise the process will hang.
	pass_enter = "\n"
	# The resulting string with the password and confirmation of the input.
	pass_rez = mypass + pass_enter
	# The command to add the key to the ssh agent.
	command = "ssh-add"
	# The waiting phrase before entering the password for the id_rsa key.
	phrases = "Enter passphrase for"
	# Specifying the key and verifying the existence of a file with this private key id_rsa.
	key_file = pathlib.Path("./id_rsa").resolve()
	# The resulting wait string for the key with the full path.
	str_waits = phrases + " " + str(key_file)
	if key_file.is_file():
		# The resulting command.
		cmd = command + " " + str(key_file)
		# Executing "pexpect".
		output = pexpect.run(cmd, events={str_waits:pass_rez})
		# Output of the result of executing all commands to the console.
		print(output.decode("utf-8"))

if __name__ == '__main__':
	main()
