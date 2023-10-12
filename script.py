import webbrowser
from urllib import request

def extract_playlist_id(video_url):
    # Extracts the playlist ID from a YouTube video URL
    parts = video_url.split('&')
    for part in parts:
        if part.startswith('list='):
            return part[5:]
    return None

def create_watch_videos_url(video_ids):
    # Creates a watch_videos URL for a list of video IDs
    return "http://www.youtube.com/watch_videos?video_ids=" + ",".join(video_ids)

def add_videos_to_playlist(video_ids):
    watch_videos_url = create_watch_videos_url(video_ids)

    try:
        response = request.urlopen(watch_videos_url)
        playlist_url = response.geturl()
        print("Playlist URL:", playlist_url)

        playlist_id = extract_playlist_id(playlist_url)

        if playlist_id:
            play_list_url = "https://www.youtube.com/playlist?list=" + playlist_id + "&disable_polymer=true"
            webbrowser.open(play_list_url)
        else:
            print("Playlist link not found in URL.")

    except Exception as e:
        print("Error:", e)

# Read video IDs from file
with open("list.txt", 'r') as f:
    all_video_ids = [line.strip() for line in f]

# Split the video IDs into chunks of 50
chunk_size = 50
video_id_chunks = [all_video_ids[i:i+chunk_size] for i in range(0, len(all_video_ids), chunk_size)]

# Add videos to playlists for each chunk
for chunk in video_id_chunks:
    add_videos_to_playlist(chunk)
