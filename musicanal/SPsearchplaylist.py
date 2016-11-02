import spotipy
import sys

def search():
    data=[]
    search_str = 'sport'

    sp = spotipy.Spotify()
    result = sp.search(search_str, 5, 0, 'playlist')
    
    for playlist in result['playlists']['items']:
        print(playlist['name'])
        results = sp.user_playlist(playlist['owner']['id'], playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            data.append(tracks)   
    return data
