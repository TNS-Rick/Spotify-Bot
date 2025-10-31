# Funzioni helper per formattare messaggi Telegram in markdown/MarkdownV2 stile.
def format_song_message(song):
    # Restituisce una stringa formattata per una traccia
    return f"🎵 *{song['name']}* by *{', '.join(song['artists'])}*\n[Listen on Spotify]({song['url']})"

def format_artist_message(artist):
    # Restituisce una stringa formattata per un artista
    return f"🎤 *{artist['name']}*\n[Listen on Spotify]({artist['url']})"

def format_playlist_message(playlist):
    # Restituisce una stringa formattata per una playlist
    return f"📋 *{playlist['name']}*\n[Listen on Spotify]({playlist['url']})"

def format_error_message(error):
    # Messaggio di errore formattato
    return f"⚠️ *Error:* {error}"