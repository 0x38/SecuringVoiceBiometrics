import sys
import scipy.io.wavfile as wav
import numpy as np

class Silence:
    def __init__(self,signal):
        self.array = np.ones(10, dtype=np.int16)
        self.array = self.array * 10
        print self.array
        self.array = self.array.astype(np.int64)
        print self.array
        # self.signal = signal
        # self.orig_dtype = type(signal[0])
        # self.typeinfo = np.iinfo(orig_dtype)
        # self.is_unsigned = typeinfo.min >= 0
        # self.signal = signal.astype(np.int64)

    #
    # def remove_silence(self):
    #     print "h"


if __name__ == '__main__':
    fs, signal = wav.read(sys.argv[1])
    obj = Silence(signal)
    # obj.remove_silence()
