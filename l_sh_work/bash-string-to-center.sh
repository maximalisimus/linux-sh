#!/bin/bash

center()
{ 
IFS=""
while read L
do
printf "%b\n" $(printf "%.$((($(tput cols)-${#L})/2))d" 0 | sed 's/0/ /g')$L
done
}

echo "Этот текст будет выведен по центру экрана терминала" | center

exit 0
