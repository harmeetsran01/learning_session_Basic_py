
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

    def insert(self,document,collection="users"):
        # self.collection=collection
        self.collection.insert_one(document)
        print("Insert done in Collection:",self.collection.name)
        print("Document inserted in collection:",self.collection.name)
        # result=self.collection.insert_one(document)
        # print(result.__inserted_id)
        # return result
        

# query as input will act as condition

    def fetch(self,query=""):
        documents=self.collection.find(query) #return as list
        return list(documents)
    
    def delete(self, query=""):
        result = self.collection.delete_one(query)
        print("result is:", result)

    def update(self, document, query):
        document_to_upate = {'$set': document}
        result = self.collection.update_one(query, document_to_upate)
        print("result is:", result)
        