import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util

def search():

    username = 'diakov111'
    playlist_name = 'Sport'
    print("Usage: %s username playlist-name" % (sys.argv[0],))

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlist_name)

    else:
        print("Can't get token for", username)

