import requests
import ipdb

from settings import ticketmaster_key

url = "https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey=" + ticketmaster_key

r = requests.get(url)
json = r.json()
page = json['_embedded']['events']

data = []
for event in page:
  info = {}
  info['name'] = event['name']

  maxMinPrice = event['priceRanges']
  info['max'] = maxMinPrice[0]
  info['min'] = maxMinPrice[1]
  info['promotorCount'] = len([p['name'] for p in event['promoters']]) # we just want to know how many promoters
  info['location'] = event['location'] # long/lat
  info['imageCount'] = len(event['images'])
  info['artist'] = event[]

  data.append(info)

def priceParser(priceRangeObject):
  if priceRangeObject['currency'] != 'USD':
    # we only want to handle us currency - could improve this to handle conversion rates
    # but this doesn't seenm worth it
    return None

  return (priceRangeObject['max'], priceRangeObject['min'])