import os
import sys
import subprocess
import logging
import json
from pathlib import Path
from json import load, dump
from discord.ext import commands
from cogs.utils.config import *

if not os.path.exists('settings/'):
    os.makedirs('settings/')

def setup():
    config = {}
    print("Welcome to the MonBot setup wizard!\nThis wizard will guide you through the initial configuration required to get the bot working.\nThe choices you make in this wizard can be changed at any time by editing the settings/config.json file.\n")

    config["token"] = False
    while not config["token"]:
        print("The first step is to enter your bot token.")
        print("Go to https://discord.com/developers and copy the bot token from the desired application.")
        print("Paste the token below.")
        print("-------------------------------------------------------------")
        config["token"] = input("| ").strip().strip('"')
        if not config["token"]:
            print("Please enter your token.")

    config["prefix"] = False
    while not config["prefix"]:
        print("\nEnter the command prefix you want to use for main commands (e.g. if you enter > you will use commands like so: >about).")
        print("-------------------------------------------------------------")
        config["prefix"] = input("| ").strip()
        if not config["prefix"]:
            print("Empty command prefixes are invalid.")

    config["setup_run"] = True

    input("\nThis concludes the setup wizard. The bot can be started by pressing enter.")

    print("Starting bot...")

    if not os.path.exists('settings/config.json'):
        Path('settings/config.json').touch()

    with open('settings/config.json', encoding='utf8', mode='w') as f:
        dump(config, f, sort_keys=True, indent=4)

    params = [sys.executable, 'main.py']
    params.extend(sys.argv[1:])
    subprocess.call(params) 

if not os.path.exists('settings/config.json'):
    setup()

if get_config_value('config', 'setup_run'):
    print("The setup has already run.")
else:
    setup()