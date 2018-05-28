import requests
import json

def prices(id):
    key={"sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o"}
    link='https://app.ticketmaster.com/commerce/v2/events/' + id + '/offers'+'.json?{sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o'+'}'
    print link
    resp=requests.get(link)
    jsonresp = resp.json()
    return jsonresp
