import requests
import ipdb

from settings import ticketmaster_key, spotify_client_id, spotify_client_secret

def GetData():
  url = "https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey={}".format(ticketmaster_key)
  data = []

  while (len(data) < 200):
    r = requests.get(url)
    json = r.json()
    page = json['_embedded']['events']
    print json['page']['totalPages']
    print json['page']['number']

    for event in page:
      info = {}
      info['name'] = event['name']

      # check if the event is a music event or not
      try:
        attractions = event['_embedded']['attractions'][0]
      except KeyError:
        continue

      if attractions['classifications'][0]['segment']['name'] != "Music":
        continue
      
      maxMinPrice = priceParser(event['priceRanges'][0]) # probably don't want to index
      if maxMinPrice == None: # we don't want to0 deal with non-us currency
        continue
      info['max'] = maxMinPrice[0]
      info['min'] = maxMinPrice[1]

      info['promotorCount'] = len([p['name'] for p in event['promoters']]) # we just want to know how many promoters

      info['artist'] = attractions['name']
      # info['popularity'] = getArtistPopularity(info['artist'])

      data.append(info)
      print info

    # after we go through a page, we want the next one
    next = json['_links']['next']['href']
    url = "https://app.ticketmaster.com{}&apikey={}".format(next, ticketmaster_key)

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
  # print getArtistPopularity("Imagine Dragons")
  GetData()