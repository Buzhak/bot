from glob import glob
from random import choice
from utils import get_smile, play_random_number, main_keyboard

def greet_user(update, context):
    context.user_data['emoji']= get_smile(context.user_data)
    update.message.reply_text(f"Здравствуй, пользователь {context.user_data['emoji']}!", reply_markup = main_keyboard())

def talk_to_me(update, contect):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text, reply_markup = main_keyboard())

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
    context.bot.send_photo(chat_id = chat_id, photo = open(cat_picture_fileName, 'rb'),  reply_markup = main_keyboard())

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )