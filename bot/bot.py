from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import settings
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, ChatID: %s, Message: %s' %
                 (update.message.chat.username, update.message.chat.id, update.message.text))
    update.message.reply_text(user_text)


def get_constellation(bot, update, args):
    solar_system = {
        'Mercury': ephem.Mercury(),
        'Venus': ephem.Venus(),
        'Mars': ephem.Mars(),
        'Jupiter': ephem.Jupiter(),
        'Saturn': ephem.Saturn(),
        'Uranus': ephem.Uranus(),
        'Neptune': ephem.Neptune(),
        'Pluto': ephem.Pluto()
    }
    planet_name = args[0].strip()
    if planet_name in solar_system:
        planet = solar_system[planet_name]
        planet.compute(datetime.date.today())
        update.message.reply_text('{} is in constellation {}'.format(planet_name, ephem.constellation(planet)[1]))
    else:
        update.message.reply_text('Неизвестная планета')


def main():
    mybot = Updater(settings.API_KEY)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', get_constellation, pass_args=True))
    mybot.start_polling()
    mybot.idle()


main()
