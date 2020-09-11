#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from bot import bot

bot.start_webhook(host='0.0.0.0', path=os.environ['TOCK_WEBHOOK_PATH'], port=5000)
