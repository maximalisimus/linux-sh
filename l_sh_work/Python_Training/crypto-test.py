#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Linux:
# pip install pycryptodome
# Windows
# pip install pycryptodomex

from Crypto.PublicKey import RSA
import pathlib
import os
import sys

def writeKey(filePath, data):
	with open(str(pathlib.Path(filePath)), "wb") as f:
		f.write(data)

def readKey(fName):
	with open(str(pathlib.Path(fName)), "rb") as f:
		data = f.read()
	return data

def main():
	passphrases = 'pass'
	#key = RSA.generate(4096)
	 
	#encrypted_key = key.exportKey(
	#	format='PEM',
	#	passphrase=passphrases, 
	#	pkcs=8, 
	#	protection="scryptAndAES128-CBC"
	#)
	#writeKey('./private-key.gpg',encrypted_key)
	#writeKey('./public-key.gpg',key.publickey().exportKey())
	private_files = readKey('./private-key.gpg')
	public_files = readKey('./public-key.gpg')
	pubkey = RSA.import_key(public_files)
	privkey = RSA.import_key(private_files, passphrase=passphrases)
	print(pubkey.public_key())
	print(privkey.public_key())
	print(pubkey.publickey().exportKey().decode("utf-8"))
	print(privkey.publickey().exportKey().decode("utf-8"))

if __name__ == '__main__':
	main()
