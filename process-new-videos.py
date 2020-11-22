import os, sys, getopt

from helpers import get_playlist_id_from_url, get_videos, main

# playlist_url = 'https://www.youtube.com/playlist?list=PLkVbIsAWN2lsHdY7ldAAgtJug50pRNQv0'

def usage():
    print('test.py -p <playlist_id> -o <output_path>')

def parse_args(argv):
    playlist_id = ''
    output_path = ''
    try:
        opts, args = getopt.getopt(argv,"hp:o:",["playlist=","output_path="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-p", "--playlist"):
            playlist_id = arg
        elif opt in ("-o", "--output_path"):
            output_path = arg
    return playlist_id, output_path

if __name__ == "__main__":
    playlist_id, output_path = parse_args(sys.argv[1:])

    path = os.path.abspath(output_path)
    path_captions = os.path.join(path, 'captions')

    # playlist_id = get_playlist_id_from_url(playlist_id)
    videos = get_videos(playlist_id)
    count = 0
    maxx = len(videos)
    videos_titles = ''
    failed_videos = ''

    os.makedirs(path_captions, exist_ok=True)
    already_processed = os.listdir(path_captions)

    for video in videos:
        count +=1
        print('=='*20)
        print(f'getting {count} of {maxx} : {video["videoID"]}')
        print('=='*20)
        if video["videoID"] + '.txt' in already_processed:
            print('Already processed. Skipping...')
        else:
            try:
                print(f'Video ID: {video["videoID"]}; Title: {video["title"]}')
                videos_titles += f'{video["videoID"]}:{video["title"]}\n'
                # print(f'Title using lib: {get_title_using_lib(video["videoID"])}')
                main(video["videoID"], translation=False, output_file=f'{os.path.join(path_captions, video["videoID"])}.txt')
            except:
                failed_videos += f'failed to download: {video["videoID"]}\n'
                print(f'failed to download: {video["videoID"]}\n')

    with open(os.path.join(path, 'titles.txt'),'w') as f:
        f.write(videos_titles)
    with open(os.path.join(path, 'fails.txt'),'w') as f:
        f.write(failed_videos)