def handle_callback_query(update, context):
    query = update.callback_query
    query.answer()

    # Extract data from the callback query
    data = query.data

    # Handle different callback data
    if data.startswith('open_song_'):
        song_id = data.split('_')[2]
        # Logic to open the song in Spotify
        open_song_in_spotify(song_id, query)
    elif data.startswith('open_artist_'):
        artist_id = data.split('_')[2]
        # Logic to open the artist in Spotify
        open_artist_in_spotify(artist_id, query)
    elif data.startswith('open_playlist_'):
        playlist_id = data.split('_')[2]
        # Logic to open the playlist in Spotify
        open_playlist_in_spotify(playlist_id, query)
    else:
        query.edit_message_text(text="Unknown action.")

def open_song_in_spotify(song_id, query):
    # Logic to generate the Spotify link for the song
    spotify_link = f"https://open.spotify.com/track/{song_id}"
    query.edit_message_text(text=f"Open song: {spotify_link}")

def open_artist_in_spotify(artist_id, query):
    # Logic to generate the Spotify link for the artist
    spotify_link = f"https://open.spotify.com/artist/{artist_id}"
    query.edit_message_text(text=f"Open artist: {spotify_link}")

def open_playlist_in_spotify(playlist_id, query):
    # Logic to generate the Spotify link for the playlist
    spotify_link = f"https://open.spotify.com/playlist/{playlist_id}"
    query.edit_message_text(text=f"Open playlist: {spotify_link}")