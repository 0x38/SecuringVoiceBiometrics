import scipy.io.wavfile as wav
import numpy as np
rate,data = wav.read("vasanth1.wav")
audio = np.ndarray(shape=(data.shape[0],),dtype='int16')
# audio = audio.transpose()
x = data.shape
# y = x[0]
for i in range(0,x[0],1):
    if data[i] < 0:
        audio[i] = data[i] % np.iinfo(np.int16).max
    else:
        audio[i] = data[i] % np.iinfo(np.int16).min
# print np.iinfo(np.int16).max
# print -24 % -7
    # print "For"
wav.write("testint16.wav",rate,audio)
