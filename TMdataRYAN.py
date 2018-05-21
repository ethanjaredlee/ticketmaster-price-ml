import requests
import json
import datetime
from event import Event

apikey = 'sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o'
headers={'key':apikey}

endpoint = 'https://app.ticketmaster.eu/mfxapi/v1/'


par={u'name':'value1'}
resp=requests.get('https://app.ticketmaster.com/discovery/v2/events.json?size=20&keyword=post_malone&sort=relevance,desc&apikey=sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o',params=par)
response=resp.text
jsonresp = resp.json()
events = {}
for i in range(0,len(jsonresp.get(u'_embedded').get(u'events'))):
    show=Event()
    year=[]
    month=[]
    day=[]
    for j in range(0,len(jsonresp.get(u'_embedded').get(u'events')[i].get(u'dates').get(u'start').get(u'localDate'))):
        if j<=3:
            year.append(jsonresp.get(u'_embedded').get(u'events')[i].get(u'dates').get(u'start').get(u'localDate')[j])
        elif j>=5 and j<=6:
            month.append(jsonresp.get(u'_embedded').get(u'events')[i].get(u'dates').get(u'start').get(u'localDate')[j])
        elif j>7 and j<=9:
            day.append(jsonresp.get(u'_embedded').get(u'events')[i].get(u'dates').get(u'start').get(u'localDate')[j])

    dday = day[0]+ day[1]
    mmonth = month[0] + month[1]
    yyear = year[0] + year[1] + year[2] + year[3]
    d=datetime.date(int(yyear),int(mmonth),int(dday))
    eventdaynum=d.weekday()
    weekend=0
    if eventdaynum==0 or eventdaynum>=5:
        weekend=1
    eventcity=jsonresp.get(u'_embedded').get(u'events')[i].get(u'_embedded').get(u'venues')[0].get(u'city').get(u'name')
    eventvenue= jsonresp.get(u'_embedded').get(u'events')[i].get(u'_embedded').get(u'venues')[0].get(u'name')
    #pricerange=jsonresp.get(u'_embedded').get(u'events')[i].get(u'priceRanges')
    artistname=jsonresp.get(u'_embedded').get(u'events')[i].get(u'name')
    eventid= jsonresp.get(u'_embedded').get(u'events')[i].get(u'_embedded').get(u'attractions')[0].get(u'id')
    eventgenre= jsonresp.get(u'_embedded').get(u'events')[i].get(u'classifications')[0].get(u'genre').get(u'name')
    #print eventdaynum,eventid,eventgenre
    show.weekend=weekend
    show.artist=artistname
    show.month=mmonth
    show.genre=eventgenre
    show.venue=eventvenue
    show.city=eventcity
    events[eventid]=show
    print events
    print 'NEW EVENT!!''weekend:', show.weekend, 'artist:', show.artist, 'genre:', show.genre,'venue:',show.venue,'city:',show.city,'month:',show.month


with open('data.txt', 'w') as outfile:
    json.dump(jsonresp, outfile)
if resp.status_code != 200:
    print"error"
