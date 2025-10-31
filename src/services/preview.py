# Funzione helper per ottenere l'URL di preview di una traccia usando il client Spotify.
def get_preview_url(track_id, spotify_client):
    # Richiede il dettaglio della traccia e ritorna preview_url se presente
    track = spotify_client.get_track(track_id)
    if track and 'preview_url' in track and track['preview_url']:
        return track['preview_url']
    return None