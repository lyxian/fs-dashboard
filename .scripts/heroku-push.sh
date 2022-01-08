#!/bin/bash 

BRANCH=`git rev-parse --abbrev-ref HEAD`

git checkout $BRANCH
git branch -M main
git push -u heroku main
if [ $? -eq 0 ]; then
echo "=====Code deployed to Heroku successfully====="
else
echo "=====Code not deployed to Heroku====="
fi

git branch -M $BRANCH


