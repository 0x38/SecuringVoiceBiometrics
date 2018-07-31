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

class CompareModel:
    def compare(self,template,testmodel):
        R = robj.r
        DTW = importr('dtw')

        # Generate our data
        print "____________________compare_model____________________"
        print template.shape
        print testmodel.shape
        rt,ct = template.shape
        rq,cq = testmodel.shape

        #converting numpy matrices to R matrices
        templateR=R.matrix(template,nrow=rt,ncol=ct)
        queryR=R.matrix(testmodel,nrow=rq,ncol=cq)

        # Calculate the alignment vector and corresponding distance
        alignment = R.dtw(templateR,queryR,keep=True, step_pattern=R.rabinerJuangStepPattern(4,"c"),open_begin=True,open_end=True)

        dist = alignment.rx('distance')[0][0]


        steps = (template.shape[0]-1) * (template.shape[1]-1) *(testmodel.shape[0]-1)
        print "***model_compare***"
        print dist
        print steps
        print template.shape
        # print template.shape
        print testmodel.shape
        print "*******************"
        return dist,steps
