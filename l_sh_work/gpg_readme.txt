

GPG ReadMe.



mkdir -p ./homelab
chown -R mikl:users ./homelab
chmod 0700 ./homelab



gpg.conf

keyid-format 0xshort
throw-keyids
no-emit-version
no-comments

default-key BE2BA3C896E3C043

gpg-agent.conf

default-cache-ttl 300
max-cache-ttl 999999

gpa.conf

default-key 1DEC8548C828F98EBDE8D46ABE2BA3C896E3C043
detailed-view



export GNUPGHOME=./homelab


gpg --homedir=./ --import public-key.gpg --yes

gpg --homedir=./homelab --batch --import private-keys.gpg --pinentry-mode loopback --yes --passphrase mypass

gpg --homedir=./homelab --batch --pinentry-mode loopback --yes --delete-secret-keys 1DEC8548C828F98EBDE8D46ABE2BA3C896E3C043

gpg --homedir=./homelab --batch --pinentry-mode loopback --yes --delete-keys 0x96E3C043

unset GNUPGHOME

rm -rf ./homelab





