#!/usr/bin/env bash

blacklist_dir="/etc/blacklist-scripts"
#blacklist_dir="."

py_blacklist_script="${blacklist_dir}/py-blacklist.py"
iptables_tmp="${blacklist_dir}/iptables-tmp.txt"

IPTABLES=iptables

blacklist=""
net_ip=""
net_mask=""
_count=0
_quantity=0
_ignore=0

blacklist=$(python "${py_blacklist_script}" -c 3 -s)
ignorelist=$(python "${py_blacklist_script}" -i -c 1 -s)

_out_fromat=0
_output_file=""
_input_file=""

function start_ban() {
	_old_ignore="${_ignore}"
	_ignore=1
	wait
	for IIP in ${ignorelist[*]}; do
		ban_unban "yes" "${IIP}"
	done
	wait
	_ignore="${_old_ignore}"
	wait
	for IP in ${blacklist[*]}; do
		ban_unban "yes" "${IP}"
	done
}

function stop_ban() {
	_old_ignore="${_ignore}"
	wait
	for IP in ${blacklist[*]}; do
		ban_unban "no" "${IP}"
	done
	wait
	_ignore=1
	wait
	for IIP in ${ignorelist[*]}; do
		ban_unban "no" "${IIP}"
	done
	_ignore="${_old_ignore}"
}

function reload_ban() {
	$IPTABLES -L > "${iptables_tmp}"
	wait
	stop_ban
	wait
	$IPTABLES -L > "${iptables_tmp}"
	wait	
	start_ban
}

function add_del_json(){
	if [[ "${1}" == 'yes' ]]; then
		if [[ "${_ignore}" -eq 0 ]]; then
			python "${py_blacklist_script}" -ip ${2} -n ${3} -q "${4}" -if "${_input_file}" -of "${_output_file}" -a
		else
			python "${py_blacklist_script}" -ip ${2} -i -q "${3}" -if "${_input_file}" -of "${_output_file}" -a
		fi
	else
		if [[ "${_ignore}" -eq 0 ]]; then
			python "${py_blacklist_script}" -ip ${2} -n ${3} -if "${_input_file}" -of "${_output_file}" -d
		else
			python "${py_blacklist_script}" -ip ${2} -i -if "${_input_file}" -of "${_output_file}" -d
		fi
	fi
}

function ip_to_net(){
	_ip=$(ipcalc "${1}" | grep -Ei "Network" | xargs -0 | awk '{print $2}')
	if [[ "${_ip[*]}" != "" ]]; then
		echo "${_ip[*]}"
	else
		_ip=$(ipcalc "${1}" | grep -Ei "Address" | xargs -0 | awk '{print $2}')
		echo "${_ip[*]}"
	fi
}

function question_ban() {
	if [[ $(cat "${iptables_tmp}" | grep -Ei "${1}" | wc -l) -eq 0 ]]; then
		if [[ "${2}" != "" ]]; then
			if [[ $(cat "${iptables_tmp}" | grep -Ei "${2}" | wc -l) -eq 0 ]]; then
				echo "empty"
			else
				echo "no-empty"
			fi
		else
			echo "empty"
		fi
	else
		echo "no-empty"
	fi
}

function ban_unban() {
	_add="${1}"
	_out_ip=$(ip_to_net "${2}")
	if [[ "${_ignore}" -eq 0 ]]; then
		_ip=$(echo "${_out_ip[*]}" | cut -d '/' -f1)
	else
		_ip=$(echo "${2}" | cut -d '/' -f1)
	fi
	_host=$(nslookup ${_ip[*]} | grep -Evi "can't find" | grep -Ei "in-addr.arpa|name" | cut -d '=' -f2 | xargs -0 | sed 's/.$//')
	wait
	if [[ "${_host[*]}" != "" ]]; then
		_host_mask="${_host[*]}"
	else
		_host_mask=""
	fi
	wait
	if [[ "${_add}" == "yes" ]]; then
		if [[ $(question_ban "${_ip[*]}" "${_host_mask[*]}") == "empty" ]]; then
			if [[ "${_ignore}" -eq 0 ]]; then
				$IPTABLES -t filter -A INPUT -s "${_out_ip[*]}" -j DROP
				echo " * Ban ${_out_ip[*]}"
			else
				$IPTABLES -t filter -A INPUT -s "${2}" -j ACCEPT
				echo " * Ignore ${2}"
			fi
		fi
	else
		if [[ $(question_ban "${_ip[*]}" "${_host_mask[*]}") == "no-empty" ]]; then
			if [[ "${_ignore}" -eq 0 ]]; then
				$IPTABLES -t filter -D INPUT -s "${_out_ip[*]}" -j DROP
				echo " * Unban ${_out_ip[*]}"
			else
				$IPTABLES -t filter -D INPUT -s "${2}" -j ACCEPT
				echo " * Delete ignore ${2}"
			fi
		fi
	fi
}

_help() {
	echo -e -n "\nHelp $0"
	echo -e -n "\nThe command is:\n"
	echo -e -n "usage: blacklist-ip.sh [-ipv6] [-start] [-stop] [-nostop] [-reload]\n\t\t\t[-show] [-ignore]\n\t\t\t[-j] [-if input-file] [-of output file]"
	echo -e -n "\n\t\t\t[-c count] [-q quantity]"
	echo -e -n "\n\t\t\t[-ip address ...] [-net mask ...]"
	echo -e -n "\n\t\t\t[-ban] [-unban] [-add] [-del] [-h]"
	echo -e -n "\n\t-ipv6\t\tip6tables.\n"
	echo -e -n "\t-start\t\tLaunching a blacklist and adding network\n\t\t\t addresses to IPTABLES.\n"
	echo -e -n "\t-stop\t\tStopping the blacklist and removing network\n\t\t\t addresses from IPTABLES.\n"
	echo -e -n "\t-nostop\t\tStopping the blacklist and skipping network\n\t\t\t addresses from IPTABLES.\n"
	echo -e -n "\t-reload\t\tReload the blacklist and adding the all network\n\t\t\t addresses to IPTABLES.\n"
	echo -e -n "\t-show\t\tView the blacklist of ip addresses of subnets.\n"
	echo -e -n "\t-ignore\t\tWhitelist IP.\n"
	echo -e -n "\t-j\t\tShow in json format.\n"
	echo -e -n "\t-if\t\tInput file.\n"
	echo -e -n "\t-of\t\tOutput file.\n"
	echo -e -n "\t-c\t\tThe number of bans at which the network \n\t\t\tIP address is added to IPTABLES.\n"
	echo -e -n "\t-q\t\tHow many times the address has been banned.\n"
	echo -e -n "\t-ip\t\tThe IP address to add to the blacklist.\n\t\t\tYou can specify both with and without a mask.\n"
	echo -e -n "\t-net\t\tThe IP address of the network to add to the blacklist.\n\t\t\tYou can specify both with and without a mask.\n"
	echo -e -n "\t-ban\t\tBan the ip address of the network when specifying \n\t\t\ta single ip address (key -ip) or the ip address \n\t\t\tof the network (key -net).\n"
	echo -e -n "\t-unban\t\tUnban the ip address of the network, when specifying \n\t\t\ta single ip address (key -ip) or the ip address \n\t\t\tof the network (key -net).\n"
	echo -e -n "\t-add\t\tAdd an address to the blacklist without being \n\t\t\tbanned in IPTABLES.\n"
	echo -e -n "\t-del\t\tRemove an address from the blacklist without being \n\t\t\tbanned in IPTABLES.\n"
	echo -e -n "\t--h\t\tHelp.\n"
	echo -e -n "\t--help\t\tHelp.\n"
}

while [ -n "$1" ]; do
	case "$1" in
		-c) [[ $2 != "" ]] && _count=${2}
			wait
			blacklist=$(python "${py_blacklist_script}" -c ${_count} -if "${_input_file}" -s)
			shift
			;;
		-q) [[ $2 != "" ]] && _quantity=${2}
			shift
			;;
		-j) _out_fromat=1
			;;
		-if) [[ $2 != "" ]] && _input_file=${2}
			shift
			;;
		-of) [[ $2 != "" ]] && _output_file=${2}
			shift
			;;
		-start) $IPTABLES -L > "${iptables_tmp}"
				wait
				echo "Launching the blacklist ..."
				start_ban
				;;
		-stop)  $IPTABLES -L > "${iptables_tmp}"
				wait
				echo "Stopping the blacklist ..."
				stop_ban
				;;
		-nostop) echo "Stopping the blacklist."
				echo "The following addresses will not be removed from IPTABLES: ${blacklist[*]}"
				;;
		-reload) echo "Updating the blacklist ..."
				reload_ban
				;;
		-show)	if [[ "${_ignore}" -eq 0 ]]; then
					if [[ "${_out_fromat}" -eq 0 ]]; then
						blacklist=$(python "${py_blacklist_script}" -c "${_count}" -if "${_input_file}" -of "${_output_file}" -s)
					else
						blacklist=$(python "${py_blacklist_script}" -c "${_count}" -j -if "${_input_file}" -of "${_output_file}" -s)
					fi
				else
					if [[ "${_out_fromat}" -eq 0 ]]; then
						blacklist=$(python "${py_blacklist_script}" -c "${_count}" -i -if "${_input_file}" -of "${_output_file}" -s)
					else
						blacklist=$(python "${py_blacklist_script}" -c "${_count}" -i -j -if "${_input_file}" -of "${_output_file}" -s)				
					fi
				fi
				wait
				echo "${blacklist[*]}"
				exit 0
				;;
		-ignore) _ignore=1
				;;
		-ip) [[ $2 != "" ]] && net_ip="${2}"
			shift
			;;
		-net) [[ $2 != "" ]] && net_mask="${2}"
			shift
			;;
		-ban) $IPTABLES -L > "${iptables_tmp}"
				wait
				if [[ "${net_ip[*]}" != "" ]]; then 
					if [[ "${net_mask[*]}" != "" ]]; then 
						ban_unban "yes" "${net_ip[*]}/${net_mask[*]}"
					else
						ban_unban "yes" "${net_ip[*]}"
					fi
				fi
				;;
		-unban) $IPTABLES -L > "${iptables_tmp}"
				wait
				if [[ "${net_ip[*]}" != "" ]]; then 
					if [[ "${net_mask[*]}" != "" ]]; then 
						ban_unban "no" "${net_ip[*]}/${net_mask[*]}"
					else
						ban_unban "no" "${net_ip[*]}"
					fi
				fi
				;;
		-add) if [[ "${_ignore}" -eq 0 ]]; then
				[[ "${net_ip[*]}" != "" ]] && [[ "${net_mask[*]}" != "" ]] && add_del_json "yes" "${net_ip[*]}" "${net_mask[*]}" "${_quantity}"
			else
				[[ "${net_ip[*]}" != "" ]] && add_del_json "yes" "${net_ip[*]}" "${_quantity}"
			fi
				;;
		-del) if [[ "${_ignore}" -eq 0 ]]; then
				[[ "${net_ip[*]}" != "" ]] && [[ "${net_mask[*]}" != "" ]] && add_del_json "no" "${net_ip[*]}" "${net_mask[*]}"
			else
				[[ "${net_ip[*]}" != "" ]] && add_del_json "no" "${net_ip[*]}"
			fi
				;;
		-ipv6) IPTABLES=ip6tables
				;;
		-[h?] | --help) _help;;
		*) echo -e -n "\nUnkonwn parameters!\n"
			_help
			;;
	esac
	shift
done

echo "Exit the blacklist ..."

exit 0
