

sudo iptables -N blackwhite
sudo iptables -A blackwhite -j RETURN
sudo iptables -I INPUT -j blackwhite

sudo iptables -D INPUT -j blackwhite

# clear
sudo iptables -F blackwhite

# Delete chain
sudo iptables -X blackwhite

sudo iptables -n -L INPUT | grep -q 'blackwhite[ \t]'

sudo iptables -I blackwhite 1 -s 192.168.0.107 -j DROP
sudo iptables -D blackwhite -s 192.168.0.107 -j DROP

sudo iptables -I blackwhite 1 -s 192.168.0.107 -j ACCEPT
sudo iptables -D blackwhite -s 192.168.0.107 -j ACCEPT





sudo nft delete table inet blackwhite
sudo nft flush table inet blackwhite
sudo nft delete chain inet blackwhite INPUT
sudo nft flush chain inet blackwhite INPUT


sudo nft add table inet blackwhite
sudo nft list table inet blackwhite

#sudo nft add chain inet blackwhite INPUT
sudo nft add chain inet blackwhite INPUT '{ type filter hook input priority 0; policy accept; }'

sudo nft 'add rule inet blackwhite INPUT ip saddr 192.168.0.107 counter drop'

sudo nft --handle --numeric list chain inet blackwhite INPUT | grep -Ei 'ip saddr|# handle' | sed 's/^[ \t]*//' | awk '!/^$/{print $0}'

sudo nft delete rule inet blackwhite INPUT handle 3










