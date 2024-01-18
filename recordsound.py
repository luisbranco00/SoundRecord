# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:06:48 2022

@author: luisb
"""

import pyaudio
import numpy as np
from numpy import log10, sqrt
from Adafruit_IO import *
import json
from json import JSONEncoder
import time

 
aio = Client(X, Key) #provide your Client name and key 


class NumpyArrayEncoder(JSONEncoder): #Convert into json file before introducing in adafruit
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 1024 # 2^12 samples for buffer
audio = pyaudio.PyAudio() 
# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans ,input = True,
                    frames_per_buffer=chunk)

try:
    while True:
        stream.start_stream()
        for i in range(0, int(samp_rate / chunk * 150)):
            data = np.frombuffer(stream.read(chunk),dtype=np.int16)
            data = 20*log10( sqrt((data**2)))
            numpyArrayOne=data
            valores = json.dumps(numpyArrayOne, cls=NumpyArrayEncoder)
            #É preciso passar para Json para meter no adafruit!!!
            valores=valores.split(',')
            for j in range(0,len(valores)):
                if valores[j]!='-Infinity' and valores[j]!='NaN' and valores[j]!='[NaN': 
                    time.sleep(2)
                    valores[j]=valores[j].replace('[', "")
                    aio.send_data("semana2", valores[j])
                    
                else:
                    aio.send_data("semana2", -1)
                    valores[j]=valores[j].replace("NaN","-1")
                    valores[j]=valores[j].replace("-Infinity","-1")
            #É preciso passar para Json para meter no adafruit!!!
except KeyboardInterrupt:
    stream.stop_stream() 
    pass
sound_file = wave.open("record.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.write_frames(b''.join(frames))
sound_file.close()
