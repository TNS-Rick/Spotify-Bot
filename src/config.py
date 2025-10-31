# Caricamento variabili d'ambiente da .env nella root del progetto.
import os
from pathlib import Path
from dotenv import load_dotenv

# carica .env dalla root del progetto
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

# Variabili di configurazione esposte al resto del progetto
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")