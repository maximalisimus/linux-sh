#!/bin/bash
hexchars="0123456789ABCDEF"
mac=""
for((i = 1 ; i < 7 ; ++i)); do 
	str=""
	for((j = 1 ; j < 3 ; ++j)); do
		str+="${hexchars:$(( $RANDOM % 16 )):1}"
	done
	mac="${mac}${str}:"
done
echo "${mac::17}"
exit 0
