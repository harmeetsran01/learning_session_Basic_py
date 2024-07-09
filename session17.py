# Docter application to record patient details
# and consulation
# cid pid remarks medicines next_followup created on
"""
create table patient (
    pid int primary key auto_increment,
    name varchar(20),
    phone varchar(20),
    email varchar(20),
    dob varchar(20),
    gender varchar(20)
    created_on datetime
                      );
"""

import datetime

class patient:
    def __int__(self,pid="",name="",phone="",email="",dob="",gender="",created_on=None):
        self.pid=pid
        self.name=name
        self.phone=phone
        self.email=email
        self.dob=dob
        self.gender=gender
        self.created_on=created_on

    def add_details(self):
        self.pid=input("Enter PID: ")
        self.name=input("Enter Name: ")
        self.phone=input("Enter Phone: ")
        self.email=input("Enter Email:")
        self.dob=input("Enter DOB: ")
        self.gender=input("Enter Gender: ")
        self.created_on=datetime.datetime.now()

    def show(self):

        p1="""{pid} | {name} | {phone} | {email} | {dob} | {gender} | {created_on}""".format_map(vars(self))
        print(p1)




        