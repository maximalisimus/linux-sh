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
.PHONY: all install install-action install-filter install-jail uninstall uninstall-all uninstall-action uninstall-filter uninstall-jail clear
all: install install-all
	echo "Installation complete!"

install:
	rm -rf $(SETUPDIR)/
	mkdir -p $(SETUPDIR)/ $(DESTDIR)usr/bin/
	install -Dm 755 $(SCRIPT) $(SETUPDIR)/
	ln -s $(EXEC) $(SETUPEXEC) 2>/dev/null
	chmod +x $(EXEC)

install-action:
	install -dDm 755 $(F2BSETUP)/action.d/
	install -Dm 755 $(SOURCES)/action.d/*.conf $(F2BSETUP)/action.d/

install-filter:
	install -dDm 755 $(F2BSETUP)/filter.d/
	install -Dm 755 $(SOURCES)/filter.d/*.conf $(F2BSETUP)/filter.d/

install-jail:
	install -dDm 755 $(F2BSETUP)/jail.d/
	install -Dm 755 $(SOURCES)/jail.d/*.conf $(F2BSETUP)/jail.d/

install-all: install-action install-filter install-jail
	echo "Installation fail2ban modules complete!"

uninstall:
	rm -rf $(SETUPDIR)
	rm -rf $(SETUPEXEC)

uninstall-action:
	rm -rf $(F2BSETUP)/action.d/$(blackfull) $(F2BSETUP)/action.d/$(blacksimple)

uninstall-filter:
	rm -rf $(F2BSETUP)/filter.d/$(nginx_access) $(F2BSETUP)/filter.d/$(nginx_error)

uninstall-jail:
	rm -rf $(F2BSETUP)/jail.d/$(access_nginx) $(F2BSETUP)/jail.d/$(error_nginx)
	rm -rf $(F2BSETUP)/jail.d/$(nginx_ddos) $(F2BSETUP)/jail.d/$(ssh)

uninstall-all: uninstall-action uninstall-filter uninstall-jail
	echo "Uninstall fail2ban modules complete!"

clear: uninstall uninstall-all
	echo "Uninstal complete!"
