'''
Server class, establishes connection with client via Sockets
Author : Vasanthakumar N
Date   : 16 Mar 2018

Todo
Error handling, unit testing, cleaning code,interface with other classes
'''

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import numpy
import scipy.io.wavfile as wav
import sys
# first_message = True
# print first_message
# comp_audio = []
comp_audio = numpy.ndarray(shape=(1,),dtype='int32')
# total_msg =100
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        comp_audio = []

    def on_message(self, message):
        if message != 'terminate':
            global comp_audio
            print type(message)
            # print message
            audio = numpy.frombuffer(message,dtype='int32')
            print type(audio)
            comp_audio = numpy.append(comp_audio, audio)
        else:
            print "end of recording"
            # scaled = numpy.int16(comp_audio/numpy.max(numpy.abs(comp_audio)) * 32767)
            wav.write("testaudio1.wav",44100,comp_audio)
            comp_audio = []
            print "written"
            self.close()

    def on_close(self):
        print 'connection closed'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8889)
    myIP = socket.gethostbyname(socket.gethostname())
    print 'Websocket Server Started at %s' % myIP
    tornado.ioloop.IOLoop.instance().start()
