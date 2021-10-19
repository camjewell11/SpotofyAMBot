# importing the necessary packages
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

sp = spotipy.Spotify()

# setting up authorization
cid = "2dd8ed6a41da4bc3b8ea4ce4bad4cc00"
secret = "8710800d6686483d91b1d475762f7f1c"

# saving the info you're going to need
username = 'your_account_number'
scope = 'user-library-read' #check the documentation
authorization_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
redirect_uri ='https://localhost.com/callback/'

token = util.prompt_for_user_token(username,scope,client_id='client_id_number',client_secret='client_secret',redirect_uri='https://localhost.com/callback/')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)