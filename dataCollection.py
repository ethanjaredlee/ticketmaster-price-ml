import requests

from settings import ticketmaster_key, spotify_client_id, spotify_client_secret

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
