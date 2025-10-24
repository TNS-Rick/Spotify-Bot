from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Song:
    title: str
    artist: str
    album: str
    preview_url: Optional[str]

@dataclass
class Artist:
    name: str
    genres: List[str]
    popularity: int

@dataclass
class Playlist:
    name: str
    description: str
    tracks: List[Song]