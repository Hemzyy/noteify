from instagrapi import Client

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

import os, sys
import json
from dotenv import load_dotenv


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print('Usage %s Username ' % (sys.argv[0],))
    sys.exit()


#get environment variables
load_dotenv()
spotify_client_id = os.getenv('SPOTIPY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
spotify_redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

accountUsername = os.getenv('ACCOUNT_USERNAME')
accountPassword = os.getenv('ACCOUNT_PASSWORD')

scope = 'user-read-currently-playing'

oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri=spotify_redirect_uri, scope=scope)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

if token:
    spotify_object = spotipy.Spotify(auth=token)
    current_song = spotify_object.currently_playing()
else:
    print("Can't get token for", username)
    sys.exit()

#print(json.dumps(current_song, sort_keys=False, indent=4))
artist_name = current_song['item']['artists'][0]['name']
song_title = current_song['item']['name']

status = "Listening to: " + artist_name + " - " + song_title
print("Listening to: " + artist_name + " - " + song_title)


cl = Client()
cl.login(accountUsername, accountPassword)
cl.send_note(status, 1)

while(True):
    #if song changes, update status
    curr = spotify_object.currently_playing()
    if(curr['item']['name'] != song_title):
        song_title = curr['item']['name']
        artist_name = curr['item']['artists'][0]['name']
        status = "Listening to: " + artist_name + " - " + song_title
        print("Listening to: " + artist_name + " - " + song_title)
        cl.send_note(status, 1)
        print("Status updated")


