from session18cMongoDB_template import MongoDBHelper
from session18a import User
from bson.objectid  import ObjectId #if you wish to fetch data from hashcode
from tabulate import tabulate

def main():
    print("Welcome to Mongodb Test app")
    dbhelper=MongoDBHelper(collection="Patients")

    user=User()
    # user.add_details()
    document=vars(user)
    query={"_id":ObjectId("668ecaa1bc300fcbd66e2bd8")}
    # dbhelper.insert(document)
    users=dbhelper.fetch()
    
    # print(dbhelper.fetch({"email":"John@example.com"}))
    print("ENds")
    # print(users)
    # print("ENds")
    # for user in users:
    #     print(user)
    #     print()

    dbhelper=MongoDBHelper(collection="patientNew")
    query={
        "doctor":"harry@example.com"
    }
    result=dbhelper.fetch(query=query)


# To use update
    # document_to_update={"name":"Johnu","age":24}
    # dbhelper.update(document_to_update,query={"email":"John@example.com"})
    header= users[0].keys() #well not working
    
    print(tabulate(result ,headers="", tablefmt='grid'))
    # print(tabulate(users ,headers="", tablefmt='grid'))

if __name__=="__main__":
    main()

