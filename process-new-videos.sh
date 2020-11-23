# Create Python venv
export ENV_PATH=.env
[ ! -d $ENV_PATH ] && python -m venv $ENV_PATH
# Activate
source .env/bin/activate
# pip install
pip install -r requirements.txt
# patch
patch $ENV_PATH/lib/python3.8/site-packages/download_youtube_subtitle/main.py download_youtube_subtitle.patch

git clone --depth 1 ${CAPTIONS_REPO} ${REPO_PATH} -b master

python process-new-videos.py -p PLkVbIsAWN2lsHdY7ldAAgtJug50pRNQv0 -o ${REPO_PATH}

export SCRIPT_PWD=$PWD

cd ${REPO_PATH}
git status -s . | grep captions | grep '^?? ' | sed 's/?? //g' | xargs git add
git add fails.txt
git add titles.txt
git commit -m "New captions"
git push

cd $SCRIPT_PWD

deactivate