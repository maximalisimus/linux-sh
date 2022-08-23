#!/bin/bash
### Translit Full Menu ###
_sh_dev_title="����� ����������"
_sh_dev_body="\n����������, �������� ����������� ����������\n"
_rsvd_nfo1="���������� "
_rsvd_nfo2=" �������� "
_rsvd_nfo3="����������������� ����� ������� � ���������:"
_reserved_info_title="������������� ����� ��� �����������������"
_rsrvd_menu_title="��������� �������� �������"
_rsrvd_menu_body="\n��������� ���������� �������� �������. ��������� tmpfs ��� SSD �����������\n"
_rsrvd_menu1="���������� � ����������������� ������"
_rsrvd_menu2="��������� ������������������ ������"
_rsrvd_menu3="���������� � ����� tmp � FSTAB"
_rsrvd_menu4="��������� tmpfs"
_yesno_tmpfs_body="\n������� ��������� ����� tmp ��� SSD �����������?\n"
_input_reserved_title="���� ������ ������������������ ������������"
_input_reserved_body="\n����������, ������� �������� ����� ������������������ ������������ ������� � ��������� �� 1 �� 10%\n"
_info_tmpfs_title="���������� � tmpfs"
_info_tmpfs_bd1="������ ����� ������� ������ SSD ����������."
_info_tmpfs_bd2="������������ ����� tmp � ����������� ������."
_info_tmpfs_bd3="����� ������� �������� ����� ����� � �������� �� 1 �� 10 ��"
_info_tmpfs_bd4="�� ����� ������ ����������� ������."
_info_tmpfs_bd5="��������: 1G"
_info_tmpfs_body="\n$_info_tmpfs_bd1\n$_info_tmpfs_bd2\n$_info_tmpfs_bd3\n$_info_tmpfs_bd4\n$_info_tmpfs_bd5\n"
_input_size_tmpfs_title="���� ������ ����� tmp"
_input_size_tmpfs_body="\n���������� ������� �������� �����. ��������: 1G\n"
### Translit Full Menu ###
declare -a _devices
declare -a _device_menu
DEVICES=""
_isreserved=""
_rsrvd_file="./rsrvd.nfo"
_tmp_fstab="./tmp.fstab"
_once_shwram=0
### Delete Variables ###
_mem_file="./mem.conf"
_free_info="�������� ����������� ������ ����������"
VERSION=$(uname -r)
SYSTEM=$(uname -s)
ARCHI=$(uname -m)
MOUNTPOINT="/"
ANSWER="./.asf"
_freefile=""
### Delete Variables ###
select_mountpoint()
{
    devices_list=$(lsblk -l | sed '/SWAP/d' | grep -Ei "$1" | awk 'BEGIN{OFS=" "} {print $1,$4}')
    dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_sh_dev_title" --menu "$_sh_dev_body" 0 0 4 ${devices_list} 2>${ANSWER}
    DEVICES=$(cat ${ANSWER})
}
### Delete Function ###
show_memory()
{
	echo -e -n "\n" > $_mem_file
	count=0
	for letter in "${_freefile[@]}"; do
		if [ "$count" -le 5 ]; then
			echo -e -n "\t$letter" >> $_mem_file
		elif [ "$count" -eq 6 ]; then
			echo -e -n "\n$letter" >> $_mem_file
		elif [ "$count" -eq 10 ]; then
			echo -e -n "\t  $letter" >> $_mem_file
		elif [ "$count" -eq 11 ]; then
			echo -e -n "\t     $letter" >> $_mem_file
		elif [ "$count" -eq 12 ]; then
			echo -e -n "\t    $letter" >> $_mem_file
		elif [ "$count" -le 12 ]; then
			echo -e -n "\t$letter" >> $_mem_file
		elif [ "$count" -eq 13 ]; then
			echo -e -n "\t\n$letter" >> $_mem_file
		elif [ "$count" -le 19 ]; then
			echo -e -n "\t$letter" >> $_mem_file
		fi
		let count+=1
	done
}
### Delete Function ###
showmemory()
{
	if [[ $_once_shwram == "0" ]]; then
		rm -rf ${_mem_file}
		_freefile=( $(free -h) )
		IFS=$' '
		show_memory
		_once_shwram=1
	fi
	dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_free_info" --textbox ${_mem_file} 15 100
	clear
}
function reserved_block()
{
	_block_count=$(tune2fs -l $1 | grep -Ei "^(Block count:)" | sed 's/Block count://' | tr -d ' ')
	_reserved_block_count=$(tune2fs -l $1 | grep -Ei "^(Reserved block count:)" | sed 's/Reserved block count://' | tr -d ' ')
	bc=${_block_count[*]}
	unset _block_count
	rbc=${_reserved_block_count[*]}
	unset _reserved_block_count
	_reserv_procent=$(awk 'BEGIN{print ('"$rbc"'*100/'"$bc"')}' | sed 's/\./,/')
	unset bc
	unset rbc
	# round
	_rnd_reserv_procent=$(printf "%.0f" $_reserv_procent)
	unset _reserv_procent
	echo "${_rnd_reserv_procent[*]}"
}
show_block_info()
{
	deviceslist=$(lsblk -l | sed '/SWAP/d' | grep -Ei "${MOUNTPOINT}" | awk '{print $1}')
	echo "" > ${_rsrvd_file}
	for i in ${deviceslist[*]}; do
		devicessize=$(lsblk -l | sed '/SWAP/d' | grep -Ei "$i" | awk '{print $4}')
		_reserved_size=$(reserved_block "/dev/$i")
		echo -e -n "\n$_rsvd_nfo1 $i $_rsvd_nfo2 ${devicessize[*]} \n" >> ${_rsrvd_file}
		echo -e -n "$_rsvd_nfo3 $_reserved_size\n" >> ${_rsrvd_file}
	done
	dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_reserved_info_title" --textbox ${_rsrvd_file} 0 0
	clear
}
input_reserved_percentage()
{
	dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_input_reserved_title" --inputbox "$_input_reserved_body" 0 0 "" 2>${ANSWER}
	qst=$?
	case $qst in
		0) _isreserved=$(cat ${ANSWER})
			;;
	esac
}
### Delete Function ###
check_for_error() {

 if [[ $? -eq 1 ]] && [[ $(cat /tmp/.errlog | grep -i "error") != "" ]]; then
    dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_ErrTitle" --msgbox "$(cat /tmp/.errlog)" 0 0
    echo "" > /tmp/.errlog
    rsrvd_menu
 fi
}
### Delete Function ###
fine_rsrvd_menu()
{
	### Delete Variables ###
	rm -rf /tmp/.errlog
	### Delete Variables ###
	rm -rf ${_rsrvd_file}
	rm -rf ${_mem_file}
	rm -rf ${_tmp_fstab}
	unset IFS
	unset freefile
}
rsrvd_menu()
{
	if [[ $SUB_MENU != "rsrvd_menu" ]]; then
	   SUB_MENU="rsrvd_menu"
	   HIGHLIGHT_SUB=1
	else
	   if [[ $HIGHLIGHT_SUB != 5 ]]; then
	      HIGHLIGHT_SUB=$(( HIGHLIGHT_SUB + 1 ))
	   fi
	fi
	dialog --default-item ${HIGHLIGHT_SUB} --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_rsrvd_menu_title" --menu "$_rsrvd_menu_body" 0 0 5 \
 	"1" "$_rsrvd_menu1" \
	"2" "$_rsrvd_menu2" \
	"3" "$_rsrvd_menu3" \
	"4" "$_rsrvd_menu4" \
	"5" "_Back" 2>${ANSWER} # $_Back
	
	HIGHLIGHT_SUB=$(cat ${ANSWER})
    case $(cat ${ANSWER}) in
    "1") show_block_info
		clear
         ;;
    "2") clear
		select_mountpoint "${MOUNTPOINT}"
		input_reserved_percentage
		if [[ ${_isreserved[*]} -le 10 ]]; then
			if [[ ${_isreserved[*]} -ge 1 ]]; then
				sudo tune2fs -m ${_isreserved[*]} /dev/$DEVICES 2>/tmp/.errlog
				clear
			else echo "Error size paramter at 1 to 10" > /tmp/.errlog
			fi
		else echo "Error size paramter at 1 to 10" > /tmp/.errlog
		fi
         ;;		
	"3") cat /etc/fstab | grep -i "tmpfs" > ${_tmp_fstab}
		dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_rsrvd_menu3" --textbox ${_tmp_fstab} 0 0
		;;
	"4") clear
		dialog --defaultno --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_rsrvd_menu3" --yesno "$_yesno_tmpfs_body" 0 0
		if [[ $? -eq 0 ]]; then
			dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_info_tmpfs_title" --msgbox "$_info_tmpfs_body" 0 0
			showmemory
			dialog --backtitle "$VERSION - $SYSTEM ($ARCHI)" --title "$_input_size_tmpfs_title" --inputbox "$_input_size_tmpfs_body" 0 0 "" 2>${ANSWER}
			qst=$?
			case $qst in
				0) _size_tmpfs=$(cat ${ANSWER})
					# ${MOUNTPOINT}
					sudo sed -i '/tmpfs/d' /etc/fstab 2>/tmp/.errlog
					echo "tmpfs   /tmp         tmpfs   nodev,nosuid,size=${_size_tmpfs[*]}          0  0" >> /etc/fstab 2>/tmp/.errlog
				;;
			esac
		fi
		clear
		;;
      *) # Back to NAME Menu
		fine_rsrvd_menu
		clear
			exit 0
         ;;
    esac
	check_for_error
    rsrvd_menu
}
rsrvd_menu
rm -rf ${ANSWER}
exit 0
