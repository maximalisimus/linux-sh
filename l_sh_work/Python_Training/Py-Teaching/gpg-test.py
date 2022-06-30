#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import stat
import os
import gnupg

gpg_dir = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("gpgdir"))

def getRealPath(pathname):
	return str(pathlib.Path(pathname).resolve())

def rmFullDir(path: str):
	# import os
	if pathlib.Path(path).exists():
		for root, dirs, files in os.walk(path, topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))
		pathlib.Path(path).rmdir()	

def createGPG(gpg):
	input_data = gpg.gen_key_input(key_type="RSA", key_length=4096, 
									name_real="Fred Bloggs", name_comment="A test user", 
									name_email="fred.bloggs@domain.com", 
									passphrase="12345")
	# expire_date = “2009-12-31”, “365d”, “3m”, “6w”, “5y”
	key = gpg.gen_key(input_data)
	return key

def main():
	if not pathlib.Path(gpg_dir).exists():
		pathlib.Path(gpg_dir).mkdir(parents=True, exist_ok=True)
		# pathlib.Path(gpg_dir).chmod(0o700)
		pathlib.Path(gpg_dir).chmod(stat.S_IRWXU) # import stat
	# rmFullDir(gpg_dir)
	gpg = gnupg.GPG(gnupghome=gpg_dir, use_agent=True)
	#mykey = createGPG(gpg)
	'''
	fingerprint = "4D53DB3B25A0B26E6BD0BB0662774BAE11FE3D98"
	public_key = gpg.export_keys(keyids=fingerprint, secret=False) # mykey.fingerprint
	private_key = gpg.export_keys(keyids=fingerprint, secret=True, passphrase="12345") # mykey.fingerprints
	gpgfile = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("mykeyfile.gpg"))
	with open(gpgfile, 'w') as f:
		f.write(public_key)
		f.write(private_key)
	'''
	'''
	public_key = gpg.list_keys()
	if len(public_key) > 1:
		for keys in public_key:
			print(keys['fingerprint'])
	else:
		print(public_key[0]['fingerprint'])
	private_key = gpg.list_keys(secret=True)
	if len(private_key) > 1:
		for keys in private_key:
			print(keys['fingerprint'])
	else:
		print(private_key[0]['fingerprint'])
	'''

if __name__ == '__main__':
	main()
