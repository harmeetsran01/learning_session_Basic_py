from session18cMongoDB_template import MongoDBHelper
from session18a import User
def main():
    print("Welcome to Mongodb Test app")
    dbhelper=MongoDBHelper(collection="Patients")

    user=User()
    # user.add_details()
    document=vars(user)

    # dbhelper.insert(document)
    users=dbhelper.fetch()
    for user in users:
        print(user)
        print()

if __name__=="__main__":
    main()

