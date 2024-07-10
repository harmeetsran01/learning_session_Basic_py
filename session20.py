from flask import *
import datetime


web_app=Flask("Patient Management System")


@web_app.route("/")  #decorator
def index():
    message="Welcoem to Patient Management System. Its {}".format(datetime.datetime.now())
    message1="C:\index.html"
    return render_template("index.html")
def main():
    web_app.run()  #it will run the program in loop which will not ends. in.run(PORTNO.) if empty it automatically allowcates

if __name__=="__main__":
    main()

@web_app.route("/register")
def register():
    return render_template("register.html")