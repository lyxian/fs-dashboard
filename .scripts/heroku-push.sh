#!/bin/bash 

BRANCH=`git rev-parse --abbrev-ref HEAD`

echo -n "DEBUG_MODE (y/n): "
read DEBUG

git checkout -b heroku_${BRANCH}
if [ `echo $DEBUG | grep -i y` ]; then 
echo "web: python app.py" > Procfile
else
echo "web: gunicorn app:server" > Procfile
fi

echo "python-3.8.12" > runtime.txt
pip freeze > requirements.txt
git add Procfile runtime.txt requirements.txt 
git commit -m "deploy"

git branch -M main
git push -u heroku main
if [ $? -eq 0 ]; then
echo "=====Code deployed to Heroku successfully====="
git branch -M heroku_${BRANCH}
git checkout $BRANCH 
git branch -D heroku_${BRANCH}
else
git branch -M heroku_${BRANCH}
echo -e "=====Code not deployed to Heroku=====\nCheck source and re-deploy from branch..."
fi
