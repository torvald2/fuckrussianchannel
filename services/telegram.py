import time
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.account import ReportPeerRequest
from telethon import types 

def report(channel, message, period,client):
    client(JoinChannelRequest(channel))
    time.sleep(period)
    client(ReportPeerRequest(
            peer=channel,
            reason=types.InputReportReasonOther(),
            message =  message,
        ))
    client(LeaveChannelRequest(channel=channel))

def isChanelBlocked(channel,client):
    e = client.get_entity(channel)
    if e.restricted:
        return False
    return True
        