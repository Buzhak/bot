import logging
from emoji import emojize
from random import choice, randint
import logging
import settings 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, update
from glob import glob

PROXY = {'proxy_url': settings.PROXY_ULR, 
            'urllib3_proxy_kwargs':{
                'username' : settings.PROXY_USERNAME,
                'password' : settings.PROXY_PASSWORD
            }
        }


logging.basicConfig(filename='bot.log', level=logging.INFO)


    

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def greet_user(update, context):
    context.user_data['emoji']= get_smile(context.user_data)
    update.message.reply_text(f"Здравствуй, пользователь {context.user_data['emoji']}!")

def talk_to_me(update, contect):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def play_random_number(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
         message = f'Твоё число: {user_number}, моё число: {bot_number}. Ты выиграл!'
    elif user_number == bot_number:
        message = f'Твоё число: {user_number}, моё число: {bot_number}.  Ничья!'
    else:
        message = f'Твоё число: {user_number}, моё число: {bot_number}. Ты проиграл!'

    return message

def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            number = int(context.args[0])
            message = play_random_number(number)
            
        except(ValueError, TypeError):
            message = f'{context.args[0]} -  не является числом.'

    else:
        message = 'Введите число'
    update.message.reply_text(message)


def sand_cat_picture(update, context):
    print('/cat')
    cat_photos_list = glob("/Users/admin/Desktop/Projects/bot/images/cat*.jp*g")
    print(glob)
    cat_picture_fileName = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id = chat_id, photo = open(cat_picture_fileName, 'rb'))

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", sand_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()