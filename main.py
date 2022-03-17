import time
import asyncio
import json
import configparser
import random
import logging
import types
import requests
from unittest import result
from urllib import request
from telethon import TelegramClient, events, sync,types, functions 
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.account import ReportPeerRequest


#Read config 
config = configparser.ConfigParser()
config.read('config.ini')

api_id = int(config['TELEGA']['api_id'])
api_hash = config['TELEGA']['api_hash']
period_seconds = float(config["MAIN"]["join_period"])
report_store = config["MAIN"]["report_store"]
web_sote = config["MAIN"]["chanels_url"]

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
    
def get_chanel_list_from_web(url):
    r = requests.get(url)
    if r.status_code == 200:
        return json.loads(r.text)



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
        if report_store == "web":
            chanels = get_chanel_list_from_web(web_sote)
            if not chanels:
                raise("Get Chanel list error")
        else:  
            chanels = get_chanel_list_local("chanels.json")
        for chanel in chanels:
            try:
                workWithChanel(chanel, random.choice(messages),client)
            except Exception as e:
                logging.error(f"Chanel report exception {chanel}, error : {e}")
    
    
