from pymongo import MongoClient
import scipy.io.wavfile as wav
import numpy as nd
from bson import BSON
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
    # def update_tags(self, ref, newUser):
    #     db = self.db
    #     db.UserNames.update_one({'_id':1}, {'$push': {'UserName':newUser}})
    #     print "done"


if __name__ == '__main__':
    prepared_query = [0,'find()']
    # update_tags('not_imp','TestUser5')
    obj = ReadAudio('sbSVB','UserNames',prepared_query)
    Name = "TestUser1"
    # obj.update_tags('not_imp','TestUser6')
    cursor = obj.read_data()
    for temp in cursor:
        print temp
        data = temp['UserName']
        if Name in data:
            print "found"
        else:
            print "not found"
    # temp = pickle.loads(data)
    # wav.write("test.wav",44100,temp)
#
