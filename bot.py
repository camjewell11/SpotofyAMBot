# importing the necessary packages
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

sp = spotipy.Spotify()

# setting up authorization
cid = "2dd8ed6a41da4bc3b8ea4ce4bad4cc00"
secret = "8710800d6686483d91b1d475762f7f1c"

# saving the info you're going to need
username = '3bgf080jxet2k8roxm2qkibk2'
scope = 'user-library-read' #check the documentation
authorization_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
redirect_uri ='https://localhost.com/callback/'

token = util.prompt_for_user_token(username,scope,client_id='client_id_number',client_secret='client_secret',redirect_uri='https://localhost.com/callback/')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# retrieving you access token
auth = SpotifyClientCredentials(client_id= cid, client_secret=secret)

# save your token
token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)

# check if everything is in order
print(token)
print(spotify)

# this would be used by the spotipy client to find track name and artist from id (from URL)
trackID = "2shFsQSw0h1abkoK6zFF5w"
query = "https://api.spotify.com/v1/tracks/" + trackID

# queries client for URL from artist and track
artist = "shadow cliq"
track = "aerials"
q = "artist:" + artist + " track:" + track
results = sp.search(q=q, type='track', limit=5, market='US')