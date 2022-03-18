import requests
import json
import logging
import os

class ChannelStore:
    def __init__(self,report_store, report_file, report_url) -> None:
        if report_store == "web":
            logging.info("LOAD CHANEL LIST FROM WEB")
            self.chanels = self.__getChanelsFromWeb(report_url)
        else:
            logging.info("LOAD CHANEL LIST FROM LOCAL FILE")
            self.chanels = self.__loadChanelsFromFile(report_file)
    


    @staticmethod
    def __getChanelsFromWeb(store):
        r = requests.get(store)
        if r.status_code == 200:
            lst = []
            data =  json.loads(r.text)
            for row in data:
                lst.append(row["id"])
            return lst
        else:
            raise(f"Get Chanel list error: status_code: {r.status_code}")
    @staticmethod
    def __loadChanelsFromFile(store):
        data = []
        with open(os.path.join(os.getcwd(),store)) as f:
            r = json.loads(f.read())
            for line in r:
                data.append(line["id"])
        return data
        
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.chanels):
            chan = self.chanels[self.index]
            self.index+=1
            return chan
        else:
            raise StopIteration




        