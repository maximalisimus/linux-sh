

sh-add and SSH_ASKPASS

ssh_pass=$(mktemp /tmp/ssh-pass-XXXXXXX)
echo -e -n "printf \"mikl\n\"" > "$ssh_pass" && chmod 700 "$ssh_pass" && cat ./id_rsa | SSH_ASKPASS=$ssh_pass ssh-add -
rm -rf "$ssh_pass"
unset ssh_pass

ssh-add -d id_rsa




expect-standart.sh

#!/usr/bin/expect

spawn ssh-add ./id_rsa
expect "Enter passphrase for ./id_rsa: "
send "pass\n"
expect "Identity added: "
interact
exit 0




expect.sh

#!/bin/bash

COMM="
spawn ssh-add ${1}
expect \"Enter passphrase for ./id_rsa: \"
send \"$2\n\"
expect \"Identity added: \"
interact
"

output=$(expect -c "$COMM")
echo "${output[*]}"

exit 0



