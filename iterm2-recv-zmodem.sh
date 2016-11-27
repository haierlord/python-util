#!/bin/bash
# iterm2-recv-zmodem.sh

FILE=`osascript -e 'tell application "iTerm" to activate' -e 'tell application "iTerm" to set thefile to choose folder with prompt "Choose a folder to place received files in"' -e "do shell script (\"echo \"&(quoted form of POSIX path of thefile as Unicode text)&\"\")"`

if [[ $FILE = "" ]]; then
    echo Cancelled.
    # Send ZModem cancel
    echo -e \\x18\\x18\\x18\\x18\\x18
    echo \# Cancelled transfer
    echo
else
    echo $FILE
    cd "$FILE"
    /usr/local/bin/rz 
    echo \# Received $FILE
    echo
fi
