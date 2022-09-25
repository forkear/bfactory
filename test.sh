#!/bin/bash

SOUND_OK="tests/sounds/complete.oga"
SOUND_ERROR="tests/sounds/bell.oga"

while inotifywait -e close_write -r ./; do 
	 
	clear;
	
	./bfactory.py test  

	if [ $? == 0 ]; then 
		play $SOUND_OK 2> /dev/null
		~/apps/VSCode-linux-x64/bin/code /tmp/test_bfactory/todo_app/apps/api
	else 
		play $SOUND_ERROR 2> /dev/null
	fi
done
