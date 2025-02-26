# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """

import os
import signal
import sys
import time

from datetime import datetime
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from platform import python_version
from sys import version_info
from time import sleep
import re

from pathlib import Path
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil
from platform import python_version

from dotenv import load_dotenv
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telethon import TelegramClient, version

from telethon.utils import get_display_name
from telethon import Button, functions, types
from dotenv import load_dotenv
from telethon import version
from telethon.sync import TelegramClient, custom, events
from telethon.sessions import StringSession

from .storage import Storage

STORAGE = (lambda n: Storage(Path("data") / n))

load_dotenv("config.env")

StartTime = time.time()


# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
    )
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info(
        "You MUST have a python version of at least 3.8."
        "Multiple features depend on this. Bot quitting."
    )
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)


# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL", "https://github.com/ythm00/Cyber.git"
)
# UPSTREAM_REPO_URL branch, the default is master
UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Google Drive Module
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# Default .alive name anf logo
ALIVE_NAME = os.environ.get("ALIVE_NAME") or None
ALIVE_LOGO = (
    os.environ.get("ALIVE_LOGO") or "https://telegra.ph/file/7c2398e55b23097f36e41.mp4"
)

# Inline Picture
INLINE_PICTURE = os.environ.get(
    "INLINE_PICTURE") or "resource/Cyber-Button.jpg"

L_PIC = str(INLINE_PICTURE)
if L_PIC:
    cyberlogo = L_PIC
else:
    cyberlogo = "resource/Cyber-Button.jpg"


INLINE_LOGO = os.environ.get(
    "INLINE_LOGO") or "https://telegra.ph/file/eff0e10179055c4af7cac.jpg"

IN_PIC = str(INLINE_LOGO)
if IN_PIC:
    cyberlogo = IN_PIC
else:
    cyberlogo = "https://telegra.ph/file/eff0e10179055c4af7cac.jpg"

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Deezload ARL Token for Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)

lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except Exception:
        pass

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
G_DRIVE_INDEX_URL = os.environ.get("G_DRIVE_INDEX_URL", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")

# Terminal Alias
TERM_ALIAS = os.environ.get("TERM_ALIAS", None)

# Genius Lyrics API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# Uptobox
USR_TOKEN = os.environ.get("USR_TOKEN_UPTOBOX", None)


# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)


def shutdown_bot(signum, frame):
    LOGS.info("Received SIGTERM.")
    bot.disconnect()
    sys.exit(143)


signal.signal(signal.SIGTERM, shutdown_bot)


def shutdown_bot(signum, frame):
    LOGS.info("Received SIGTERM.")
    bot.disconnect()
    sys.exit(143)


signal.signal(signal.SIGTERM, shutdown_bot)


def migration_workaround():
    try:
        from userbot.modules.sql_helper.globals import addgvar, delgvar, gvarstatus
    except AttributeError:
        return None

    old_ip = gvarstatus("public_ip")
    new_ip = get("https://api.ipify.org").text

    if old_ip is None:
        delgvar("public_ip")
        addgvar("public_ip", new_ip)
        return None

    if old_ip == new_ip:
        return None

    sleep_time = 180
    LOGS.info(
        f"A change in IP address is detected, waiting for {sleep_time / 60} minutes before starting the bot."
    )
    sleep(sleep_time)
    LOGS.info("Starting bot...")

    delgvar("public_ip")
    addgvar("public_ip", new_ip)
    return None


# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly."
        )
        quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file."
        )
        quit(1)


async def update_restart_msg(chat_id, msg_id):
    DEFAULTUSER = ALIVE_NAME or "Set `ALIVE_NAME` ConfigVar!"
    message = (
        f"**Cyber is back up and running!**\n\n"
        f"**Telethon :** __{version.__version__}__\n"
        f"**Python :** __{python_version()}__\n"
        f"**User :** __{DEFAULTUSER}__"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from userbot.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    try:
        with bot:
            bot.loop.run_until_complete(update_restart_msg(int(chat_id), int(msg_id)))
    except BaseException:
        pass
    delgvar("restartstatus")
except AttributeError:
    pass

async def send_alive_status():
    if BOTLOG_CHATID:
        message = (
            "**Bot is up and running!**\n\n"
            f"**Telethon:** {version.__version__}\n"
            f"**Python:** {python_version()}\n"
            f"**User:** {ALIVE_NAME or 'Set `ALIVE_NAME` ConfigVar!'}"
        )
        await bot.send_message(BOTLOG_CHATID, message)
        return True



# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 2
    global unpage
    unpage = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline("{} {}".format("", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "<", data="{}_prev({})".format(prefix, modulo_page)           
                ),
                custom.Button.inline(
                    "Back", data="{}_back({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    ">", data="{}_next({})".format(prefix, modulo_page)
                )
            )
        ] 
    return pairs

# ___________________Reg________________ #
from git import repo

with bot:
    try:
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

# ______________Flex____________________ #
        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id


# _____________Replc______________ #

        plugins = CMD_HELP

# _______________ InlinePic _____________ #

        cyber_PIC = str(INLINE_PICTURE)
        if L_PIC:
            cyber_logo = L_PIC
        else:
            cyberlogo = "resource/Cyber-Button.jpg"


        IN_PIC = str(INLINE_LOGO)
        if IN_PIC:
            cyberlogo = IN_PIC
        else:
            cyberlogo = "https://telegra.ph/file/eff0e10179055c4af7cac.jpg"

# ======================================== Inline Handler ======================================== #

        @tgbot.on(events.NewMessage(pattern="/start"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"Hai 👋 [{get_display_name(u)}](tg://user?id={u.id}) Welcome To **Cyber**",
                    buttons=[
                        [
                            Button.url("Support Group",
                                       "https://t.me/RythmSupportGroup")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern="/deploy"))
        async def handler(event):
            if event.message.from_id != uid:
                await event.reply(
                    f"**Cyber** Deploy to Heroku, Click Here ",
                    buttons=[
                        [Button.url("Deploy", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fythm00%2FCyber&template=https%3A%2F%2Fgithub.com%2Fythm00%2FCyber%2Ftree%2Fmaster")],
                    ],
                )

        @tgbot.on(events.NewMessage(pattern="/repo"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                text = (
                    f"Haii [{get_display_name(u)}](tg://user?id={u.id}) My Name is **Cyber**\n"
                    f"and For Maintaining Your Group.\n"
                    f"I was **Created by :** @SyndicateTwenty4 For Various Userbots on Github.\n")
                await tgbot.send_file(event.chat_id, file=cyberlogo,
                                      caption=text,
                                      buttons=[
                                          [
                                              custom.Button.url(
                                                  text="Repo",
                                                  url="https://github.com/ythm00/Cyber")],
                                      ]
                                      )
                                      


        @tgbot.on(events.NewMessage(pattern=r"/alive"))
        async def handler(event):
            if event.message.from_id != uid:
                text = (
                    f"**💡 Version** : `master`\n"
                    f"**👤 User** : `{ALIVE_NAME}`\n"
                    f"                           \n"
                    f"**__Python__**: `{python_version()}`\n"
                    f"**__Telethon__**: `{version.__version__}`\n")
            await tgbot.send_file(event.chat_id, file=cyberlogo,
                                       caption=text,
                                       buttons=[
                                           [
                                               Button.url("🧪 Repo",
                                                          "https://github.com/ythm00/Cyber"),
                                               Button.url("🎖️ GNU GPL v3.0",
                                                          "https://github.com/ythm00/Cyber/blob/master/LICENSE")],
                                       ]
                                       )

        @tgbot.on(events.NewMessage(pattern=r"/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"**PONG !!**\n `{ms}ms`",
                )

                                     
        @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@UserButt"):
                buttons = [
                    (Button.inline("Open Main Menu", data="mainmenu"),),
                ]
                photo_bytesio = cyberlogo
                result = builder.photo(photo_bytesio,
                    "Cyber Main Menu",
                    text="© Cyber",
                    link_preview=False,
                    buttons=buttons,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Cyber Helper",
                    text="List of Modules",
                    buttons=[],
                    link_preview=False)
            else:
                result = builder.article(
                    "Cyber",
                    text="""You can convert your account to bot and use them. Remember, you can't manage someone else's bot! All installation details are explained from GitHub address below.""",
                    buttons=[
                        [
                            custom.Button.url(
                                "GitHub Repo",
                                "https://github.com/ythm00/Cyber"),
                            custom.Button.url(
                                "Support",
                                "https://t.me/RythmSupportGroup")],
                    ],
                    link_preview=True,
                )
            await event.answer([result] if result else None)


        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"mainmenu")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                buttons = paginate_help(0, dugmeler, "helpme")
                text = f"Cyber modules helper.\n\nTotal loaded modules: {len(plugins)}"
                await event.edit(text,
                    file=cyberlogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"opener")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                current_page_number = int(unpage)
                buttons = paginate_help(current_page_number, plugins, "helpme")
                text = f"Cyber modules helper.\n\nTotal loaded modules: {len(plugins)}"
                await event.edit(text,
                    file=cyberlogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_back\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # Lynx-Openeer
                # https://t.me/TelethonChat/115200
                await event.edit(
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("Open Menu Again", data="opener")],
                    ]
                )
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(b"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 150:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace('`', '')[:150] + "..."
                        + "\n\nRead more .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = "Please make for yourself, don't use my bot!"

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Support for inline is disabled on your bot. "
            "To enable it, define a bot token and enable inline mode on your bot. "
            "If you think there is a problem other than this, contact us.")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file."
        )
        quit(1)

    try:
        bot.loop.run_until_complete(send_alive_status())
    except BaseException:
        pass
