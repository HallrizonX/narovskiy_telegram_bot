from telegram.ext import CommandHandler, MessageHandler, Filters

# Імпортуємо функціх команд
from commands.textMessage import textMessage
from commands.startCommand import startCommand

commands = (
    CommandHandler('start', startCommand),
    MessageHandler(Filters.text, textMessage),
)
