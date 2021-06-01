from emoji import emojize
import settings 
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать котика',KeyboardButton('Мои координаты', request_location = True)]], resize_keyboard = True)


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_number(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
         message = f'Твоё число: {user_number}, моё число: {bot_number}. Ты выиграл!'
    elif user_number == bot_number:
        message = f'Твоё число: {user_number}, моё число: {bot_number}.  Ничья!'
    else:
        message = f'Твоё число: {user_number}, моё число: {bot_number}. Ты проиграл!'

    return message