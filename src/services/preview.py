def get_preview_url(track_id, spotify_client):
    track = spotify_client.get_track(track_id)
    if track and 'preview_url' in track and track['preview_url']:
        return track['preview_url']
    return None