#!/bin/sh
while [ true ]
do
    python scrape.py
    git status
    sleep 5
done
