#!/usr/bin/env bash

case $1 in
init)
    pip3 install --upgrade pip
    pip3 install -r stable-req.txt
 ;;
esac