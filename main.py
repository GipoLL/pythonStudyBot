import telebot
from telebot import types

token = '820679359:AAGfPGxx3AvVbWCI8F7QXQFlBy_F6_HKpKA'

bot = telebot.TeleBot(token)

# Реакция на команду start и первое меню
@bot.message_handler(commands=['start'])
def hadle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Обучение')
    user_markup.row('Экзамены и зачеты')
    user_markup.row('О КИПУ')
    user_markup.row('Полезное')
    bot.send_message(message.chat.id, 'Добро пожаловать в чат-бота для помощи в дистанционном обучении', reply_markup=user_markup)

@bot.message_handler(content_types=["text"])
def send_text(message):

    # Меню Обучение
    if message.text == "Обучение":
        study_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        study_markup.row('Расиписание')
        study_markup.row('Чаты и беседы')
        study_markup.row('Лабараторные и лекции')
        study_markup.row('Главное меню')
        bot.send_message(message.chat.id, "Выбери то, что тебя интересует:", reply_markup=study_markup)

        if message.text == 'Расиписание':
            sti = open('stat')
            bot.send_photo(message.chat.id, open('1.png'))

    # Меню Зачеты и Экзамены
    elif message.text == 'Экзамены и зачеты':
        exam_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        exam_markup.row('Расписание экзаменов и зачетов')
        exam_markup.row('Расписание пересдач')
        exam_markup.row('Главное меню')
        bot.send_message(message.chat.id, "Ты Нажал Экзамены и зачеты", reply_markup=exam_markup)

    # Меню О КИПУ
    elif message.text == 'О КИПУ':
        bot.send_message(message.chat.id, "Ты нажал О КИПУ")
        kipu_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        kipu_markup.row('Новости')
        kipu_markup.row('События')
        kipu_markup.row('Путеводитель')
        kipu_markup.row('Главное меню')

    # Меню Поленое
    elif message.text == 'Полезное':
        text = '[Сайт Университета](http://kipu-rc.ru/) \n' \
               '[Сайт дистанционного обучение Мудл](http://e.kipu-rc.ru/)\n' \
               '[Практика знаний в мини играх](https://www.codewars.com/)\n' \
               '[Бесплатные хостинги](https://vk.com/@thecode.media-besplatnye-hostingi-da-besplatnye)\n' \
               '[Полезные и интересные статьи в тематике IT](https://habr.com/ru/)\n' \
               '[Интересный журнал от Яндекса](https://thecode.media/)'
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')

bot.polling(none_stop=True) # Проверяет на сервере наличие новых сообщений