import requests
import json
import time

class DynamicText:
    def __init__(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1277333&APPID=37e4f15ede45e4d9abde1e7ee7ba441c')
        data = r.json()
        self.T = (data[u'main'][u'temp'] - 273.15)
        self.H = (time.strftime("%H"))
        self.M = (time.strftime("%M"))
        self.TI = (time.strftime("%H:%M"))
        self.dynamic_dict = { 'T':self.T, 'H':self.H, 'M':self.M,'TI':self.TI}

    def generateText(self,config):
        array = config.split(':')
        for word in array:
            print self.dynamic_dict[word]

if __name__ == '__main__':
    config = ("T:H:M:TI")
    obj = DynamicText()
    text = obj.generateText(config)
