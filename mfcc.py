from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import sys
import numpy as np

# def mfcc(signal,samplerate=16000,winlen=0.025,winstep=0.01,numcep=13,
                 # nfilt=26,nfft=1103,lowfreq=0,highfreq=None,preemph=0.97,
     # ceplifter=22,appendEnergy=True)

(rate1,sig1) = wav.read("testaudio1.wav")


mfcc_feat1 = mfcc(sig1,rate1)
d_mfcc_feat1 = delta(mfcc_feat1, 2)
fbank_feat1 = logfbank(sig1,rate1)

(rate2,sig2) = wav.read("testaudio2.wav")
mfcc_feat2 = mfcc(sig2,rate2)
d_mfcc_feat2 = delta(mfcc_feat2, 2)
fbank_feat2 = logfbank(sig2,rate2)


print(fbank_feat1)
print(fbank_feat2)
print "*******************************************************"
print sig1.shape
print sig2.shape
print "MFCC"
print mfcc_feat1.shape
print mfcc_feat2.shape
print "DMFCC"
print d_mfcc_feat1.shape
print d_mfcc_feat2.shape
print fbank_feat1.shape
print fbank_feat2.shape
AX,AY = fbank_feat1.shape
print AX
print AY
print "*******************************************************"
print sys.maxint
print type(np.ones((1,2)) )

cost = np.ones((10,10))
print type (cost)
print cost

# print fbank_feat.shape
# print mfcc_feat
