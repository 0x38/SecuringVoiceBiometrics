'''
Server class, establishes connection with client via Sockets
Author : Vasanthakumar N
Date   : 16 Mar 2018

Todo
Error handling, unit testing, cleaning code,interface with other classes
db.UserConfiguration.insert_one({"Name":"Vasanth","Configuration":data}) //data should be evaluated

'''

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import numpy
import scipy.io.wavfile as wav
import sys
import json
import time
from bson.binary import Binary
import pickle
import re

from readDB import ReadAudio
from WriteDB import WriteAudio
from feature import Features
from model_compare import CompareModel
from speech import SpeechtoText
from contentval import ContentValidation


comp_audio = numpy.ndarray(shape=(1,),dtype='int32')
comp_dynamicaudio = numpy.ndarray(shape=(1,),dtype='int32')

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'

    def on_message(self,message):
        global comp_audio
        global comp_dynamicaudio
        global userName
        global userConfig
        message = json.loads(message)
        # message = json.loads(yaml.load(json.dumps(message)))
        if message['Category'] == 'UserName':
            prepared_query = [0,'find()']
            obj = ReadAudio('sbSVB','UserNames',prepared_query)
            cursor = obj.read_data()
            print cursor
            for temp in cursor:
                data = temp['UserName']
                print data
                if message['Content']['Name'] in data:
                    print "Existing User"
                    userName = message['Content']['Name']
                    userConfig = message['Content']['Config']
                    # Throw User name exist exception and quit function
                    self.write_message(u'{"Category":"UserName","Content":"Exist","Status":1}')
                    del obj
                    return
                else:
                    # Proceed further sampleRat
                    print "User Doesn't exist"
                    self.write_message(u'{"Category":"UserName","Content":"NotExist","Status":0}')
                    userName = message['Content']['Name']
                    userConfig = message['Content']['Config']
                    del obj
                    return

        elif message["Category"] == "LoginAudio":
            audio = numpy.asarray(message["Content"],dtype='int32')
            comp_audio = numpy.append(comp_audio, audio)
        elif message["Category"] == "LoginAudioTer":
            syscont = ContentValidation()
            print "syscont Created"
            feat_obj = Features()
            wav.write("statictemp.wav",44100,comp_audio)
            user_model = feat_obj.featureList("statictemp.wav")

            prepared_query = [0,'find_one({\'Name\':\''+userName+'\'})']
            obj = ReadAudio('sbSVB','VoiceModels',prepared_query)
            templateModel = pickle.loads(obj.read_data()['Model'])

            obj = CompareModel()
            print "CompareModel created"
            dist,steps = obj.compare(templateModel,user_model)
            comp_audio = numpy.zeros(shape=(1,),dtype='int32')

            prepared_query = [0,'find_one({\'Name\':\''+userName+'\'})']
            obj = ReadAudio('sbSVB','UserConfiguration',prepared_query)
            config = obj.read_data()['Configuration']
            print "Config read"
            spobj = SpeechtoText("statictemp.wav")
            transcript = spobj.speechtotext()
            print "Trascript obtained"
            contentvalid = syscont.validateContent(transcript,config)
            print "Content Validated"
            if contentvalid == 1 and dist/(steps/1000000) < 1000:
                print "Valid User"
                self.write_message(u'{"Category":"Validation","Content":"Valid","Status":1}')
            else:
                print "Invalid User"
                self.write_message(u'{"Category":"Validation","Content":"NotValid","Status":0}')
            print "Status returned"
            # usertime = re.findall(r'(\d{1,2}:?\d{1,2}\ [aApP]\.[mM]\.)', transcript)
            print transcript
            print dist
            print steps
            return

        # elif message["Category"] == "userConfig":
        #     userConfig = message['Content']

        elif message["Category"] == "dynamicAudio":
            audio = numpy.asarray(message["Content"],dtype='int32')
            comp_dynamicaudio = numpy.append(comp_dynamicaudio, audio)
        elif message["Category"] == "dynamicAudioTer":
            print "dynamic audio recieved"
            feat_obj = Features()
            wav.write("dynamictem.wav",44100,comp_dynamicaudio)
            user_model = feat_obj.featureList("dynamictemp.wav")
            user_model_blob = Binary(pickle.dumps(user_model,protocol=2))
            print "user model:"
            print user_model
            print user_model.shape
            # print "user model blob:"
            # print user_model_blob
            # print user_model_blob.shape
            prepared_query = [0,'insert_one({\"Name\":\"'+userName+'\",\"Model\":data})']
            obj = WriteAudio('sbSVB','VoiceModels',prepared_query)
            obj.update_users(userName)
            obj.write_data(user_model_blob)
            del obj
            prepared_query = [0,'insert_one({\"Name\":\"'+userName+'\",\"Configuration\":data})']
            obj = WriteAudio('sbSVB','UserConfiguration',prepared_query)
            obj.write_data(userConfig);
            comp_dynamicaudio = numpy.zeros(shape=(1,),dtype='int32')

            return



        # elif message["Category"] == "staticAudio":
        #     audio = numpy.asarray(message["Content"],dtype='int32')
        #     comp_dynamicaudio = numpy.append(comp_audio, audio)
        # elif message["Category"] == "staticAudioTer":
        #     print "static audio recieved"


        # if message == 'ping':
        #     self.write_message('Connection alive')
        # print message['Content']
        # print message

    def on_close(self):
        print 'connection closed'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print 'Websocket Server Started at %s' % myIP
    tornado.ioloop.IOLoop.instance().start()
