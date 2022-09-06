import json, config
import tweepy as tw
import pandas as pd
import requests
from requests_oauthlib import OAuth1Session, OAuth1
import pprint
import openpyxl

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
BR = config.BEARER

URL = "https://api.twitter.com/2/users/1026814833272877057/timelines/reverse_chronological"

oauth = OAuth1Session(CK,CS,AT,ATS)


res = oauth.get(URL).json()

workbook = openpyxl.load_workbook('test.xlsx')
worksheet = workbook.worksheets[0]
for i in range(len(res["data"])):
    tweet = res["data"][i]["text"]
    worksheet.cell(row=i+1,column=1,value=tweet)
workbook.save('test.xlsx')
workbook.close()

#print(res["data"][0]["text"])

"""
for tweet in public_tweets:
    print(tweet)
"""

