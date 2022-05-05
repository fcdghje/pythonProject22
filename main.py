import telebot

bot = telebot.TeleBot('5396054230:AAFpE1oQKho9kNllbxkNobGhzz4aclELkAE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет как дела':
        answer ='привет'
        bot.send_message(message.from_user.id,answer)
    elif message.text == '/help':
        answer = 'Напишы "Привет"'
        bot.send_message(message.from_user.id, answer)
    else:
         answer = 'ямпап "Привет"'
         bot.send_message(message.from_user.id, answer)
bot.polling(none_stop=True,interval= 0)



