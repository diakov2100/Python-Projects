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



if __name__ == '__main__':
    auth

    print(datetime.datetime.now())
    dir = ''
    
    data=SPsearchplaylist.search()
    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    f.close()
    print(datetime.datetime.now())
    '''
    with open('data.json') as f:
        data = json.load(f)
    f.close()
    print(datetime.datetime.now())
    
    api = musicdownloader.GMauth();
    namelist= ['Love', 'Die']

    namelist
    for name in namelist:
        musicdownloader.getsong(api, name)
        sound = AudioSegment.from_mp3(dir  + name + '.mp3')
        sound.export(dir + name + '.wav', format="wav")
        bmpanaliz = bpmdetect.bpmdetect(dir + str(name+'.wav'))
        os.remove(dir + name + '.wav')
        print(datetime.datetime.now())

    musicdownloader.logout(api)
    '''