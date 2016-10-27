import bpmdetect
import os
from pydub import AudioSegment
import datetime
import spotipy.util as util
import SPsearchplaylist
import spotipy
import auth



if __name__ == '__main__':
    auth

    print(datetime.datetime.now())
   # dir = 'd:/pymus'

    #dfs для работы следующего метода нужна авторизация
    SPsearchplaylist.search()


    '''
    namelist = os.listdir(dir)

    namelist = filter(lambda x: x.endswith('.mp3'), namelist)

    for name in namelist:
        sound = AudioSegment.from_mp3(dir+'/'+name)
        sound.export(dir+'/'+name[0:-3]+'wav', format="wav")
        os.remove(dir + '/' + name)

    namelist = os.listdir(dir)

    namelist =filter(lambda x: x.endswith('.wav'), namelist)

    for name in namelist:
        bmpanaliz = bpmdetect.bpmdetect(dir+'/'+str(name))
        print(datetime.datetime.now())
    '''