from services.spotify_client import SpotifyClient
from utils.helpers import format_search_results

def search(query, search_type):
    client = SpotifyClient()
    if search_type == 'track':
        results = client.search_tracks(query)
    elif search_type == 'artist':
        results = client.search_artists(query)
    elif search_type == 'playlist':
        results = client.search_playlists(query)
    else:
        return "Invalid search type. Please use 'track', 'artist', or 'playlist'."

    formatted_results = format_search_results(results)
    return formatted_results