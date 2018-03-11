'''
Class to write audio chunks into database
Author : Vasanthakumar N
Date   : 09 Mar 2018

Todo
Error handling, unit testing
'''

from pymongo import MongoClient

class ReadAudio:
    def __init__(self,db,collection,document,querylist):
        self.client = MongoClient('localhost',27017)
        self.db = self.client.db
        self.collection = self.db[collection]
        self.querylist = querylist

    # def read_data(self):


if __name__ == '__main__':
    obj = ReadAudio()
