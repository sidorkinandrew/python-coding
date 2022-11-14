import time
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from bs4 import BeautifulSoup
import requests

SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
REDIRECT_URL = "http://localhost:8888/callback"


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#date = '1995-07-07'
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_div = soup.find_all("div", class_="o-chart-results-list-row-container")
# print(len(song_names_div))
song_names = []
for entry in song_names_div:
     place = entry.findNext("span", ["c-label","a-font-primary-bold-l"]).getText().strip()
     title = entry.findNext("h3", "c-title")
     author = title.findNextSibling("span").getText().strip()
     title = title.getText().strip()
     # print(f"{place} - {title} - {author}")
     song_names.append(f"{author}, {title}")

# print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-library-read playlist-modify-private",
        redirect_uri=REDIRECT_URL,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=False,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

song_uris = []
year = date.split("-")[0]
not_found = []
for song in song_names:
    print(song, end=": ")
    result = sp.search(q=f"track:{song}", type="track", limit=2)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        not_found.append(song)
    time.sleep(0.125)

#print(song_uris)
print("Found", len(song_uris), "tracks.\nThese were reported as 'not found' by the API:\n")
print(not_found)


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Your private playlist '{date} Billboard 100' was created! Enjoy!")
