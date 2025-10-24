def format_song_message(song):
    return f"🎵 *{song['name']}* by *{', '.join(song['artists'])}*\n[Listen on Spotify]({song['url']})"

def format_artist_message(artist):
    return f"🎤 *{artist['name']}*\n[Listen on Spotify]({artist['url']})"

def format_playlist_message(playlist):
    return f"📋 *{playlist['name']}*\n[Listen on Spotify]({playlist['url']})"

def format_error_message(error):
    return f"⚠️ *Error:* {error}"