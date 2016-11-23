import bpmdetect
import os
from pydub import AudioSegment
import datetime
import spotipy.util as util
import spotipy
import musicdownloader
import gmusicapi
import auth
import json
import string
import codecs
import pyechonest
from pyechonest import song
import Database


if __name__ == '__main__':

    auth
    testedtraks=dict()

    #with open('data.json') as data_file:    
    #    testedtraks = json.load(data_file)
    print(datetime.datetime.now())
    dir = 'D:/lib/'
    errornames=[]
    data=auth.SPsearch()
    fulldata= auth.SPgetinfo(data)
    Database.fillDB(fulldata)
    print(datetime.datetime.now())

    #api = musicdownloader.GMauth();
    #for namelist in data:
    #    for track in namelist:
    #        name=track['track']['name']
    #        artist= track['track']['artists'][0]['name']
            
    #        if track['track']['id'] not in testedtraks:
    #           # try:
    #                results = song.search(artist="Tania Bowra", title="All I Want", results=1, buckets=['audio_summary'])
    #                if len(results) > 0:
    #                    print(results[0].audio_summary['tempo'])
    #                #musicdownloader.getsong(api, name, dir)
    #                #sound = AudioSegment.from_mp3(dir  + name + '.mp3')
    #                #sound.export(dir + name + '.wav', format="wav")
    #                #testedtraks[track['track']['id']]=bpmdetect.bpmdetect(dir + str(name+'.wav')).tolist()
    #                #os.remove(dir + name + '.wav')
    #            #except:
    #                print('not found')
    #                errornames.append(track['track'])
    #        print(str(name).encode("UTF-8"))
    #    print(datetime.datetime.now())
    #musicdownloader.logout(api)
    #with open('data.json', 'w') as f:
    #    json.dump(testedtraks, f, ensure_ascii=False)
    #f.close()

