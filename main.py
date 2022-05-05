import telebot
import requests as r
bot = telebot.TeleBot(')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет как дела':
        answer ='привет'
        bot.send_message(message.from_user.id,answer)
    elif message.text == '/help':
        answer = 'Напишы "Привет"'
        bot.send_message(message.from_user.id, answer)
    elif message .text == '/check-github':
        response =r.get('https://github.com')
        if
    else:
         answer = 'япам "я не понимаю"'
         bot.send_message(message.from_user.id, answer)
bot.polling(none_stop=True,interval= 0)



