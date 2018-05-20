import requests
import json
import datetime

apikey = 'sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o'
headers={'key':apikey}

endpoint = 'https://app.ticketmaster.eu/mfxapi/v1/'


par={u'name':'value1'}
resp=requests.get('https://app.ticketmaster.com/discovery/v2/events.json?size=20&keyword=post_malone&sort=relevance,desc&apikey=sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o',params=par)
response=resp.text
jsonresp = resp.json()
for i in range(0,len(jsonresp.get(u'_embedded').get(u'events'))):
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
    print d.weekday()
        #print jsonresp.get(u'_embedded').get(u'events')[i].get(u'dates').get(u'start').get(u'localDate')[j]


with open('data.txt', 'w') as outfile:
    json.dump(jsonresp, outfile)
if resp.status_code != 200:
    print"error"
