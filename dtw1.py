from math import *
import numpy as np
import sys
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
# def mfcc(signal,samplerate=16000,winlen=0.025,winstep=0.01,numcep=13,
                 # nfilt=26,nfft=1103,lowfreq=0,highfreq=None,preemph=0.97,
     # ceplifter=22,appendEnergy=True)

(rate1,sig1) = wav.read("testaudio1.wav")
# mfcc_feat1 = mfcc(sig1,rate1)
# d_mfcc_feat1 = delta(mfcc_feat1, 2)
# fbank_feat1 = logfbank(sig1,rate1)
#
(rate2,sig2) = wav.read("testaudio2.wav")
# mfcc_feat2 = mfcc(sig2,rate2)
# d_mfcc_feat2 = delta(mfcc_feat2, 2)
# fbank_feat2 = logfbank(sig2,rate2)
def DTW(A, B, window = sys.maxint, d = lambda x,y: abs(x-y)):

    # A, B = np.array(A), np.array(B)
    M, N = len(A), len(B)
    cost = sys.maxint * np.ones((M, N))


    cost[0, 0] = d(A[0], B[0])
    for i in range(1, M):
        cost[i, 0] = cost[i-1, 0] + d(A[i], B[0])

    for j in range(1, N):
        cost[0, j] = cost[0, j-1] + d(A[0], B[j])

    for i in range(1, M):
        for j in range(max(1, i - window), min(N, i + window)):
            choices = cost[i - 1, j - 1], cost[i, j-1], cost[i-1, j]
            cost[i, j] = min(choices) + d(A[i], B[j])


    n, m = N - 1, M - 1
    path = []

    while (m, n) != (0, 0):
        path.append((m, n))
        m, n = min((m - 1, n), (m, n - 1), (m - 1, n - 1), key = lambda x: cost[x[0], x[1]])

    path.append((0,0))
    return cost[-1, -1], path

def main():
    A = sig1
    B = sig2
    # A = np.random.rand(100,1)
    # B = A
    # C = np.array([7,8,5,9,11,9])
    # B = C
    cost, path = DTW(A, B, window = 200)
    print 'Total Distance is ', cost
    import matplotlib.pyplot as plt
    offset = 5
    plt.xlim([-1, max(len(A), len(B)) + 1])
    plt.plot(A)
    plt.plot(B + offset)
    for (x1, x2) in path:
        plt.plot([x1, x2], [A[x1], B[x2] + offset])
    plt.show()

if __name__ == '__main__':
    main()
