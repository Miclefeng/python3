#!/bin/bash

git pull origin master
if [ 0 -eq $? ];
then
    chown root:root -R /opt/python/base/python3
fi

