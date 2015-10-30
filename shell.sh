#!/bin/sh
while [ true ]
do
    # master
    git checkout master
    git pull origin master
    # scrape taipei
    python scrape.py taipei
    sleep 10
    # scrape taichung
    python scrape.py taichung
    sleep 10
    # scrape kaohsiung
    python scrape.py kaohsiung
    sleep 10
    # scrape japan
    python scrape.py japan
    git add -A
    git commit -m 'Update data'
    git push origin master

    # sleep 10
    sleep 10

    # gh-pages
    git checkout gh-pages
    git pull origin gh-pages
    git checkout master -- restaurant-*.json
    git add restaurant-*.json
    git commit -m 'Update data'
    git push origin gh-pages

    # sleep 300 - 5 minutes
    sleep 300
done
