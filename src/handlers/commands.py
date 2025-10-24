from telegram import Update
from telegram.ext import CallbackContext
from services.spotify_client import SpotifyClient
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

from typing import List, Dict

spotify = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

def _format_duration(ms: int) -> str:
    if not ms:
        return ""
    s = ms // 1000
    m, s = divmod(s, 60)
    return f"{m}:{s:02d}"

def song_command(update: Update, context: CallbackContext):
    query = ' '.join(context.args) if context.args else ''
    if not query:
        update.message.reply_text("Usa /song <titolo> per cercare una canzone.")
        return
    try:
        tracks = spotify.search_tracks(query, limit=5)
    except Exception as e:
        update.message.reply_text("Errore nella ricerca su Spotify.")
        return

    if not tracks:
        update.message.reply_text("Nessun risultato per la ricerca.")
        return

    lines: List[str] = []
    for i, t in enumerate(tracks, start=1):
        artists = ", ".join(t.get("artists", [])) or "Unknown"
        name = t.get("name") or "Unknown"
        album = t.get("album") or ""
        duration = _format_duration(t.get("duration_ms") or 0)
        url = t.get("external_url") or ""
        preview = t.get("preview_url") or ""
        parts = [f"{i}. {name} — {artists}"]
        if album:
            parts.append(f"Album: {album}")
        if duration:
            parts.append(f"Durata: {duration}")
        if url:
            parts.append(f"Spotify: {url}")
        if preview:
            parts.append(f"Preview: {preview}")
        lines.append("\n".join(parts))

    update.message.reply_text("\n\n".join(lines))

def artist_command(update: Update, context: CallbackContext):
    query = ' '.join(context.args) if context.args else ''
    if not query:
        update.message.reply_text("Usa /artist <nome> per cercare un artista.")
        return
    try:
        artists = spotify.search_artists(query, limit=5)
    except Exception:
        update.message.reply_text("Errore nella ricerca su Spotify.")
        return

    if not artists:
        update.message.reply_text("Nessun artista trovato.")
        return

    lines = []
    for i, a in enumerate(artists, start=1):
        name = a.get("name") or "Unknown"
        genres = ", ".join(a.get("genres", [])) or "—"
        followers = a.get("followers")
        url = a.get("external_url") or ""
        lines.append(f"{i}. {name}\nGeneri: {genres}\nFollowers: {followers}\nSpotify: {url}")

    update.message.reply_text("\n\n".join(lines))

def playlist_command(update: Update, context: CallbackContext):
    query = ' '.join(context.args) if context.args else ''
    if not query:
        update.message.reply_text("Usa /playlist <nome> per cercare una playlist.")
        return
    try:
        playlists = spotify.search_playlists(query, limit=5)
    except Exception:
        update.message.reply_text("Errore nella ricerca su Spotify.")
        return

    if not playlists:
        update.message.reply_text("Nessuna playlist trovata.")
        return

    lines = []
    for i, p in enumerate(playlists, start=1):
        name = p.get("name") or "Unknown"
        owner = p.get("owner") or "Unknown"
        tracks_total = p.get("tracks_total") or 0
        url = p.get("external_url") or ""
        desc = p.get("description") or ""
        lines.append(f"{i}. {name} — {owner}\nTracce: {tracks_total}\n{desc}\nSpotify: {url}")

    update.message.reply_text("\n\n".join(lines))