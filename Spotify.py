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
token_url = 'https://accounts.spotify.com/authorize?client_id=client_id_number&response_type=code&redirect_uri=https%3A%2F%2Flocalhost.com%2Fcallback%2F&scope=user-library-read'
redirect_uri ='https://accounts.spotify.com/authorize?client_id=client_id_number&response_type=code&redirect_uri=https%3A%2F%2Flocalhost.com%2Fcallback%2F&scope=user-library-read'

def getClient():
    # token = "BQDZnXnyMHMs0eVrRq6m1-jsx7Zm6qk3NmC-VvqCYQxUHC9-1gGlXP8f7Y41GCcPXbKWu9Pgc0upYQGBWiCjHlpHnzbmxwJYtvdIgSM9Fnq1uRvjNIi0thXEBRGN_qQlopgWIn_u6diQ3L0Z-JljaMTfN77Gv1YuvWqOC68eaHrpkb3O"
    # token = util.prompt_for_user_token(username,scope,client_id='client_id_number',client_secret='client_secret',redirect_uri='https://localhost.com/callback/')
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

    return sp

# used by the spotipy client to find URL from id from track name and artist
def queryForURL(sp, artist, track):
    # queries client for URL from artist and track
    q = "artist:" + artist + " track:" + track
    results = sp.search(q=q, type='track', limit=5, market='US')

    URL = results["tracks"]["items"][0]["external_urls"]["spotify"]

    return URL

# used by spotipy client to find artist and track from id
def queryForTrackData(id):
    result = sp.tracks(id)

    artist = result["album"]["artists"][0]["name"]
    track  = result["album"]["name"]

    return artist, track