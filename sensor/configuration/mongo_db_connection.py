import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()
import os

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                MONGODB_URL = os.getenv('MONGODB_URL',None)
                MONGODB_SECRET = os.getenv('MONGODB_SECRET',None)                
                mongo_db_url = MONGODB_URL.format(MONGODB_SECRET)

                #export MONGODB_URL='mongodb+srv://vvksensors:{0}@cluster0.xxfdwvf.mongodb.net/?retryWrites=true&w=majority'
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

