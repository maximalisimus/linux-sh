#!/bin/bash
openssl rand -hex 6 | sed 's/\(..\)\(..\)\(..\)\(..\)\(..\)\(..\)/\1:\2:\3:\4:\5:\6/' # | tr '[:lower:]' '[:upper:]'
openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/:$//' # | tr '[:lower:]' '[:upper:]'
exit 0
