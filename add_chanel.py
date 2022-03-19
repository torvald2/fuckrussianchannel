import sys
import json

with open("chanels.json") as f:
    data = json.loads(f.read())

for chan in sys.argv[1:]:

    ch = list(filter(lambda x: x["id"]==chan,data))
    if len(ch)==0:
        data.append({"id":chan})
        print(f"Chanel {chan} added")

with open("chanels.json","w") as f:
    f.write(json.dumps(data))
