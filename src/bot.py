from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TELEGRAM_TOKEN
from handlers.commands import song_command, artist_command, playlist_command

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("song", song_command))
    dispatcher.add_handler(CommandHandler("artist", artist_command))
    dispatcher.add_handler(CommandHandler("playlist", playlist_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()