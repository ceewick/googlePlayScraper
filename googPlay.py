#!/usr/bin/env python

import requests
from bs4 import  BeautifulSoup
import pandas as pd
from urllib.request import urlopen


head = {"User-Agent":"Mozilla/5.0  (Macintosh; Intel   Mac OS\
            X   10_9_5) AppleWebKit 537.36  (KHTML, like    Gecko)\
              Chrome","Accept":"text/html,application/xhtml+xml,\
              application/xmlq=0.9,image/webp,*/*;q=0.8"}

def soup(url,ext,headers):
    ''' url = glassdoor.com exten='/Reviews/Brierley-and-Partners-Reviews-E9540.htm'''
    session = requests.Session()
    address = url+ext
    req = session.get(address, headers=headers)
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs

url = 'https://play.google.com/store/apps'
exten = '/collection/topselling_free'
bsFree = soup(url,exten,head)

title = bsFree.h2.text

chart = bsFree.find('div',{'class','id-card-list card-list two-cards'})
for app in chart.findAll('div',{'class',
                        'card no-rationale square-cover apps small'}):

        tit = app.find('a',{'class','title'}).text.split('.')
        title = tit[1].strip()
        rank = tit[0].strip()

        rate = app.find('div',{'class','current-rating'})
        rating = rate['style'].split()
        percentRating = rating[1][:7]

        #attr sjsname="jIIjq" style="width: 80.88788032531738%;"></div>)
