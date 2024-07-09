import datetime
# from session17 import patient

class consultation:
    def __init__(self,cid=0,pid="",remarks="",medicines="",next_followup="",created_on=None):
        self.cid=cid
        self.pid=pid
        self.remarks=remarks
        self.medicines=medicines
        self.next_followup=next_followup
        self.created_on=created_on

    def add_col_details(self):

        self.pid=input("Enter Pid here: ")
        self.remarks=input("Enter Remarks")
        self.medicines=input("Enter Medicines: ")
        self.next_followup=input("Enter Next Followup (yyyy-mm-dd): ")
        self.created_on=datetime.datetime.now()

    def show(self):
        consultation="""{cid} | {pid} | {remarks} | {medicines} | {next_followup} | {created_on}""".format_map(vars(self))
        print(consultation)
        

