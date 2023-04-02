#!/bin/bash

echo "Starting $NAME as `whoami`"

source ~/.bashrc

exec python3 email_script.py >> logs.log