import bpmdetect
import os
from pydub import AudioSegment



if __name__ == '__main__':
    dir = 'd:/pymus'
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