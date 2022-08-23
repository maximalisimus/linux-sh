#!/bin/bash
ANSWER="./.answer"
HIGHLIGHT=0
SUB_MENU=""
HIGHLIGHT_SUB=0
if [ -d /usr/share/xsessions/ ]; then
	# _xsession=$(ls /usr/share/xsessions/ | sed 's/.desktop//g' | tr '[:upper:]' '[:lower:]' | wc -l)
	_xsession=$(find /usr/share/xsessions/ -type f | sed 's/.desktop//g' | tr '[:upper:]' '[:lower:]' | wc -l)
	if [[ "${_xsession}" -ge 1 ]]; then
		DIALOG=Xdialog
	else
		DIALOG=dialog
	fi
else
	DIALOG=dialog
fi
# DIALOG=dialog
# DIALOG=Xdialog
sub_menu_1()
{
	if [[ $SUB_MENU != "sub_menu_1" ]]; then
		SUB_MENU="sub_menu_1"
		HIGHLIGHT_SUB=1
	else
		if [[ $HIGHLIGHT_SUB != 3 ]]; then
			HIGHLIGHT_SUB=$(( HIGHLIGHT_SUB + 1 ))
		fi
	fi
	$DIALOG --default-item ${HIGHLIGHT_SUB} --backtitle "VERSION - SYSTEM (ARCHI)" --title "Sub menu title" --menu "Sub menu body" -1 -1 3 \
	"1" "Menu Name 1" \
	"2" "Menu Name 2" \
	"3" "Back" 2>${ANSWER}
	
	HIGHLIGHT_SUB=$(cat ${ANSWER})
	case $(cat ${ANSWER}) in
		"1") clear
			echo "Sub menu 1, Menu Name 1"
			sleep 3
			wait
			;;
		"2") clear
			echo "Sub menu 2, Menu Name 2"
			sleep 3
			wait
			;;     
		*) main_menu_online
			;;
	esac
    
    sub_menu_1
	
}
sub_menu_2()
{
	if [[ $SUB_MENU != "sub_menu_2" ]]; then
		SUB_MENU="sub_menu_2"
		HIGHLIGHT_SUB=1
	else
		if [[ $HIGHLIGHT_SUB != 3 ]]; then
			HIGHLIGHT_SUB=$(( HIGHLIGHT_SUB + 1 ))
		fi
	fi
	$DIALOG --default-item ${HIGHLIGHT_SUB} --backtitle "VERSION - SYSTEM (ARCHI)" --title "Sub menu title 2" --menu "Sub menu body 2" -1 -1 3 \
	"1" "Menu Sub Name 1" \
	"2" "Menu Sub Name 2" \
	"3" "Back" 2>${ANSWER}
	
	HIGHLIGHT_SUB=$(cat ${ANSWER})
	case $(cat ${ANSWER}) in
		"1") clear
			echo "Sub menu 1, Menu Sub Name 1"
			sleep 3
			wait
			;;
		"2") clear
			echo "Sub menu 2, Menu Sub Name 2"
			sleep 3
			wait
			;;     
		*) main_menu_online
			;;
	esac
    
    sub_menu_2
	
}
main_menu_online() {

	if [[ $HIGHLIGHT != 3 ]]; then
		HIGHLIGHT=$(( HIGHLIGHT + 1 ))
	fi
	
	$DIALOG --default-item ${HIGHLIGHT} --backtitle "VERSION - SYSTEM (ARCHI)" --title "Title base menu" \
	--menu "Body base menu" -1 -1 3 \
	"1" "1 sub Menu" \
	"2" "2 sub Menu" \
	"3" "Exit" 2>${ANSWER}
	HIGHLIGHT=$(cat ${ANSWER})
	case $(cat ${ANSWER}) in
		"1") sub_menu_1 ;;
		"2") sub_menu_2 ;;
		*) clear
			rm -rf "${ANSWER}"
			exit 0 ;;
	esac
	main_menu_online
}
main_menu_online
exit 0
