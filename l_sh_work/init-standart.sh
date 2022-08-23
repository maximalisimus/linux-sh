#!/bin/bash
SETCOLOR_SUCCESS="echo -en \\033[1;32m"
SETCOLOR_FAILURE="echo -en \\033[1;31m"
SETCOLOR_NORMAL="echo -en \\033[0;39m"
sms()
{
	case "$1" in
		1) echo -e -n "Process to complete";; 
		2) echo -e -n "Process to failure";;
	esac
}
checkprocess()
{
	errcode=$?
	if [ $errcode -eq 0 ]; then
		$SETCOLOR_SUCCESS
		echo -e -n "\n"
		sms "1"
		echo -e -n "$(tput hpa $(tput cols))$(tput cub 6)[OK]"
		$SETCOLOR_NORMAL
	else
		$SETCOLOR_FAILURE
		echo -e -n "\n"
		sms "2"
		echo -e -n "$(tput hpa $(tput cols))$(tput cub 6)[fail]"
		$SETCOLOR_NORMAL
	fi
}
ABSOLUT_FILENAME=`readlink -e "$0"`
filesdir=`dirname "$ABSOLUT_FILENAME"`
internet="$filesdir//conf/network.sh"
Xorg --version 1>/dev/null 2>/dev/null
_err=$?
if [[ $_err == "1" ]]; then
	Xdialog --version 1>/dev/null 2>/dev/null
	_error=$?
	if [[ $_error == "0" ]]; then
		DIALOG=Xdialog
	else
		DIALOG=dalog
	fi
else
	DIALOG=dalog
fi
unset _err
unset _error
clear

