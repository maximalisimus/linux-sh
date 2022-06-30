#!/usr/bin/env python
# by Seth Kenlon
# GPLv3
 
# install deps:
# python3 -m pip install --user python-gnupg getpass4
 
import gnupg
import getpass
from pathlib import Path
 
def get_api_pass():
	homedir = str(Path.home())
	gpg = gnupg.GPG(gnupghome=os.path.join(homedir,".gnupg"), use_agent=True)
	passwd = getpass.getpass(prompt="Enter your GnuPG password: ", stream=None)
	with open(os.path.join(homedir,'.mutt','pass.gpg'), 'rb') as f:
		apipass = (gpg.decrypt_file(f, passphrase=passwd))
	f.close()
	return str(apipass)
   
if __name__ == "__main__":
	apipass = get_api_pass()
	print(apipass)
