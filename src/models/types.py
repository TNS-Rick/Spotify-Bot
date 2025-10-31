# Tipi dati semplici usando dataclass per rappresentare entità del dominio.
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Song:
    # Rappresentazione minimale di una canzone
    title: str
    artist: str
    album: str
    preview_url: Optional[str]

@dataclass
class Artist:
    # Rappresentazione minimale di un artista
    name: str
    genres: List[str]
    popularity: int

@dataclass
class Playlist:
    # Rappresentazione minimale di una playlist
    name: str
    description: str
    tracks: List[Song]