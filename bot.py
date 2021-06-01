import logging
import settings 
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import greet_user, guess_number, sand_cat_picture, talk_to_me, user_coordinates



PROXY = {'proxy_url': settings.PROXY_ULR, 
            'urllib3_proxy_kwargs':{
                'username' : settings.PROXY_USERNAME,
                'password' : settings.PROXY_PASSWORD
            }
        }


logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", sand_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), sand_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()