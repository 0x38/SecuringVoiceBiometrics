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


    def write_data(self,data):
        if self.querylist[0] == 0:                 # For individual queries
            db = self.db

            query = 'db' + '.' + self.collection + '.' + self.querylist[1]
            print query
            eval(query)
        # if self.querylist[0] == 1:               # For multiple queries to be executed by a single object

    def update_users(self,newUser):
        db = self.db
        db.UserNames.update_one({'_id':1}, {'$push': {'UserName':newUser}})
        print "done"


if __name__ == '__main__':                         # Driver
        rate, data = wav.read('resources/eric.wav')
        obj.write_data(audio)
        prepared_query = [0,'insert_one({\"static_phrase\": audio})']
        obj = WriteAudio('BMStest2','Static',prepared_query)
        audio = Binary(pickle.dumps(data,protocol=2))
        obj.write_data(audio)
