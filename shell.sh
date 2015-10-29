#!/bin/sh
while [ true ]
do
    python scrape.py
    git add -A
    git commit -m 'Update data'
    git push origin master
    sleep 30
done
