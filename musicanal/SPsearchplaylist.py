import pprint

import spotipy
import sys

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

def search():

    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = 'sport'

    sp = spotipy.Spotify()
    result = sp.search(search_str, 5, 0, 'playlist')
    for playlist in result['playlists']['items']:
        print(playlist['name'])
        results = sp.user_playlist(playlist['owner']['id'], playlist['id'], fields="tracks,next")# '94a636ebaa3f46d1af9c8dcf66858daf', '8b057cb6a70641969d3a5b706dc501d9')
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)

    #pprint.pprint(result.playlists)
