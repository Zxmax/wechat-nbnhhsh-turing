# encoding:utf-8

from wxpy import *
from selenium import webdriver
from time import sleep
import json
import requests

url = 'https://lab.magiconch.com/api/nbnhhsh/'

def returnReplyTR(Msg):
    url2 = "http://openapi.tuling123.com/openapi/api/v2"  
    api_key="yourkey"  
    payload={
	    "reqType":0,
        "perception": {
            "inputText": {
                "text": Msg
            }
        },
        "userInfo": {
            "apiKey": api_key,
            "userId": "1"
        }
    }
    r = requests.post(url2,data=json.dumps(payload)).json()
    return (r['results'][0]['values']['text'])


bot = Bot(cache_path=True)
myself=bot.self
fileHelper=bot.file_helper
#需要活跃的群，如果编译出错，在群里发一句话就可以通过
ZJUT=bot.groups().search('groupName')[0]


@bot.register(ZJUT, TEXT)
def auto_reply1(msg):
    print(msg.text)
    if("缩写" in msg.text):
        msg=msg.text.replace("(Text)",'')
        msg=msg.replace("缩写",'')
        data = {"text": msg}
        req = requests.post(url+'guess',json=data)
        print(req.text[req.text.rfind('"trans":'):-2])
        return req.text[req.text.rfind('"trans":')+8:-2]
    if msg.is_at:
        msg=msg.text.replace("@Zxmax ",'')
        rMsg=returnReplyTR(msg)
        print(rMsg)
        return rMsg


embed()
