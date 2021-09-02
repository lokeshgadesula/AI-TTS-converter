import JarvisAI
import re

obj = JarvisAI.JarvisAssistant()

def t2s(text):
    obj.text2speech(text)

while True :
    res = obj.mic_input()
    if re.search('weather|tempareture', res):
        city = res.split (' ')[-1]
        weather_res = obj.weather(city= city)
    print(weather_res)
    t2s(weather_res)