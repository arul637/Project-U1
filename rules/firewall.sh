#! /bin/bash

echo "hello firewall start now..."

sudo iptables -t mangle --flush

sudo iptables -t mangle --policy INPUT DROP
sudo iptables -t mangle --policy FORWARD DROP

sudo iptables -t mangle -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -t mangle -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT


# sudo iptables -t mangle -A INPUT -i lo -j ACCEPT
# sudo iptables -t mangle -A OUPUT -i lo -j ACCEPT

# sudo iptables -t mangle -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
# sudo iptables -t mangle -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

sudo iptables -t mangle --policy OUTPUT ACCEPT
sudo iptables -t mangle -A OUTPUT -m conntrack --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
