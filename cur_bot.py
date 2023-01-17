import telebot
import req


bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['help'])
def send_info(message):
    bot.send_message(
        message.chat.id, 'Это бот для получения информации о курсе валют')
    info = "Доступные команды: \n \
/valute all - получить коды всех валют \n \
/valute all_v - получить курс всех валют \n \
/valute <код валюты> - получить курс конкретной валюты"
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['valute'])
def send_currency(message):
    mode = message.text.split()[1]
    if mode == 'all':
        bot.send_message(message.chat.id, req.available_valute())
    elif mode == 'all_v':
        bot.send_message(message.chat.id, req.available_valute(True))
    else:
        bot.send_message(message.chat.id, req.valute(mode))


bot.infinity_polling()
