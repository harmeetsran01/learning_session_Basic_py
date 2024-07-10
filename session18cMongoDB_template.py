
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
class MongoDBHelper:
    def __init__(self,collection="users") -> None:
        uri = "mongodb+srv://root:pcte@cluster0.yud0bu3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        self.db=client['aurobises']
        self.collection=self.db[collection]
        # print(self.collection)

        # for collections in collection:
        #     print(collections)

    def insert(self,document):
        self.collection.insert_one(document)
        print("Insert done in Collection:",self.collection.name)

    def fetch(self,query=""):
        documents=self.collection.find(query) #return as list
        return list(documents)
        

MongoDBHelper()