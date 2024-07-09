# CMS
from session16 import Customer
from session16a_Database import Database
from tabulate import tabulate #pip installed
# from session16a import database

def main():
    print("CMS app")
    db=Database()
    customer=Customer()

    def showtable_using_cid(cid):
        sql = "select * from Customer where cid = {}".format(cid)
        rows = db.read(sql)
        customer = Customer(cid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3], age=rows[0][4], gender=rows[0][5])
        columns=["Cid","Name","Phone","Email","Age","Gender","Created_On"]
        print(tabulate(rows,headers=columns,tablefmt="grid"))
        


    while True:
        print("1. Add new customer:")
        print("2. Update Existong Customer:")
        print("3. Delete Existing Customer:")
        print("4. View Customer by Phone")
        print("5. View Customer by CID")
        print("6. View All customer:")
        print("0. to Exit\n")
        
        choice=int(input("Enter Choice: "))

        if choice==1:
            customer.add_details()
            sql = "insert into customer values(null,'{name}',{phone},'{email}',{age},'{gender}','{created_on}')".format_map(vars(customer))

            db.write(sql)
            # Database.write(sql)
            print("CMS APP",customer.name,"Saved in Database")

        elif choice==2:
            while True:
                print("To Update...")
                cid=int(input("Enter CID or 0 To exit: "))

                if cid == 0:
                    break
                
                showtable_using_cid(cid)

                # sql = "select * from Customer where cid = {}".format(cid)
                # rows = db.read(sql)
                # print(rows)
            
                # customer = Customer(cid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3], age=rows[0][4], gender=rows[0][5])
                # customer.show()
                # columns=["Cid","Name","Phone","Email","Age","Gender","Created_On"]
                # print(tabulate(rows,headers=columns,tablefmt="grid"))

                choice=input("Enter Column you want to change: ")

                if choice=="name":
                    name=input("Enter name: ")
                    sql="update customer set name = '{}' where cid = {}".format(name,cid)
                    db.write(sql)
                    print("Updation Done!")

                elif choice=="phone":
                    phone=int(input("Enter phone: "))
                    sql="update customer set phone = '{}' where cid = {}".format(phone,cid)
                    db.write(sql)
                    print("Updation Done!")

                elif choice=="email":
                    email=input("Enter email: ")
                    sql="update customer set email = '{}' where cid = {}".format(email,cid)
                    db.write(sql)
                    print("Updation Done!")

                elif choice=="age":
                    age=int(input("Enter age: "))
                    
                    sql="update customer set age = '{}' where cid = {}".format(age,cid)
                    db.write(sql)
                    print("Updation Done!")

                elif choice=="gender":
                    gender=input("Enter gender: ")
                    sql="update customer set gender = '{}' where cid = {}".format(gender,cid)
                    db.write(sql)
                    print("Updation Done!")

                else:
                    print("Invalid Statement")
                    

        elif choice==3:
            cid=int(input("Enter cid: "))
            sql= "delete from customer where cid = {}".format(cid)
            db.write(sql)
            print(cid,". CID is deleted...")
        elif choice==4:
            phone=int(input("Enter phone: "))
            sql="select * from customer where phone = {}".format(phone)
            rows=db.read(sql)
            columns=["Cid","Name","Phone","Email","Age","Gender","Created_On"]
            print(tabulate(rows,headers=columns,tablefmt="grid"))

        elif choice==5: 
            cid=int(input("Enter CID: "))
            sql="select * from customer where cid = {}".format(cid)
            print(db.read(sql))

            # For formatted tabulate printing
            rows=db.read(sql)
            columns=["Cid","Name","Phone","Email","Age","Gender","Created_On"]
            print(tabulate(rows,headers=columns,tablefmt="grid"))

        elif choice==6:
            sql="select * from customer"
            print(db.read(sql))

            # For formatted tabulate printing
            rows=db.read(sql)
            columns=["Cid","Name","Phone","Email","Age","Gender","Created_On"]
            print(tabulate(rows,headers=columns,tablefmt="grid"))
        elif choice==0:
            print("Thankyou for Using CMS!")
            break
        else:
            print("Invalid Choice: ")
        


if __name__=="__main__":

    main()



