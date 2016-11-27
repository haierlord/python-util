#!/bin/bash
# iterm2-send-zmodem.sh

FILE=`osascript -e 'tell application "iTerm" to activate' -e 'tell application "iTerm" to set thefile to choose file with prompt "Choose a file to send"' -e "do shell script (\"echo \"&(quoted form of POSIX path of thefile as Unicode text)&\"\")"`

if [[ $FILE = "" ]]; then
    echo Cancelled.
    # Send ZModem cancel
    echo -e \\x18\\x18\\x18\\x18\\x18
    echo \# Cancelled transfer
    echo
else
    echo $FILE
    /usr/local/bin/sz "$FILE"
    echo \# Received $FILE
    echo
fi

