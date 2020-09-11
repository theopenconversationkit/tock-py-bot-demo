#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from bot import bot

bot.start_websocket(apikey=os.environ['TOCK_APIKEY'])
# .start_websocket(apikey=os.environ['TOCK_APIKEY'], host="localhost", port=8080, protocol="ws")
