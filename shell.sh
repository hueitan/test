#!/bin/sh
while [ true ]
do
    # master
    git pull origin master
    python scrape.py
    # gh-pages
    git checkout gh-pages
    git pull origin gh-pages
    git add restaurant.json
    git commit -m 'Update data'
    git push origin gh-pages

    # sleep 30
    sleep 30
done
