import requests
import json


def locator(city):
    link='https://public.opendatasoft.com/api/records/1.0/search/?dataset=1000-largest-us-cities-by-population-with-geographic-coordinates&q='+city+'&facet=city&facet=state'
    resp=requests.get(link).json()
    if len(resp.get(u'records'))==0:
        return '???'
    return resp.get(u'records')[0].get(u'fields').get(u'population')
