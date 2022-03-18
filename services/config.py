import logging
import os
import configparser

CHALELS_URL="https://raw.githubusercontent.com/torvald2/fuckrussianchannel/master/chanels.json"

class Config:
    def __init__(self) -> None:
        if os.environ.get("RUN_IN_DOCKER"):
            logging.info("GET CONFIG FROM ENVIRONMENT")
            try:
                self.api_id = int(os.environ.get("API_ID"))
            except:
                raise("BAD API_URL")
            self.api_hash = os.environ.get("API_HASH")
            if not self.api_hash:
                raise("BAD API HASH")
            self.join_period = float(os.environ.get("JOIN_PERIOD","15"))
            self.report_store = os.environ.get("REPORT_STORE","web")
            self.report_list_file = os.environ.get("REPORT_LIST_FILE","chanels.json")
            self.messages_list_file = os.environ.get("MESSAGES_LIST_FILE","messages.json")
            self.chanels_url = os.environ.get("CHALENS_URL",CHALELS_URL)
        else: 
            logging.info("LOAD CONFIG FROM INI FILE")
            config = configparser.ConfigParser()
            config.read(os.path.join(os.getcwd(),'config.ini'))
            try:
                self.api_id = int(config['TELEGA']['api_id'])
            except:
                raise("BAD API_URL")
            self.api_hash = config['TELEGA']['api_hash']
            if self.api_hash=="":
                raise("BAD API HASH")
            self.join_period = float(config["MAIN"].get("join_period","15"))
            self.report_store = config["MAIN"].get("report_store","web")
            self.report_list_file = config["MAIN"].get("report_list_address","chanels.json")
            self.messages_list_file = config["MAIN"].get("messages_list_address","messages.json")
            self.chanels_url = config["MAIN"].get("chanels_url",CHALELS_URL)

    

            




