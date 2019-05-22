import apiai
import json
from settings import GOOGLE_CLIENT_ACCESS
from utils import log

def textMessage(bot, update):
    request = apiai.ApiAI(GOOGLE_CLIENT_ACCESS).text_request()  # Токен API к Dialogflow

    request.lang = 'ua'  # На якій мові буде відправлено запит
    request.session_id = 'Finick_learn'  # ID сесії діалога (для навчання)
    request.query = update.message.text  # Запит до ШІ

    try:
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
    except:
        response = None

    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        log.logging.info("ERERE")
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')

