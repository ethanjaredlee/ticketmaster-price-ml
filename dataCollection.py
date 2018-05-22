import requests
import ipdb

from settings import ticketmaster_key, spotify_client_id, spotify_client_secret

def GetData():
  url = "https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey={}".format(ticketmaster_key)

  r = requests.get(url)
  json = r.json()
  page = json['_embedded']['events']

  data = []
  for event in page:
    info = {}
    info['name'] = event['name']

    
    maxMinPrice = priceParser(event['priceRanges'][0]) # probably don't want to index
    info['max'] = maxMinPrice[0]
    info['min'] = maxMinPrice[1]
    info['promotorCount'] = len([p['name'] for p in event['promoters']]) # we just want to know how many promoters
    info['imageCount'] = len(event['images'])

    _embedded = event['_embedded']
    info['artist'] = _embedded['attractions'][0]['name'] # prob shouldnt do this either
    info['popularity'] = getArtistPopularity(info['artist'])

    data.append(info)
    print info

def priceParser(priceRangeObject):
  if priceRangeObject['currency'] != 'USD':
    # we only want to handle us currency - could improve this to handle conversion rates
    # but this doesn't seenm worth it
    return None

  return (priceRangeObject['max'], priceRangeObject['min'])

def getArtistPopularity(artist):
  formattedArtist = artist.replace(" ", "%20")

  body = {"grant_type": "client_credentials"}

  tokenURL = "https://accounts.spotify.com/api/token"
  token = requests.post(tokenURL, data=body, auth=(spotify_client_id, spotify_client_secret))
  tJSON = token.json()

  header = {"Authorization": "Bearer " + tJSON['access_token']}

  searchURL = "https://api.spotify.com/v1/search?q={}&type=artist".format(formattedArtist)
  r = requests.get(searchURL, headers=header)
  artistInfo = r.json()
  popularity = artistInfo['artists']['items'][0]['popularity']
  return popularity




if __name__ == "__main__":
  print getArtistPopularity("Drake")