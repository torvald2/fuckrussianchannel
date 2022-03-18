import random
import logging
from telethon import TelegramClient,sync
from telethon.sessions import StringSession

import asyncio

import services
logging.basicConfig(level=logging.INFO)

if __name__=="__main__":
    conf = services.Config()
    with TelegramClient("session", conf.api_id, conf.api_hash) as client:
        try:
            messages = services.get_message_list(conf.messages_list_file)
        except Exception as e:
            raise(f"Load messages lisr failed {e}")
        
        chanelStore = services.ChannelStore(conf.report_store,conf.report_list_file, conf.chanels_url)
        for chanel in chanelStore:
            try:
                services.report(chanel, random.choice(messages),conf.join_period, client)
                logging.info(f"reported chanel {chanel}")
            except Exception as e:
                logging.error(f"Chanel report exception {chanel}, error : {e}")
