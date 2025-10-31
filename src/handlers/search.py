# Wrapper semplice che usa SpotifyClient per eseguire ricerche e formatta i risultati.
from services.spotify_client import SpotifyClient
from utils.helpers import format_search_results

def search(query, search_type):
    # Instanzia un client e seleziona il tipo di ricerca
    client = SpotifyClient()
    if search_type == 'track':
        results = client.search_tracks(query)
    elif search_type == 'artist':
        results = client.search_artists(query)
    elif search_type == 'playlist':
        results = client.search_playlists(query)
    else:
        return "Invalid search type. Please use 'track', 'artist', or 'playlist'."

    # Usa helper per formattare i risultati (atteso che format_search_results esista in utils.helpers)
    formatted_results = format_search_results(results)
    return formatted_results