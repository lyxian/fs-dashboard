#!/bin/bash 

BRANCH=`git rev-parse --abbrev-ref HEAD`

echo -n "DEBUG_MODE (y/n): "
read DEBUG

git checkout -b heroku_${BRANCH}
git pull heroku main
if [ `echo $DEBUG | grep -i y` ]; then 
echo "web: python app.py" > Procfile
else
echo "web: gunicorn app:server" > Procfile
fi
git add Procfile

if [ -f runtime.txt]; then
echo "python-3.8.12" > runtime.txt
git add runtime.txt
fi

if [-f requirements.txt]; then
pip freeze > requirements.txt
git add requirements.txt
fi

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
