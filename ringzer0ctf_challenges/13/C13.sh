#!/bin/sh

wget --load-cookies=cookie.txt "https://ringzer0ctf.com/challenges/13" -O main.html -q
#xclip -selection clipboard main.html

cat main.html | tr -d '\n',' ' | grep  -o -P '(?<=(-----BEGINMESSAGE-----))(.)*?(?=(-----ENDMESSAGE-----))'
