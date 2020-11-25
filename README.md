# Caption Extractor

## Explanation
This script is used to extract the captions from each video. The results of this can be found <a href="https://github.com/repair-manual/youtube-captions">here</a>.

## The Playlist
This the YouTube Playlist: https://www.youtube.com/playlist?list=PLkVbIsAWN2lsHdY7ldAAgtJug50pRNQv0

# Usage

## Docker - official image

```bash
docker run --rm -t \
--env CAPTIONS_REPO=github.com/[username]/youtube-captions.git \
--env GIT_USERNAME=[username] \
--env GIT_TOKEN=[git_token] \
--env GIT_EMAIL=[email] \
--env GOOGLE_API_KEY=[google_api_key] \
repairmanual/caption-extractor:latest
```

## Local

### Script

Set env vars:
```bash
CAPTIONS_REPO=https://github.com/marosoft/youtube-captions.git
REPO_PATH=/tmp/out
GOOGLE_API_KEY=[YOUR_API_KEY]
```

Invoke the script:
`./process-new-videos.sh`

### Docker

Build image:

```bash
docker build -t caption-extractor .
```

Run:

```bash
docker run --rm -t \
--env CAPTIONS_REPO=github.com/[username]/youtube-captions.git \
--env GIT_USERNAME=[username] \
--env GIT_TOKEN=[git_token] \
--env GIT_EMAIL=[email] \
--env GOOGLE_API_KEY=[google_api_key] \
caption-extractor
```

# Dev Setup

## ENV setup
1. Create a virtual environment (e.g. `python -m venv .env`)
2. Activate the virtual environment (`source .env/bin/activate`)
3. `pip install -r requirements.txt`

## Google API key
It is used to retrieve the list of videos from the playlist.
Obtain the API key by using Google Developer Console. 

It allows 10000 units per day. 
https://developers.google.com/youtube/v3/getting-started#quota
https://developers.google.com/youtube/v3/docs/playlistItems/list

`export GOOGLE_API_KEY=[YOUR_API_KEY]`

## Execution
`python process-new-videos.py -p PLkVbIsAWN2lsHdY7ldAAgtJug50pRNQv0 -o out`

