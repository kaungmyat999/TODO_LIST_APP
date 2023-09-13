from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connectDB() -> MongoClient:
    uri = "mongodb+srv://kaungmyatcomputerscience:Ty5mJAyR9vqNEoel@cluster0.l4mblox.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client


class DB:
    def __init__(self,DBName,collection):
        self.db = connectDB()[DBName]
        self.myCollection = self.db[collection]


    def find(self):
        return self.self.myCollection.find()
    
    def getIndex(self):
        return self.myCollection.index_information()
    
    def getCollection(self):
        return self.myCollection

    def getAllCollections(self):
        return self.db.get_collection()
    
    

    


