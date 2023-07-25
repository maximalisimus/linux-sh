DESTDIR=./
POSTDIR=etc
INSTALLDIR=/
TARGET=blacklist-scripts
SCRIPT=py-blacklist.py
SYMLINK=blacklist
SETUPDIR=$(DESTDIR)$(POSTDIR)/$(TARGET)
EXEC=$(INSTALLDIR)$(POSTDIR)/$(TARGET)/$(SCRIPT)
SETUPEXEC=$(DESTDIR)usr/bin/$(SYMLINK)
SOURCES=f2b
F2BSETUP=$(DESTDIR)etc/fail2ban
# action.d
action_dir=$(SOURCES)/action.d/*.conf
action_files=$(notdir $(wildcard $(action_dir)))
# filter.d
filter_dir=$(SOURCES)/filter.d/*.conf
filter_files=$(notdir $(wildcard $(filter_dir)))
# jail.d
jail_dir=$(SOURCES)/jail.d/*.conf
jail_files=$(notdir $(wildcard $(jail_dir)))
#
DESCENG="The Fail2Ban black and white list in Python."
DESCRU="Черный и белый список Fail2Ban в Python."
#
.PHONY: all install install-action install-filter install-jail uninstall uninstall-all uninstall-action uninstall-filter uninstall-jail clear
all: install install-all
	echo "Installation complete!"

install:
	rm -rf $(SETUPDIR)
	mkdir -p $(SETUPDIR) $(DESTDIR)usr/bin/
	install -Dm 755 $(SCRIPT) $(SETUPDIR)/
	ln -s $(EXEC) $(SETUPEXEC) 2>/dev/null
	chmod +x $(DESTDIR)$(POSTDIR)/$(TARGET)/$(SCRIPT) 2>/dev/null

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
	for i in $(action_files) ; do \
		rm -rf $(F2BSETUP)/action.d/$$i ; \
	done

uninstall-filter:
	for i in $(filter_files) ; do \
		rm -rf $(F2BSETUP)/filter.d/$$i ; \
	done

uninstall-jail:
	for i in $(jail_files) ; do \
		rm -rf $(F2BSETUP)/jail.d/$$i ; \
	done

uninstall-all: uninstall-action uninstall-filter uninstall-jail
	echo "Uninstall fail2ban modules complete!"

clear: uninstall uninstall-all
	echo "Uninstal complete!"
