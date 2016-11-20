import bpmdetect
import os
from pydub import AudioSegment
import datetime
import spotipy.util as util
import SPsearchplaylist
import spotipy
import musicdownloader
import gmusicapi
import auth
import json
import string
import codecs

if __name__ == '__main__':

    auth
    testedtraks=dict()
    with open('data.json') as data_file:    
        testedtraks = json.load(data_file)
    print(datetime.datetime.now())
    dir = 'D:/lib/'
    errornames=[]
    data=auth.SPsearch()


    api = musicdownloader.GMauth();
    for namelist in data:
        for track in namelist:
            name=track['track']['name']
            if track['track']['id'] not in testedtraks:
                try:
                    musicdownloader.getsong(api, name, dir)
                    sound = AudioSegment.from_mp3(dir  + name + '.mp3')
                    sound.export(dir + name + '.wav', format="wav")
                    testedtraks[track['track']['id']]=bpmdetect.bpmdetect(dir + str(name+'.wav')).tolist()
                    os.remove(dir + name + '.wav')
                except:
                    print('not found')
                    errornames.append(track['track'])
            print(str(name).encode("UTF-8"))
        print(datetime.datetime.now())
    musicdownloader.logout(api)
    with open('data.json', 'w') as f:
        json.dump(testedtraks, f, ensure_ascii=False)
    f.close()

