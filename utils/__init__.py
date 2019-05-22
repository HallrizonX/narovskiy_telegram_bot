import logging


class Logging:
    def __init__(self):
        logging.basicConfig(filename='telegram-bot.log', filemode='w',
                            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

        self.logging = logging


log = Logging()
