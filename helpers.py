import os
# import re

# from pytube import Playlist
from download_youtube_subtitle.main import get_data, get_tracks_title, main, parseVideoID

import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

def get_video_id_from_url(video_url):
    query = parse_qs(urlparse(video_url).query, keep_blank_values=True)
    return query["v"][0]

def get_playlist_id_from_url(playlist_url):
    query = parse_qs(urlparse(playlist_url).query, keep_blank_values=True)
    return query["list"][0]

# This method would use download_youtube_subtitle lib to obtain the title
# def get_title_using_lib(videoID):
#     _, _, data_link = parseVideoID(videoID)
#     data=get_data(data_link)
#     _, title = get_tracks_title(data)
#     return title

# This does not work as it seems there is a bug in the pytube library
# def get_videos_using_lib(playlist_id):
#     playlist= Playlist(playlist_id)
#     #this fixes the empty playlist.videos list
#     playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

#     videos = []
#     for url in playlist.video_urls:
#         video_id = get_video_id_from_url(url)
#         videos += {
#             'videoID': video_id,
#             'title': get_title_using_lib(video_id)
#         }
#     return videos

def get_videos(playlist_id):
    print(f'get all playlist items links from {playlist_id}')
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = os.environ['GOOGLE_API_KEY'])

    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    print(f"total: {len(playlist_items)}")

    videos = []

    for playlist_item in playlist_items:
        videos.append({
            'videoID': playlist_item["snippet"]["resourceId"]["videoId"],
            'title': playlist_item["snippet"]["title"]
        })
    return videos

    # Example element (a video) of an array from the response:
    # {
    #   "kind": "youtube#playlistItem",
    #   "etag": "zAlQIQGMJAaGKCnyPnXjEcTjq9A",
    #   "id": "UExrVmJJc0FXTjJsc0hkWTdsZEFBZ3RKdWc1MHBSTlF2MC41RjE3Q0ExQjdGMzgyQzI2",
    #   "snippet": {
    #     "publishedAt": "2020-11-07T01:12:44Z",
    #     "channelId": "UCl2mFZoRqjw_ELax4Yisf6w",
    #     "title": "Demonstration of our industry leading quality control/quality assurance post-repair testing.",
    #     "description": "We repair Macbook logic boards: https://rossmanngroup.com/macbook-logic-board-repair\n👉 DISCORD chat server: https://discord.gg/X54g8gm\n👉 Rossmann Repair Group Inc is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to amazon.com\n\n✖ Buying on eBay? Support us while you shop! https://www.rossmanngroup.com/ebay",
    #     "thumbnails": {
    #       "default": {
    #         "url": "https://i.ytimg.com/vi/7jCELmSji_A/default.jpg",
    #         "width": 120,
    #         "height": 90
    #       },
    #       "medium": {
    #         "url": "https://i.ytimg.com/vi/7jCELmSji_A/mqdefault.jpg",
    #         "width": 320,
    #         "height": 180
    #       },
    #       "high": {
    #         "url": "https://i.ytimg.com/vi/7jCELmSji_A/hqdefault.jpg",
    #         "width": 480,
    #         "height": 360
    #       },
    #       "standard": {
    #         "url": "https://i.ytimg.com/vi/7jCELmSji_A/sddefault.jpg",
    #         "width": 640,
    #         "height": 480
    #       },
    #       "maxres": {
    #         "url": "https://i.ytimg.com/vi/7jCELmSji_A/maxresdefault.jpg",
    #         "width": 1280,
    #         "height": 720
    #       }
    #     },
    #     "channelTitle": "Louis Rossmann",
    #     "playlistId": "PLkVbIsAWN2lsHdY7ldAAgtJug50pRNQv0",
    #     "position": 2,
    #     "resourceId": {
    #       "kind": "youtube#video",
    #       "videoId": "7jCELmSji_A"
    #     }
    #   }
    # },