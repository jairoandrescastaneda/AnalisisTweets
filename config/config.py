import os

class Config:

    def __init__(self):
        self.mongodb_host = os.getenv("MONGODB_HOST")
        self.mongodb_username = os.getenv("MONGODB_USERNAME")
        self.mongodb_password = os.getenv("MONGODB_PASSWORD")
        self.mongodb_name = os.getenv("MONGODB_NAME")
        self.twitter_consumerkey = os.getenv("TWITTER_CONSUMERKEY")
        self.twitter_consumer_secretkey = os.getenv("TWITTER_CONSUMER_SECRETKEY")
        self.twitter_accesstoken = os.getenv("TWITTER_ACESSTOKEN")
        self.twitter_access_tokensecret = os.getenv("TWITTER_ACESS_TOKENSECRET")
        self.enviroment = os.getenv("ENV")
        self.ibm_key = os.getenv("IBM_API_KEY")
        self.ibm_version = os.getenv("IBM_VERSION")
        self.ibm_url = os.getenv("IBM_SERVICE_URL")
        self.ibm_assistant = os.getenv("IBM_ASSISTANT_ID")


    
    def get_connectiondb(self):
        return  {
            "host": self.mongodb_host,
            "name": self.mongodb_name,
            "password": self.mongodb_password,
            "username": self.mongodb_username
        }

    def get_twittercredentials(self):
        return {
            "consumer_key": self.twitter_consumerkey,
            "consumer_secret": self.twitter_consumer_secretkey,
            "access_token": self.twitter_accesstoken,
            "access_token_secret": self.twitter_access_tokensecret
        }

    def get_enviroment(self):
        return self.enviroment  
    
    def get_ibmcredentials(self):
        return {

            "ibm_key":self.ibm_key,
            "assistant_id":self.ibm_assistant,
            "version":self.ibm_version,
            "url":self.ibm_url

        }