#!/bin/bash
#5-post_params.sh
curl -sX POST -d 'email=hr@holbertonschool.com' -d 'subject=I will always be here for PLD' $1
