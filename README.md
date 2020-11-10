# Caption Extractor

## Explanation
This script is used to extract the captions from each video. The results of this can be found <a href="https://github.com/repair-manual/youtube-captions">here</a>.

## The Playlist
This the YouTube Playlist: https://www.youtube.com/playlist?list=PLkVbIsAWN2lsHdY7ldAAgtJug50pRNQv0

# Usage

Set env vars:
```bash
CAPTIONS_REPO=https://github.com/marosoft/youtube-captions.git
REPO_PATH=/tmp/out
GOOGLE_API_KEY=[YOUR_API_KEY]
```

Invoke the script:
`./process-new-videos.sh`



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

