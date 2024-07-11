#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2024 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

# if you are using this following code then don't forgot to give proper
# credit to t.me/kAiF_00z (github.com/kaif-00z)

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default="22615660", cast=int)
    API_HASH = config("API_HASH", default="906e31e7abb5b7bc2990f8f78e8e4a78")
    BOT_TOKEN = config("BOT_TOKEN", default="7428457378:AAGEy3MiawGr6N5uXxFyg-J0-IKiuNkSBB0")
    SESSION = config("SESSION", default="1BVtsOLUBu4HpSq4_DPBHlQSbjjux-LrtG59xAFG93GO6YQ9-yHhaZVPs1MHZYFoPZamwH2vBVv5eQmCX9OMky2x2X61YrQBZM07phag8yU3Qe0yHJ0-qHI2HLfUPGMTgYjQQQI2b87uJYzGEhqM8ZtZGZbf16LnjazDpqGZ_U--r5Ucib_82yQMubyyK9ib00cyRE7ShfThEcekx2Y8-rVnKjr5bOR1ITF6hGJO9TIxOJJXmAkpkFAVC1Y3agrDhcrvIP0jyFNhUmgF9ENs80Wzspfj338A2TEvrdbXIQiHjgmvrADhPeGVTSzlQTWqZ0TLCeTXQSxdl5hvrq_deJbUQpPJDDZo=")

    # Database Credentials

    FIREBASE_URL = config("FIREBASE_URL", default="https://mrakanime-29308-default-rtdb.firebaseio.com")
    FIREBASE_SERVICE_ACCOUNT_FILE = config(
        "FIREBASE_SERVICE_ACCOUNT_FILE", default="https://gist.githubusercontent.com/MrAKTech/c733258771e265fdc5d1cf51436e626f/raw/6aef7fb1cd92c66e00b9a7c5e6a4eed7a909cd49/service.json"
    )

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default="-1002203370135", cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default="-1002190818424", cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default="-1002155091634", cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default="-1002186868546", cast=int)
    FORCESUB_CHANNEL = config("FORCESUB_CHANNEL", default="-1002107568197", cast=int)
    OWNER = config("OWNER", default="6119769857", cast=int)

    # Other Configs

    API_KEY = config("API_KEY", cast=str)
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/ad1b25807b81cdf1dff65.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CRF = config("CRF", default="27")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=False, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
    FORCESUB_CHANNEL_LINK = config("FORCESUB_CHANNEL_LINK", default="https://t.me/MrAK_AnimeZz", cast=str)
