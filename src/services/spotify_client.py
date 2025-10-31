# Client HTTP minimale per usare le API Web di Spotify con Client Credentials flow.
import time
import base64
from typing import List, Dict, Optional
import requests


class SpotifyClient:
    # URL per ottenere token e per le ricerche
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    SEARCH_URL = "https://api.spotify.com/v1/search"

    def __init__(self, client_id: str, client_secret: str):
        # Conserva credenziali e stato del token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token: Optional[str] = None
        self._token_expires_at: float = 0.0

    def authenticate(self, force: bool = False) -> str:
        """Fetch an access token using Client Credentials flow.
        Caches token fino alla scadenza e lo restituisce.
        """
        # Se token valido e non forzato, riusa
        if not force and self.access_token and time.time() < self._token_expires_at:
            return self.access_token

        # Prepara header Basic e corpo form data
        auth_header = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        headers = {"Authorization": f"Basic {auth_header}", "Content-Type": "application/x-www-form-urlencoded"}
        data = {"grant_type": "client_credentials"}

        # Richiesta al server token
        resp = requests.post(self.TOKEN_URL, headers=headers, data=data, timeout=10)
        resp.raise_for_status()
        payload = resp.json()
        token = payload.get("access_token")
        expires_in = int(payload.get("expires_in", 3600))

        if not token:
            raise RuntimeError("Failed to obtain Spotify access token")

        # Memorizza token con piccolo buffer sulla scadenza
        self.access_token = token
        self._token_expires_at = time.time() + expires_in - 30
        return self.access_token

    def _get_headers(self) -> Dict[str, str]:
        # Recupera header Authorization con token valido
        token = self.authenticate()
        return {"Authorization": f"Bearer {token}"}

    def _search(self, query: str, types: str, limit: int = 5) -> Dict:
        # Esegue una chiamata GET al endpoint di ricerca
        params = {"q": query, "type": types, "limit": limit}
        headers = self._get_headers()
        resp = requests.get(self.SEARCH_URL, headers=headers, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def search_tracks(self, query: str, limit: int = 5) -> List[Dict]:
        """Ritorna lista semplificata di tracce per la query."""
        if not query:
            return []
        data = self._search(query, "track", limit=limit)
        items = data.get("tracks", {}).get("items", [])
        results = []
        for t in items:
            # Estrae campi utili dalla struttura complessa dell'API Spotify
            results.append({
                "id": t.get("id"),
                "name": t.get("name"),
                "artists": [a.get("name") for a in t.get("artists", [])],
                "album": t.get("album", {}).get("name"),
                "preview_url": t.get("preview_url"),
                "external_url": t.get("external_urls", {}).get("spotify"),
                "duration_ms": t.get("duration_ms"),
            })
        return results

    def search_artists(self, query: str, limit: int = 5) -> List[Dict]:
        """Ritorna lista semplificata di artisti per la query."""
        if not query:
            return []
        data = self._search(query, "artist", limit=limit)
        items = data.get("artists", {}).get("items", [])
        results = []
        for a in items:
            results.append({
                "id": a.get("id"),
                "name": a.get("name"),
                "genres": a.get("genres", []),
                "followers": a.get("followers", {}).get("total"),
                "external_url": a.get("external_urls", {}).get("spotify"),
                "images": a.get("images", []),
            })
        return results

    def search_playlists(self, query: str, limit: int = 5) -> List[Dict]:
        """Ritorna lista semplificata di playlist per la query."""
        if not query:
            return []
        data = self._search(query, "playlist", limit=limit)
        items = data.get("playlists", {}).get("items", [])
        results = []
        for p in items:
            results.append({
                "id": p.get("id"),
                "name": p.get("name"),
                "owner": p.get("owner", {}).get("display_name"),
                "tracks_total": p.get("tracks", {}).get("total"),
                "external_url": p.get("external_urls", {}).get("spotify"),
                "description": p.get("description"),
                "images": p.get("images", []),
            })
        return results

    def get_access_token(self) -> Optional[str]:
        # Restituisce token memorizzato (potrebbe essere None)
        return self.access_token

    def refresh_access_token(self) -> str:
        # Forza il refresh del token
        return self.authenticate(force=True)