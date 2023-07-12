#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ip_no_mask(in_ip) -> str:
	''' Convert an ip address to an address without a network mask. '''
	return str(in_ip).split('/', 1)[0]

def search_handle(text: str, in_ip):
	count = 0
	rez = -1
	nomask = ip_no_mask(in_ip)
	for elem in text.split('\n'):
		if nomask in elem:
			rez = count
		count += 1
	if rez != -1:
		return text.split('\n')[rez].split(' ')[-1]
	else:
		return None

def main():
	data='''chain INPUT { # handle 77
counter packets 104796 bytes 99994613 jump f2b-anginx # handle 506
meta l4proto 6 tcp dport 53 counter packets 98 bytes 4304 accept # handle 78
meta l4proto 17 udp dport 53 counter packets 1035 bytes 67093 accept # handle 79
meta l4proto 17 udp dport 5353 counter packets 111 bytes 8561 accept # handle 80
meta l4proto 6 tcp dport 853 counter packets 87214 bytes 5581132 accept # handle 81
ip saddr 10.10.10.0/24 counter packets 10568 bytes 422720 accept # handle 480
ip saddr 52.162.218.19 counter packets 0 bytes 0 drop # handle 483
ip saddr 43.128.227.146 counter packets 0 bytes 0 drop # handle 484
ip saddr 134.209.243.49 counter packets 0 bytes 0 drop # handle 485
ip saddr 35.216.199.51 counter packets 0 bytes 0 drop # handle 487
ip saddr 193.187.172.27 counter packets 0 bytes 0 drop # handle 488
ip saddr 178.62.216.118 counter packets 0 bytes 0 drop # handle 489
ip saddr 193.35.18.177 counter packets 0 bytes 0 drop # handle 490
ip saddr 148.153.45.234 counter packets 0 bytes 0 drop # handle 491
ip saddr 206.189.29.146 counter packets 0 bytes 0 drop # handle 492
ip saddr 188.166.151.195 counter packets 0 bytes 0 drop # handle 493
ip saddr 193.56.29.164 counter packets 0 bytes 0 drop # handle 494
ip saddr 34.124.185.168 counter packets 0 bytes 0 drop # handle 496
ip saddr 221.122.67.75 counter packets 2 bytes 80 drop # handle 497
ip saddr 185.83.254.56 counter packets 0 bytes 0 drop # handle 498
ip saddr 162.0.234.213 counter packets 0 bytes 0 drop # handle 499
ip saddr 114.67.217.170 counter packets 0 bytes 0 drop # handle 500
ip saddr 221.130.143.254 counter packets 0 bytes 0 drop # handle 501
ip saddr 58.144.148.20 counter packets 0 bytes 0 drop # handle 502
ip saddr 182.42.60.18 counter packets 0 bytes 0 drop # handle 503'''
	#ip = '193.56.29.164'
	ip = '193.56.29.164/32'
	handle = search_handle(data, ip)
	print(handle)
	ip = '193.56.29.165/24'
	handle = search_handle(data, ip)
	print(handle)

if __name__ == '__main__':
	main()
