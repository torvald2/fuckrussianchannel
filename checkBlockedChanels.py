import random
import logging
from telethon import TelegramClient,sync
from telethon.sessions import StringSession
import json
import asyncio

import services
logging.basicConfig(level=logging.INFO)

if __name__=="__main__":
    conf = services.Config()
    with open("chanels.json") as f:
        data = json.loads(f.read())
    res = []

    
    with TelegramClient("session", conf.api_id, conf.api_hash) as client:
        
        for chanel in data:
            blocked = services.isChanelBlocked(chanel["id"],client)
            if blocked:
                print(f"Chaner {chanel['id']} is blocked")
            else:
                res.append(chanel)

    with open("chanels.json","w") as f:
        f.write(json.dumps(res))
        
    
            
