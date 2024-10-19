"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("21060976")
        self.API_HASH: str = os.environ.get("b8b9e236dd578d07621f5a8174a891d9")
        self.SESSION: str = os.environ.get("BAFBXXAABB7UIkEHGsrDzcwN1dR5m2p5qZgTjQ5LT6HK0cNEcC_-trIJ3aOnTyp3Jq9_bdxkjjeF2pcVJ3V37Mj7c-VJ-qWr-Vu6YQJFuLOz_bb5tQtqZeeBVxjP5pcPoiVv3LV1dEwT_CeADLJW0yzJv14UgTNo8mCBoIFj3xxUQTvAIr1OrDyhaQm4oIleKRLVLyD18sPi7T-5xhQ9yJfT8FUGuR3XbROqxWd23R91P8P-trM6doJzDd2BV0IGjxbgp7LXnlWEspFD8kMGIxbSeg_FZy8clhG1tpDotpqTyCv2nZijs6f0avXycXh2RhxX48ioFe0CNUpz8wa2zBWKB8KqagAAAAGRsXUgAA")
        self.BOT_TOKEN: str = os.environ.get("7847521628:AAHn0CiVxcWZF2mG0leMLzRTsCS134xz0PE")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS"6739293472"").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("31befwqzmxiik7rs5betkymkxeiy")
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("6nfdNPorHewU3f8H4oSgFC")


config = Config()
