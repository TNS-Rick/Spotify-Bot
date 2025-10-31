from telegram import Update  # import per i tipi/update di telegram
from telegram.ext import CallbackContext  # import per il contesto dei handler
from services.spotify_client import SpotifyClient  # client per chiamare l'API Spotify
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET  # credenziali caricate da .env

from typing import List, Dict  # tipi usati per annotazioni

# istanzia un client Spotify condiviso usando le variabili di configurazione
spotify = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

def _format_duration(ms: int) -> str:
    # Riceve una durata in millisecondi e la formatta come M:SS
    # Se ms è falsy (es. 0 o None) ritorna stringa vuota.
    if not ms:
        return ""
    s = ms // 1000  # converte in secondi interi
    m, s = divmod(s, 60)  # ottiene minuti e secondi rimanenti
    return f"{m}:{s:02d}"  # formatta con due cifre per i secondi

def song_command(update: Update, context: CallbackContext):
    # Handler per il comando /song: costruisce la query dai token passati
    query = ' '.join(context.args) if context.args else ''
    if not query:
        # Messaggio informativo se l'utente non fornisce argomenti
        update.message.reply_text("Usa /song <titolo> per cercare una canzone.")
        return
    try:
        # Esegue la ricerca di tracce su Spotify (limite 5)
        tracks = spotify.search_tracks(query, limit=5)
    except Exception as e:
        # In caso di errore nell'API risponde con messaggio generico
        update.message.reply_text("Errore nella ricerca su Spotify.")
        return

    if not tracks:
        # Nessun risultato trovato
        update.message.reply_text("Nessun risultato per la ricerca.")
        return

    # Costruisce il testo di risposta unendo le informazioni utili di ogni traccia
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

    # Invia il messaggio con i risultati formattati
    update.message.reply_text("\n\n".join(lines))

def artist_command(update: Update, context: CallbackContext):
    # Handler per il comando /artist: cerca artisti
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

    # Costruisce la lista di risultati per gli artisti
    lines = []
    for i, a in enumerate(artists, start=1):
        name = a.get("name") or "Unknown"
        genres = ", ".join(a.get("genres", [])) or "—"
        followers = a.get("followers")
        url = a.get("external_url") or ""
        lines.append(f"{i}. {name}\nGeneri: {genres}\nFollowers: {followers}\nSpotify: {url}")

    update.message.reply_text("\n\n".join(lines))

def playlist_command(update: Update, context: CallbackContext):
    # Handler per il comando /playlist: cerca playlist
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

    # Costruisce la lista di risultati per le playlist
    lines = []
    for i, p in enumerate(playlists, start=1):
        name = p.get("name") or "Unknown"
        owner = p.get("owner") or "Unknown"
        tracks_total = p.get("tracks_total") or 0
        url = p.get("external_url") or ""
        desc = p.get("description") or ""
        lines.append(f"{i}. {name} — {owner}\nTracce: {tracks_total}\n{desc}\nSpotify: {url}")

    update.message.reply_text("\n\n".join(lines))