#!/bin/bash

# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
set -euo pipefail

git clone --depth 1 https://${GIT_USERNAME}:${GIT_TOKEN}@${CAPTIONS_REPO} ${REPO_PATH} -b master

# Activate
source $ENV_PATH/bin/activate

python process-new-videos.py -p PLkVbIsAWN2lsHdY7ldAAgtJug50pRNQv0 -o ${REPO_PATH}

export SCRIPT_PWD=$PWD

cd ${REPO_PATH}
git config user.name ${GIT_USERNAME}
git config user.email ${GIT_EMAIL}
git remote set-url origin https://${GIT_USERNAME}:${GIT_TOKEN}@${CAPTIONS_REPO}
export outcome=$(git status -s captions/. | wc -l)
[ $outcome -gt 0 ] && git add captions
git add fails.txt
git add titles.txt
export outcome=$(git status -s | wc -l)
[ $outcome -gt 0 ] && git commit -m "New captions" && git push

cd $SCRIPT_PWD
