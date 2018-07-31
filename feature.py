from __future__ import absolute_import
import numpy as np
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()
from rpy2.robjects.packages import importr
import rpy2.robjects as robj
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import os
import scipy.io.wavfile as wav
from silence import Silence
class Features:
    def featureList(self,path):
        # obj = Silence()
        # newpath = os.path.splitext(path)[0] + "_silenced" + os.path.splitext(path)[1]
        # obj.silencemain(path,newpath)

        (rate,sig) = wav.read(path)
        print "___________________path_________________"
        print sig.shape
        print rate
        print path
        mfcc_feat = mfcc(sig,rate)
        d_mfcc_feat = delta(mfcc_feat, 2)
        fbank_feat = logfbank(sig,rate)

        print "file:feature.py line:24"
        print fbank_feat.shape

        return fbank_feat
