#!/bin/bash 

USERFILE=$1

if [ "$USERFILE" = "" ] 
  then 
      echo "Please specify an input file!" 
       exit 10
elif test -e $USERFILE 
  then 
       for user in `cat $USERFILE`  
       do
            echo "deleting the "$user" user..." 
            userdel -r $user  
       done
       exit 20
else
    echo "Invalid input file specified!" 
    exit 30
fi
