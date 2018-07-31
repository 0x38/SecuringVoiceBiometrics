import requests
import json
import time
# class CurrentStat
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1277333&APPID=37e4f15ede45e4d9abde1e7ee7ba441c')
data = r.json()
temp = (data[u'main'][u'temp'] - 273.15)
hour = (time.strftime("%H"))
minute = (time.strftime("%M"))
hourmin = (time.strftime("%H:%M"))
ampm = (time.strftime("%p"))


print temp
print hour
print minute
print hourmin
print ampm
