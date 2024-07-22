from flask import *
import datetime


web_app=Flask("Patient Management System")


@web_app.route("/")  #decorator
def index():
    message="Welcoem to Patient Management System. Its {}".format(datetime.datetime.now())
    message1="C:\index.html"
    return render_template("index.html")

@web_app.route("/register")
def register():
    
    return render_template("register.html")

@web_app.route("/home")
def home():
    return render_template("home.html")

@web_app.route("/add-patient" ,methods=["POST"])
def add_patient():
    return render_template("add_patient.html")

@web_app.route("/add-user" , methods=["POST"])
def add_user_in_db():
    pass


def main():
    web_app.run()  #it will run the program in loop which will not ends. in.run(PORTNO.) if empty it automatically allowcates

if __name__=="__main__":
    main()