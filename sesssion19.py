"""
Install Flask in virtual env
"""
from flask import *

application=Flask("Its a Web Application")


def main():
    application.run()

@application.route("/")
def buggi():
    gungi="l"
    return gungi

@application.route("/home")
def faltu():
    message="Welcome to Application"
    return message

@application.route("/home1")
def html():
    html="""
    <html>
    <head>
    <title> hello </title>
    </head>
    <body> <h3> Hello </h3>
    </body>
    </html>
    """
    return html

    
    

if __name__=="__main__":
    main()



