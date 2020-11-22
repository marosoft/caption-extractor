#!/bin/bash

# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
set -euo pipefail

# Create Python venv
[ ! -d $ENV_PATH ] && python -m venv $ENV_PATH
# Activate
source $ENV_PATH/bin/activate

python -m pip install -r requirements.txt

# patch
patch $ENV_PATH/lib/python3.8/site-packages/download_youtube_subtitle/main.py download_youtube_subtitle.patch
