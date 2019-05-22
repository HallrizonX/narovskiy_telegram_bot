from telegram.ext import Updater
from commands import commands


class MainHandler:
    __slots__ = ['updater', 'dispatcher']

    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

        self._add_handlers()

    def _add_handlers(self):
        for handler in commands:
            self.add_handler(handler)

    def add_handler(self, command):
        self.dispatcher.add_handler(command)

    def run(self):
        # Починаємо пошук оновлень
        self.updater.start_polling(clean=True)
        # Зупиняємо бота якщо було натиснуто Ctrl + C
        self.updater.idle()
