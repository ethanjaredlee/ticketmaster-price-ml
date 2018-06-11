import requests
import json

def prices(id):
    key="sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o"
    Request_Params={
    'apikey':key
    }
    link='https://app.ticketmaster.com/commerce/v2/events/' + id + '/offers'+'.json?{apikey' + '}'
    resp=requests.get(url=link,params=Request_Params)
    jsonresp = resp.json()
    return jsonresp
