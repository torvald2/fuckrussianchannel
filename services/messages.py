import os
import json

def get_message_list(path):
    data = []
    with open(os.path.join(os.getcwd(),path)) as f:
        r = json.loads(f.read())
        for line in r:
            data.append(line["text"])
    return data