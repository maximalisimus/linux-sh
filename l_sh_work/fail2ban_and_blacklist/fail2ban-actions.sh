#!/bin/bash

# https://bulkin.me/notes/4767

#sudo touch /etc/fail2ban/ip.blacklist
#sudo nano /etc/fail2ban/action.d/iptables-multiport.conf
#sudo nano /etc/fail2ban/action.d/firewallcmd-multiport.conf

#actionban = iptables -I fail2ban-<name> 1 -s <ip> -j DROP
#            echo <ip> >> /etc/fail2ban/ip.blacklist

#actionstart = iptables -N fail2ban-<name>
#              iptables -A fail2ban-<name> -j RETURN
#              iptables -I INPUT -p <protocol> -m multiport --dports <port> -j fail2ban-<name>
#              cat /etc/fail2ban/ip.blacklist | while read IP; do iptables -I fail2ban-<name> 1 -s $IP -j DROP; done

#service fail2ban restart



