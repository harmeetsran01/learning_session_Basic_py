from flask import *

web=Flask(__name__)

@web.route("/")
def tester1():
    return render_template("1.html")

@web.route("/home" , methods=['POST'])
def tester2():
    data={
        "name":request.form['yo']
    }
    if len(data) > 0:
        return render_template("2.html")

if __name__=="__main__":
    web.run(debug=True)
