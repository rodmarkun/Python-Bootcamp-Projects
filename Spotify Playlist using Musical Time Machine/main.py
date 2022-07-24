import argparse
import requests
import os
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = os.environ.get("API_SPOTIFY_CLIENTID")
SPOTIFY_CLIENT_SECRET = os.environ.get("API_SPOTIFY_CLIENTSECRET")
REDIRECT_URI = "http://example.com"

scope = "playlist-modify-private"

def main():
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
    webpage = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/").text

    soup = BeautifulSoup(webpage, "html.parser")
    tags = soup.select(selector="li #title-of-a-story")

    titles = [title.getText().strip() for title in tags]
    print(titles)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))
    url_list = []
    for title in titles:
        try:
            result = sp.search(f"track: {title} year: {date[0:4]}")
            url_list.append(result['tracks']['items'][0]['external_urls']['spotify'])
        except:
            print(f'Could not find {title} in Spotify')

    user_id = sp.current_user()['id']
    playlist_name = f"{date} Billboard 100"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    sp.playlist_add_items(playlist_id=playlist['id'], items=url_list)

if __name__ == '__main__':
    main()