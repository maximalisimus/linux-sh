DESTDIR=./
TARGET=blacklist-scripts
SCRIPT=py-blacklist.py
SYMLINK=blacklist
SETUPDIR=$(DESTDIR)etc/$(TARGET)
EXEC=$(SETUPDIR)/$(SCRIPT)
SETUPEXEC=$(DESTDIR)usr/bin/$(SYMLINK)
SOURCES=f2b
F2BSETUP=$(DESTDIR)etc/fail2ban
# action.d
blackfull=blackfull.conf
blacksimple=blacksimple.conf
# filter.d
nginx_access=nginx-access.conf
nginx_error=nginx-error.conf
# jail.d
access_nginx=access-nginx.conf
error_nginx=error-nginx.conf
nginx_ddos=nginx-ddos.conf
ssh=ssh.conf
#
DESCENG="The Fail2Ban black and white list in Python."
DESCRU="Черный и белый список Fail2Ban в Python."
#
.PHONY: all install install-f2b uninstall uninstall-f2b clear
all: install install-f2b
	echo ""
	echo "Installation complete!"
	echo ""

install:
	rm -rf $(SETUPDIR)/
	mkdir -p $(SETUPDIR)/ $(DESTDIR)usr/bin/
	install -Dm 755 $(SCRIPT) $(SETUPDIR)/
	ln -s $(EXEC) $(SETUPEXEC) 2>/dev/null
	chmod +x $(EXEC)

install-f2b:
	install -dDm 755 $(F2BSETUP)/action.d/ $(F2BSETUP)/filter.d/ $(F2BSETUP)/jail.d/
	install -Dm 755 $(SOURCES)/action.d/*.conf $(F2BSETUP)/action.d/
	install -Dm 755 $(SOURCES)/filter.d/*.conf $(F2BSETUP)/filter.d/
	install -Dm 755 $(SOURCES)/jail.d/*.conf $(F2BSETUP)/jail.d/

uninstall:
	rm -rf $(SETUPDIR)
	rm -rf $(SETUPEXEC)

uninstall-f2b:
	rm -rf $(SETUPDIR) $(F2BSETUP)/action.d/$(blackfull) $(F2BSETUP)/action.d/$(blacksimple) 
	rm -rf $(F2BSETUP)/filter.d/$(nginx_access) $(F2BSETUP)/filter.d/$(nginx_error) 
	rm -rf $(F2BSETUP)/jail.d/$(access_nginx) $(F2BSETUP)/jail.d/$(error_nginx) 
	rm -rf $(F2BSETUP)/jail.d/$(nginx_ddos) $(F2BSETUP)/jail.d/$(ssh)

clear: uninstall uninstall-f2b
	echo ""
	echo "Uninstal complete!"
	echo ""
