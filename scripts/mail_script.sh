#!/bin/bash

echo "Starting $NAME as `whoami`"

source ~/.bashrc

exec python email_script.py >> logs.log
