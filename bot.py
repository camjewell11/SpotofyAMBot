import Spotify

spotifyClient = Spotify.getClient()
# trackID = "2shFsQSw0h1abkoK6zFF5w"
# query = "https://api.spotify.com/v1/tracks/" + trackID
Spotify.queryForTrackData("2shFsQSw0h1abkoK6zFF5w")
Spotify.queryForURL(spotifyClient, "shadow cliq", "aerials")