#!/bin/bash

buildPack=python

# Get API Key
API_KEY=`python3 -c "import json; file = open('.config/heroku.json'); data=json.loads(file.read()); print(data['api_key']); file.close()"`
curlSettings="-H \"Accept: application/vnd.heroku+json; version=3\" -H \"Content-Type: application/json\""
curlSettings="$curlSettings -H \"Authorization: Bearer ${API_KEY}\""

# Ask Props
echo -n "Enter app name: "
read appName
payLoad="-d '{\"name\": \"${appName}\", \"region\": \"us\", \"stack\": \"heroku-20\"}'"
echo "Creating app=${appName}..."

# Create App
eval "curl $curlSettings $payLoad -X POST https://api.heroku.com/apps" > .config/response_create.json
echo -e "Heroku-App-Create response saved in .config/response_create.json...\n"

# Add Buildpack (optional)
if [ -z $buildPack ]; then
echo -n "Enter buildpack name: "
read buildPack
fi
payLoad="-d '{\"updates\": [{\"buildpack\": \"https://github.com/heroku/heroku-buildpack-${buildPack}\"}]}'"
echo "Installing buildpack=${buildPack}..."
eval "curl $curlSettings $payLoad -X PUT https://api.heroku.com/apps/${appName}/buildpack-installations" > .config/response_buildpack.json
echo -e "Heroku-Buildpack-Install response saved in .config/response_buildpack.json...\n"

# Add Remote
if [ -d .git ]; then
if [ `git remote | grep "^heroku$"` ]; then
git remote set-url heroku "https://git.heroku.com/${appName}.git"
echo "Heroku Git Repo renamed successfully: https://git.heroku.com/${appName}.git"
else
git remote add heroku "https://git.heroku.com/${appName}.git"
echo "Heroku Git Repo added successfully: https://git.heroku.com/${appName}.git"
fi
else
echo -e "This is not a Git repository...\nHeroku Git Repo: https://git.heroku.com/${appName}.git"
fi
