import time
import asyncio
import json
import configparser
import random
import logging
import types
from unittest import result
from telethon import TelegramClient, events, sync,types, functions 
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.account import ReportPeerRequest


#Read config 
config = configparser.ConfigParser()
config.read('config.ini')

api_id = int(config['TELEGA']['api_id'])
api_hash = config['TELEGA']['api_hash']
period_seconds = float(config["MAIN"]["join_period"])

def get_message_list_local(path):
    data = []
    with open(path) as f:
        r = json.loads(f.read())
        for line in r:
            data.append(line["text"])
    return data

def get_chanel_list_local(path):
    data = []
    with open(path) as f:
        r = json.loads(f.read())
        for line in r:
            data.append(line["id"])
    return data
    



def workWithChanel(channel,message,client):
    client(JoinChannelRequest(channel))
    time.sleep(period_seconds)
    client(ReportPeerRequest(
            peer=channel,
            reason=types.InputReportReasonOther(),
            message =  message,
    ))
    logging.debug(f"Chanel reported {channel}")
    client(LeaveChannelRequest(channel=channel))

if __name__=="__main__":
    with TelegramClient("session", api_id, api_hash) as client:
        messages = get_message_list_local("messages.json")
        chanels = get_chanel_list_local("chanels.json")
        for chanel in chanels:
            workWithChanel(chanel, random.choice(messages),client)
    
    
