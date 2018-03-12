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
import pickle
from bson.binary import Binary
from bson import BSON



class WriteAudio:
    def __init__(self,db,collection,querylist):     #Constructor to initialize info requied for write operation
        self.con = MongoClient('localhost',27017)
        self.db = eval ('self.con.' + db)
        self.collection = collection
        self.querylist = querylist


    def write_data(self,audio):
        if self.querylist[0] == 0:                 # For individual queries
            query = 'self.db' + '.' + self.collection + '.' + self.querylist[1]
            return eval(query)
        # if self.querylist[0] == 1:               # For multiple queries to be executed by a single object



if __name__ == '__main__':                         # Driver
        rate, data = wav.read('resources/eric.wav')
        print type(data)
        pickled = pickle.dumps(data, protocol=2)
        print type(pickled)
        audio = pickled
        print type(audio)
        prepared_query = [0,'insert_one({\"static_phrase\": audio})']
        obj = WriteAudio('TestDataBase','Static',prepared_query)
        status = obj.write_data(audio)
