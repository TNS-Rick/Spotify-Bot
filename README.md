# Spotify Telegram Bot

This project is a Telegram bot that allows users to search for songs, artists, and playlists on Spotify. Users can share or preview their favorite music directly in the chat.

## Features

- Search for songs, artists, and playlists on Spotify.
- Share links to Spotify content directly in Telegram.
- Preview available tracks within the chat.

## Requirements

- Python 3.7 or higher
- Telegram Bot API token
- Spotify API credentials

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/spotify-telegram-bot.git
   ```

2. Navigate to the project directory:

   ```
   cd spotify-telegram-bot
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Telegram bot token and Spotify API credentials. You can use the `.env.example` file as a reference.

## Usage

1. Run the bot:

   ```
   python src/bot.py
   ```

2. Interact with the bot in Telegram using the following commands:
   - `/song <song_name>`: Search for a song.
   - `/artist <artist_name>`: Search for an artist.
   - `/playlist <playlist_name>`: Search for a playlist.

## Testing

To run the tests, use the following command:

```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.