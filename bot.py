import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi Friends ❤️

Here You can get Kana Kaanum Kaalangal Web Series All Episode.

Our Main Channel ID
@Aj_creations_ajay
@Kaana_kaanum_kaalangal

Type /Start for Every Updates

Use /off to pause your subscription.')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Hi Friends ❤️

Here You can get Kana Kaanum Kaalangal Web Series All Episodes within 1 second.

Our Main Channel ID
@Aj_creations_ajay
@Kaana_kaanum_kaalangal

Type /Start for Every Updates

Use /off to pause your subscription.')    

@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

