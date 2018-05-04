from __future__ import absolute_import
import numpy as np
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()
from rpy2.robjects.packages import importr
import rpy2.robjects as robj
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from silence import Silence
# obj = Silence()
# global task,remove_silence
# obj.silencemain("Recordings/Santhosh2.wav","temp1.wav")
# obj.silencemain("Recordings/Santhosh1.wav","temp2.wav")
(rate1,sig1) = wav.read("Recordings/vasanth2.wav")
# (rate1,sig1) = wav.read(".wav")
mfcc_feat1 = mfcc(sig1,rate1)
d_mfcc_feat1 = delta(mfcc_feat1, 2)
fbank_feat1 = logfbank(sig1,rate1)

(rate2,sig2) = wav.read("Recordings/vasanth1.wav")
# (rate2,sig2) = wav.read("statictemp.wav")
mfcc_feat2 = mfcc(sig2,rate2)
d_mfcc_feat2 = delta(mfcc_feat2, 2)
fbank_feat2 = logfbank(sig2,rate2)

print fbank_feat1.shape



R = robj.r
DTW = importr('dtw')

# Generate our data
template = fbank_feat1
# template = np.array([[1,2,3,4,5],[1,2,3,4,5]]).transpose()
rt,ct = template.shape
# query = template
query = fbank_feat2
rq,cq = query.shape

#converting numpy matrices to R matrices
templateR=R.matrix(template,nrow=rt,ncol=ct)
queryR=R.matrix(query,nrow=rq,ncol=cq)

# Calculate the alignment vector and corresponding distance
alignment = R.dtw(templateR,queryR,keep=True, step_pattern=R.rabinerJuangStepPattern(4,"c"),open_begin=True,open_end=True)

dist = alignment.rx('distance')[0][0]

print dist
steps = (fbank_feat1.shape[0]-1) * (fbank_feat1.shape[1]-1) *(fbank_feat2.shape[0]-1)
print steps
print dist/(steps/1000000)
print fbank_feat1.shape
print fbank_feat2.shape
