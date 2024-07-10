
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:pcte@cluster0.yud0bu3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Get reference to the database
db = client['aurobises']

# Get Collection Names from DataBase
collections = db.list_collection_names()

for collection in collections:
    print(collection)

documents = db['hello'].find() #it will return in list or dictionary
print(documents)

print(vars(documents))
# documents = db['users'].find()
# print(documents)

# for document in documents:
#     print(document)