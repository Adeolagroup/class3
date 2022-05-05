#!/bin/bash
for user in `cat userlist.txt`
do
   echo "We are going to create user $user"
   useradd -m $user
done
