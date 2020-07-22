import os
import sys
import logging
import logging.handlers
from discord.ext import commands
from cogs.utils.config import *

def set_log():
    errformat = logging.Formatter(
        '%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: '
        '%(message)s',
        datefmt="[%d/%m/%Y %H:%M]")

    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)

    if not os.path.exists('settings/logs'):
        os.makedirs('settings/logs')
    errhandler = logging.handlers.RotatingFileHandler(
        filename='settings/logs/bot.log', encoding='utf-8', mode='a',
        maxBytes=10**7, backupCount=5)
    errhandler.setFormatter(errformat)

    logger.addHandler(errhandler)

    return logger

logger = set_log()

bot = commands.Bot(command_prefix="%", description='''MonBot sends hugs on command!\nMade by Lexi#2248''')

@bot.event
async def on_ready():
    message = 'logged in as %s' % bot.user
    uid_message = 'user id %s' % bot.user.id
    separator = '-' * max(len(message), len(uid_message))
    print(separator)
    try:
        print(message)
    except:
        print(message.encode(errors='replace').decode())
    print(uid_message)



token = get_config_value('config', 'token')
bot.run(token)