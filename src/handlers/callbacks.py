# Handler per callback_query di Telegram (pulsanti inline).
def handle_callback_query(update, context):
    # Risponde al callback e processa il payload data
    query = update.callback_query
    query.answer()

    # Estrae i dati inviati dal bottone
    data = query.data

    # Gestisce azioni diverse in base al prefisso della data
    if data.startswith('open_song_'):
        song_id = data.split('_')[2]
        # Logica per aprire brano in Spotify
        open_song_in_spotify(song_id, query)
    elif data.startswith('open_artist_'):
        artist_id = data.split('_')[2]
        # Logica per aprire artista in Spotify
        open_artist_in_spotify(artist_id, query)
    elif data.startswith('open_playlist_'):
        playlist_id = data.split('_')[2]
        # Logica per aprire playlist in Spotify
        open_playlist_in_spotify(playlist_id, query)
    else:
        query.edit_message_text(text="Unknown action.")

def open_song_in_spotify(song_id, query):
    # Genera link open.spotify per la traccia
    spotify_link = f"https://open.spotify.com/track/{song_id}"
    query.edit_message_text(text=f"Open song: {spotify_link}")

def open_artist_in_spotify(artist_id, query):
    # Genera link open.spotify per l'artista
    spotify_link = f"https://open.spotify.com/artist/{artist_id}"
    query.edit_message_text(text=f"Open artist: {spotify_link}")

def open_playlist_in_spotify(playlist_id, query):
    # Genera link open.spotify per la playlist
    spotify_link = f"https://open.spotify.com/playlist/{playlist_id}"
    query.edit_message_text(text=f"Open playlist: {spotify_link}")