# url = "https://accounts.spotify.com/authorize"
# data = {
# 	"client_id": "2677052c01ac46f69ae9fa2dd8a5ffc2",
# 	"response_type": "code",
# 	"redirect_uri": "https://31c0c4a3.ngrok.io",
# 	"scope": ["user-read-private", "user-read-email"]
# }

import spotipy
import sys
import spotipy.util as util
import os

os.environ['SPOTIPY_CLIENT_ID'] = "94a636ebaa3f46d1af9c8dcf66858daf"
os.environ['SPOTIPY_CLIENT_SECRET'] = "8b057cb6a70641969d3a5b706dc501d9"
os.environ['SPOTIPY_REDIRECT_URI'] = "https://c5346607.ngrok.io/auth/"


#if len(sys.argv) > 1:
username = 'diakov111'
#else:
 #   print("Whoops, need your username!")
  #  print("usage: python featured_playlists.py [username]")
   # sys.exit()

def SPsearch():
    token = util.prompt_for_user_token(username)

    if token:
    # sp = spotipy.Spotify(auth=token)

    # response = sp.featured_playlists()
    # print(response['message'])

    # while response:
    #     playlists = response['playlists']
    #     for i, item in enumerate(playlists['items']):
    #         print(playlists['offset'] + i, item['name'])

    #     if playlists['next']:
    #         response = sp.next(playlists)
    #     else:
    #         response = None

        data = []
        search_str = 'sport'

        sp = spotipy.Spotify(auth=token)
        result = sp.search(search_str, 12, 0, 'playlist')

        for playlist in result['playlists']['items']:
          print(playlist['name'].encode("utf-8"))
          results = sp.user_playlist(playlist['owner']['id'], playlist['id'], fields="tracks,next")
          tracks = results['tracks']
          data.append(tracks['items'])
        return data
    else:
        print("Can't get token for", username)

def SPgetinfo(data):
    token = util.prompt_for_user_token(username)
    fulldata=[]
    
    if token:
        sp = spotipy.Spotify(auth=token)
        for namelist in data:
            for track in namelist:
                if track['track']['id'] not in fulldata:
                    trackdata=dict()
                    trackdata['id']=track['track']['id']
                    trackdata['name']=track['track']['name']
                    trackdata['artists']=track['track']['artists']
                    trackdata['tempo']=sp.audio_features([track['track']['id']])[0]['tempo']
                    fulldata.append(trackdata)
    return fulldata                   