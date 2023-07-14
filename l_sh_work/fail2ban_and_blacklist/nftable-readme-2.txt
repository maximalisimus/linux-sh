

sudo iptables -N blacklist
sudo iptables -A blacklist -j RETURN
sudo iptables -I INPUT -j blacklist

sudo iptables -D INPUT -j blacklist

# clear
sudo iptables -F blacklist

# Delete chain
sudo iptables -X blacklist

sudo iptables -n -L INPUT | grep -q 'blacklist[ \t]'

sudo iptables -I blacklist 1 -s 192.168.0.107 -j DROP
sudo iptables -D blacklist -s 192.168.0.107 -j DROP

sudo iptables -I blacklist 1 -s 192.168.0.107 -j ACCEPT
sudo iptables -D blacklist -s 192.168.0.107 -j ACCEPT





sudo nft add table inet blacklist
sudo nft list table inet blacklist

sudo nft delete table inet blacklist

sudo nft flush table inet blacklist
#sudo nft add chain inet blacklist INPUT
sudo nft add chain inet blacklist INPUT '{ type filter hook input priority 0; policy accept; }'

sudo nft delete chain inet blacklist INPUT

sudo nft flush chain inet blacklist INPUT

sudo nft 'add rule inet blacklist INPUT ip saddr 192.168.0.107 counter drop'

sudo nft --handle --numeric list chain inet blacklist INPUT | grep -Ei 'ip saddr|# handle' | sed 's/^[ \t]*//' | awk '!/^$/{print $0}'

sudo nft delete rule inet blacklist INPUT handle 3










