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



if __name__ == '__main__':
    auth
    testedtraks=dict()
    print(datetime.datetime.now())
    dir = 'D:/lib/'
    
    data=auth.SPsearch()
    '''
    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    f.close()
    print(datetime.datetime.now())

    with open('data.json') as f:
        data = json.load(f)
    f.close()
    print(datetime.datetime.now())
    '''
    api = musicdownloader.GMauth();
    for namelist in data:
        for track in namelist:
            name=track['track']['name']
            if track['track']['id'] not in testedtraks:
                try:
                    musicdownloader.getsong(api, name, dir)
                    sound = AudioSegment.from_mp3(dir  + name + '.mp3')
                    sound.export(dir + name + '.wav', format="wav")
                    testedtraks[track['track']['id']]=bpmdetect.bpmdetect(dir + str(name+'.wav'))
                    os.remove(dir + name + '.wav')
                except:
                    print('not found')
            print(str(name).encode("UTF-8"))
        print(datetime.datetime.now())
    musicdownloader.logout(api)
    with open('data.json', 'w') as f:
        json.dump(testedtraks, f, ensure_ascii=False)
    f.close()
