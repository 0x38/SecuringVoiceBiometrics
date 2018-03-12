'''
Class to read audio chunks from database
Author : Vasanthakumar N
Date   : 10 Mar 2018

Todo
Error handling, unit testing, verify return status
'''

from pymongo import MongoClient
import scipy.io.wavfile as wav
import numpy as nd
from bson.binary import Binary
import pickle

class ReadAudio:
    def __init__(self,db,collection,querylist):     #Constructor to initialize info requied for write operation
        self.con = MongoClient('localhost',27017)
        self.db = eval ('self.con.' + db)
        self.collection = collection
        self.querylist = querylist


    def read_data(self):
        if self.querylist[0] == 0:                 # For individual queries
            query = 'db' + '.' + self.collection + '.' + self.querylist[1]
            db = self.db
            print query
            return eval(query)
        # if self.querylist[0] == 1:               # For multiple queries to be executed by a single object


if __name__ == '__main__':
    prepared_query = [0,'find()']
    obj = ReadAudio('BMS','Static',prepared_query)
    cursor = obj.read_data()
    for temp in cursor:
        data = temp['static_phrase']
    string1 = String(data)
    print type(string1  )
    unpickled = pickle.load(string1)
    print type(unpickled)
