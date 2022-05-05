import telebot
import requests as r
bot = telebot.TeleBot('5396054230:AAFpE1oQKho9kNllbxkNobGhzz4aclELkAE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет как дела':
        answer ='привет хорошо'
        bot.send_message(message.from_user.id,answer)
    elif message.text == '/help':
        answer = 'Напишы "Привет"'
        bot.send_message(message.from_user.id, answer)
    elif message .text == 'c':
        response =r.get('https://github.com')
        if response.status_code == 200:
            bot.send_message(message.from_user.id, 'доступен')
    else:
         answer = 'япам "я не понимаю"'
         bot.send_message(message.from_user.id, answer)
bot.polling(none_stop=True,interval= 0)



