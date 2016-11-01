from __future__ import print_function, division, absolute_import, unicode_literals
from builtins import *  # noqa

from gmusicapi import Mobileclient
import gmusicapi
import urllib.request


email="TblZmusicbot"
password="TblZmusicbot123"


def ask_for_credentials():
    # We're not going to upload anything, so the Mobileclient is what we want.
    api = Mobileclient()


    logged_in = False
    attempts = 0

    while not logged_in and attempts < 3:
        logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
        attempts += 1

    return api

def GMauth():
    api = ask_for_credentials()

    if not api.is_authenticated():
        print("Sorry, those credentials weren't accepted.")
        return

    print('Successfully logged in.')
    print()


def getsong(song_name):
    song= api.search(song_name, 1)['song_hits'][0]['track']
    url = api.get_stream_url(song['storeId'], device_id=None, quality=u'hi')
    urllib.request.urlretrieve(url, song['title']+'.mp3')

def logout():
    api.logout()

if __name__ == '__main__':
    api = ask_for_credentials()
    getsong('Love Keyshia Cole')
    logout()