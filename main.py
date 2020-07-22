import os
import sys
import logging
import logging.handlers
from discord.ext import commands
from cogs.utils.config import *
import random


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

bot = commands.Bot(command_prefix="%",
                   description='''MonBot sends hugs on command!\nMade by Lexi#2248''')


@bot.event
async def on_ready():
    message = 'Logged in as %s.' % bot.user
    uid_message = 'User ID: %s' % bot.user.id
    separator = '-' * max(len(message), len(uid_message))
    print(separator)
    try:
        print(message)
    except:
        print(message.encode(errors='replace').decode())
    print(uid_message)

gifs = [
    'https://media2.giphy.com/media/GMFUrC8E8aWoo/giphy.gif?cid=ecf05e477a38a1c180c5504f014226ef128ba632f85c71b8&rid=giphy.gif',
    'https://media0.giphy.com/media/PHZ7v9tfQu0o0/200w.webp?cid=ecf05e477a38a1c180c5504f014226ef128ba632f85c71b8&rid=200w.webp',
    'https://media3.giphy.com/media/l2QDM9Jnim1YVILXa/200w.webp?cid=ecf05e477a38a1c180c5504f014226ef128ba632f85c71b8&rid=200w.webp',
    'https://media0.giphy.com/media/BXrwTdoho6hkQ/200w.webp?cid=ecf05e477a38a1c180c5504f014226ef128ba632f85c71b8&rid=200w.webp',
    'https://media2.giphy.com/media/ARSp9T7wwxNcs/200.webp?cid=ecf05e477a38a1c180c5504f014226ef128ba632f85c71b8&rid=200.webp',
    'https://media1.giphy.com/media/ZQN9jsRWp1M76/200w.webp?cid=ecf05e477a38a1c180c5504f014226ef128ba632f85c71b8&rid=200w.webp',
    'https://media1.giphy.com/media/4HP0ddZnNVvKU/100.webp?cid=ecf05e47e96a185207f4b56a95401833f057212c5ddd67c9&rid=100.webp',
    'https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788',
    'https://media1.tenor.com/images/94989f6312726739893d41231942bb1b/tenor.gif?itemid=14106856',
    'https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/tenor.gif?itemid=14721541',
    'https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460',
    'https://media1.tenor.com/images/3ce31b15c2326831a8de9f0b693763ff/tenor.gif?itemid=16787485'
]


@bot.command()
async def hug(ctx):
    print(random.choice(gifs))
    await ctx.send(random.choice(gifs))

token = get_config_value('config', 'token')
bot.run(token)
