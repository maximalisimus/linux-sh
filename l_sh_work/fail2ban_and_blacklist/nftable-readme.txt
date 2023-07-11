
sudo nft list table ip filter

sudo nft --handle --numeric list chain ip filter INPUT

sudo nft delete rule ip filter INPUT handle 10

sudo nft 'add rule ip filter INPUT ip saddr 165.22.60.249 counter drop'
sudo nft 'add rule ip filter INPUT ip saddr 165.22.60.249 counter accept'







table ip filter {
	chain INPUT { # handle 77
		type filter hook input priority 0; policy accept;
		meta l4proto 6 tcp dport 53 counter packets 89 bytes 3916 accept # handle 78
		meta l4proto 17 udp dport 53 counter packets 952 bytes 61684 accept # handle 79
		meta l4proto 17 udp dport 5353 counter packets 98 bytes 7547 accept # handle 80
		meta l4proto 6 tcp dport 853 counter packets 78907 bytes 5049484 accept # handle 81
		ip saddr 10.10.10.0/24 counter packets 2261 bytes 90440 accept # handle 480
		ip saddr 52.162.218.19 counter packets 0 bytes 0 drop # handle 483
		ip saddr 43.128.227.146 counter packets 0 bytes 0 drop # handle 484
		ip saddr 134.209.243.49 counter packets 0 bytes 0 drop # handle 485
		ip saddr 35.216.199.51 counter packets 0 bytes 0 drop # handle 486
		ip saddr 35.216.199.51 counter packets 0 bytes 0 drop # handle 487
		ip saddr 193.187.172.27 counter packets 0 bytes 0 drop # handle 488
		ip saddr 178.62.216.118 counter packets 0 bytes 0 drop # handle 489
		ip saddr 193.35.18.177 counter packets 0 bytes 0 drop # handle 490
		ip saddr 148.153.45.234 counter packets 0 bytes 0 drop # handle 491
		ip saddr 206.189.29.146 counter packets 0 bytes 0 drop # handle 492
		ip saddr 188.166.151.195 counter packets 0 bytes 0 drop # handle 493
		ip saddr 193.56.29.164 counter packets 0 bytes 0 drop # handle 494
		ip saddr 34.124.185.168 counter packets 0 bytes 0 drop # handle 495
		ip saddr 34.124.185.168 counter packets 0 bytes 0 drop # handle 496
		ip saddr 221.122.67.75 counter packets 0 bytes 0 drop # handle 497
		ip saddr 185.83.254.56 counter packets 0 bytes 0 drop # handle 498
		ip saddr 162.0.234.213 counter packets 0 bytes 0 drop # handle 499
		ip saddr 114.67.217.170 counter packets 0 bytes 0 drop # handle 500
		ip saddr 221.130.143.254 counter packets 0 bytes 0 drop # handle 501
		ip saddr 58.144.148.20 counter packets 0 bytes 0 drop # handle 502
		ip saddr 182.42.60.18 counter packets 0 bytes 0 drop # handle 503
	}
}




