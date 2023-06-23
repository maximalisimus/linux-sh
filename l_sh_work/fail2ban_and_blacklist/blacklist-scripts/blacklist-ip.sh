#!/usr/bin/env bash

blacklist_dir="/etc/blacklist-scripts"
#blacklist_dir="."

source "${blacklist_dir}/blacklist_env"

iptables_tmp="${blacklist_dir}/iptables-tmp.txt"

$IPTABLES -L > "${iptables_tmp}"

blacklist=""
net_ip=""
_count=3

blacklist=$(python "${blacklist_dir}"/read-blacklist.py ${_count})

function start_ban() {
	for IP in ${blacklist[*]}; do
		_ip=$(echo "${IP[*]}" | cut -d '/' -f1)
		_host=$(nslookup ${_ip[*]} | grep -Ei "in-addr.arpa|name" | cut -d '=' -f2 | xargs -0 | sed 's/.$//')
		_mask=$(echo "${IP[*]}" | cut -d '/' -f2)
		_host_mask="${_host[*]}/${_mask[*]}"
		if [[ $(cat "${iptables_tmp}" | grep -Ei "${IP[*]}" | wc -l) -eq 0 ]]; then
			if [[ $(cat "${iptables_tmp}" | grep -Ei "${_host_mask[*]}" | wc -l) -eq 0 ]]; then
				$IPTABLES -t filter -A INPUT -s "${IP[*]}" -j DROP
				echo " * ban ${IP[*]}"
			fi
		fi
	done
}

function stop_ban() {
	for IP in ${blacklist[*]}; do
		ip=$(echo "${IP[*]}" | cut -d '/' -f1)
		_host=$(nslookup ${_ip[*]} | grep -Ei "in-addr.arpa|name" | cut -d '=' -f2 | xargs -0 | sed 's/.$//')
		_mask=$(echo "${IP[*]}" | cut -d '/' -f2)
		_host_mask="${_host[*]}/${_mask[*]}"
		$IPTABLES -t filter -D INPUT -s "${IP[*]}" -j DROP
		$IPTABLES -t filter -D INPUT -s "${_host_mask[*]}" -j DROP
		echo " * unban ${IP[*]}"
	done
}

function banied() {
	$IPTABLES -t filter -A INPUT -s "${1}" -j DROP
	wait
	python "${blacklist_dir}"/add-blacklist.py "${1}"
	wait
	echo " * ban ${1}"
}

function unbanied() {
	$IPTABLES -t filter -D INPUT -s "${1}" -j DROP
	wait
	python "${blacklist_dir}"/del-blacklist.py "${1}"
	wait
	echo " * unban ${1}"
}

_help() {
	echo -e -n "\nHelp $0"
	echo -e -n "\nThe command is:\n"
	echo -e -n "\t-start\t\tLaunching a blacklist and adding network\n\t\t\t addresses to IPTABLES.\n"
	echo -e -n "\t-stop\t\tStopping the blacklist and removing network\n\t\t\t addresses from IPTABLES.\n"
	echo -e -n "\t-nostop\t\tStopping the blacklist and skipping network\n\t\t\t addresses from IPTABLES.\n"
	echo -e -n "\t-update\t\tUpdating the blacklist and adding new network\n\t\t\t addresses to IPTABLES.\n"
	echo -e -n "\t-show\t\tView the blacklist of ip addresses of subnets.\n"
	echo -e -n "\t-c\t\tThe number of bans at which the network \n\t\t\tIP address is added to IPTABLES.\n"
	echo -e -n "\t-ip\t\tThe IP address to add to the blacklist.\n\t\t\tYou can specify both with and without a mask.\n"
	echo -e -n "\t-net\t\tThe IP address of the network to add to the blacklist.\n\t\t\tYou can specify both with and without a mask.\n"
	echo -e -n "\t-ban\t\tBan the ip address of the network when specifying \n\t\t\ta single ip address (key -ip) or the ip address \n\t\t\tof the network (key -net).\n"
	echo -e -n "\t-unban\t\tUnban the ip address of the network, when specifying \n\t\t\ta single ip address (key -ip) or the ip address \n\t\t\tof the network (key -net).\n"
	echo -e -n "\t--h\t\tHelp.\n"
	echo -e -n "\t--help\t\tHelp.\n"
}

function ip_to_net(){
	_ip="${1}"
	_net=$(ipcalc "${_ip[*]}" | grep -Ei "Network" | xargs | cut -d ' ' -f 2)
	unset _ip
	echo "${_net[*]}"
}

while [ -n "$1" ]; do
	case "$1" in
		-c) [[ $2 != "" ]] && _count=${2}
			wait
			blacklist=$(python "${blacklist_dir}"/read-blacklist.py ${_count})
			shift
			;;
		-start) echo "Launching the blacklist ..."
				start_ban
				;;
		-stop) echo "Stopping the blacklist ..."
				stop_ban
				;;
		-nostop) echo "Stopping the blacklist."
				echo "The following addresses will not be removed from IPTABLES: ${blacklist[*]}"
				;;
		-update) echo "Updating the blacklist ..." 
				start_ban
				;;
		-show)	blacklist=$(python "${blacklist_dir}"/read-blacklist.py)
				wait
				echo "${blacklist[*]}"
				exit 0
				;;
		-ip) [[ $2 != "" ]] && net_ip=$(ip_to_net "${2}")
			shift
			;;
		-net) [[ $2 != "" ]] && net_ip="${2}"
			shift
			;;
		-ban) [[ "${net_ip[*]}" != "" ]] && banied "${net_ip[*]}"
				;;
		-unban) [[ "${net_ip[*]}" != "" ]] && unbanied "${net_ip[*]}"
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
