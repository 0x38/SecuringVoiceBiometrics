import re
import time
import requests

class ContentValidation:
    def __init__(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1277333&APPID=37e4f15ede45e4d9abde1e7ee7ba441c')
        data = r.json()
        # print "_________________________________"
        # print "content val"
        # print data
        self.T = data[u'main'][u'temp'] - 273.15
        self.H = time.strftime("%I")
        print type(self.H)
        self.H = int(self.H) * 1
        print self.H
        self.M = time.strftime("%M")
        # self.M = 0
        self.A = time.strftime("%p")
        print "System's Temparature"
        print self.T
        # print type(self.T)

    def validateContent(self,transcript,config):
        array = config.split(':')
        timematch = 1;
        datematch = 1;
        tempmatch = 1;
        for word in array:
            if word == "Time":
                usertime = re.findall(r'(\d{1,2}:?\d{1,2}\ [aApP]\.[mM]\.)', transcript)

                if self.M == 0:
                    systemtime = str(self.H)+" "
                else:
                    systemtime = str(self.H)+":"+str(self.M)+" "

                if self.A == "AM":
                    systemtime = systemtime + "a.m."
                elif self.A == "PM":
                    systemtime = systemtime + "p.m."
                print ("System time" + systemtime)
                if usertime == []:
                    print "No data"
                    timematch = 0;
                else:
                    if usertime[0] == systemtime:
                        print "Time match"
                        timematch = 1;
                    else:
                        print "Time no match"
                        timematch = 0;

            elif word == "Date":
                print "date"

            elif word == "Temp":
                usertemp = re.findall(r'(\d{1,2}\.?\d{1,2}?\ [dD][eE][gG].*\ )', transcript)
                if usertemp == []:
                    print "No data"
                    tempmatch = 0;
                else:
                    usertemp = str(usertemp[0])
                    temp = usertemp.split(' ')
                    temp[0] = float(temp[0])
                    if int(temp[0]) == int(self.T):
                        print "Temp match"
                        tempmatch = 1;
                    else:
                        print "Temp no match"
                        tempmatch = 0;
                # temp = usertemp.split(' ')
                # if user temp[0]

                # print usertemp
                return tempmatch * timematch * tempmatch;


if __name__ == '__main__':
    obj = ContentValidation()
    transcript = "transcript: \"Time and Tide waits for none the time is 12:23 p.m. and the weather is 31.46 degrees Celsius\""
    print obj.validateContent(transcript,"Time:Temp:")



# import requests
# import json
# import time
#
# class DynamicText:
#     def __init__(self):
#         r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1277333&APPID=37e4f15ede45e4d9abde1e7ee7ba441c')
#         data = r.json()
#         self.T = (data[u'main'][u'temp'] - 273.15)
#         self.H = (time.strftime("%H"))
#         self.M = (time.strftime("%M"))
#         self.TI = (time.strftime("%H:%M"))
#         self.dynamic_dict = { 'T':self.T, 'H':self.H, 'M':self.M,'TI':self.TI}
#
#     def generateText(self,config):
#         array = config.split(':')
#         for word in array:
#             print self.dynamic_dict[word]
#
# if __name__ == '__main__':
#     config = ("T:H:M:TI")
#     obj = DynamicText()
#     text = obj.generateText(config)
