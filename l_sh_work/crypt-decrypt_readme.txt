

openssl enc -aes-256-cbc -in ./doc.pdf -out doc.pdf.enc -iter 100000

Ещё настоятельно рекомендуется использовать опцию -iter ЧИСЛО. 
Она использует указанное ЧИСЛО итераций для пароля при получении ключа шифрования. 
Высокие значения увеличивают время, необходимое для взлома пароля брут-форсом зашифрованного файла. 
Эта опция включает использование алгоритма PBKDF2 для получения ключа. 
Указывать можно большие значения — десятки и сотни тысяч.

openssl enc -aes-256-cbc -d -in ./doc.pdf.enc -out doc.pdf -iter 100000


openssl rand -base64 32 > key.bin

key.bin
0J2cXGzGSEnb2VT9jzFHf4z6n4rWPzvQsfZxy60/Ojg=

echo "@SysadminNotes" | openssl enc -aes-256-cbc -a -salt -pass file:./key.bin 2>/dev/null

echo "U2FsdGVkX1888FjYUs/Fo01pPIsjTmQKKbdJUrwoFdw=" | openssl enc -aes-256-cbc -a -d -salt -pass file:./key.bin 2>/dev/null


echo "@SysadminNotes" | openssl enc -aes-256-cbc -a -salt -pass pass:wtf
U2FsdGVkX1+POx2jdygSNT9tj2zxTAiZUUN7Ib+wL98=

echo "U2FsdGVkX1+POx2jdygSNT9tj2zxTAiZUUN7Ib+wL98=" | openssl enc -aes-256-cbc -a -d -salt -pass pass:wtf


echo '@SysadminNotes' | gpg -c -a | base64
123
123

LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tCgpqQTBFQndNQ3FOSE80MW1EUVJMcTBrUUJESDFl
RHJVL2lXR1E3T1VhN3hYU25ITFVTclhJSy9ESEphN3dNRGRhCjByZGI1dmU5VERHRWVBa0RMUDhr
dWdKcGJJeHdqOUhMTlJVcWVZaUR6eFNZeHlMa01RPT0KPWo3R3MKLS0tLS1FTkQgUEdQIE1FU1NB
R0UtLS0tLQo=

echo "LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tCgpqQTBFQndNQ3FOSE80MW1EUVJMcTBrUUJESDFlRHJVL2lXR1E3T1VhN3hYU25ITFVTclhJSy9ESEphN3dNRGRhCjByZGI1dmU5VERHRWVBa0RMUDhrdWdKcGJJeHdqOUhMTlJVcWVZaUR6eFNZeHlMa01RPT0KPWo3R3MKLS0tLS1FTkQgUEdQIE1FU1NBR0UtLS0tLQo=" | base64 -d | gpg -d
@SysadminNotes




