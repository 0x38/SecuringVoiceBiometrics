'''
Class to write audio chunks into database
Author : Vasanthakumar N
Date   : 09 Mar 2018

Todo
Error handling, unit testing
'''

from pymongo import MongoClient
import scipy.io.wavfile as wav
import numpy as nd
from bson.binary import Binary
import pickle

class WriteAudio:
    def __init__(self,db,collection,querylist):     #Constructor to initialize info requied for write operation
        self.con = MongoClient('localhost',27017)
        self.db = eval ('self.con.' + db)
        self.collection = collection
        self.querylist = querylist


    def write_data(self,audio):
        if self.querylist[0] == 0:                 # For individual queries
            db = self.db
            print db
            query = 'db' + '.' + self.collection + '.' + self.querylist[1]
            eval(query)
        # if self.querylist[0] == 0:               # For multiple queries



if __name__ == '__main__':                         # Driver
        rate, data = wav.read('eric.wav')
        audio = Binary(pickle.dumps(data, protocol=2))
        prepared_query = [0,'insert_one({\"static_phrase\": audio})']
        obj = WriteAudio('BMS','Static',prepared_query)
        obj.write_data(audio)
