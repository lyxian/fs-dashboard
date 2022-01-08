#!/bin/bash 

BRANCH=`git rev-parse --abbrev-ref HEAD`

git checkout $BRANCH
git branch -M main
git push -u heroku main
git branch -M $BRANCH

if [ $? -eq 0 ]; then
echo "=====Code pushed to Heroku successfully====="
else
echo "=====Code not push to Heroku====="
fi

