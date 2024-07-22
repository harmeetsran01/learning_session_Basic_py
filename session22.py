from flask import *
import datetime
import hashlib
from session18cMongoDB_template import MongoDBHelper
from bson.objectid import ObjectId


web_app=Flask("Patient Management System")
db=MongoDBHelper(collection="Patients")


@web_app.route("/")  #decorator
def index():
    message="Welcoem to Patient Management System. Its {}".format(datetime.datetime.now())
    message1="C:\index.html"
    return render_template("index.html")


@web_app.route("/home")
def home():
    
    return render_template("home.html")



@web_app.route("/register")
def register():
    
    
    return render_template("register.html")



@web_app.route("/add-patient" ,methods=["POST"])
def add_patient():
    
    return render_template("add_patient.html")



@web_app.route("/add-user" , methods=['POST'])
def add_user_in_db():

    user_data={
        #create a Dictionary with Data from HTML Register Form
        "name":request.form["name"], 
        "email":request.form["email"], # "name" is key of dictionary(written in input of register.html)
                                      # : request.form [""] is key value written in input div with name=' '
        "password":hashlib.sha256(request.form["pwd"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }
    collection="doctor"
    db.collection=db.db[collection]
    db.insert(user_data)
    message="Data is: {name}, {email}, {password}, {created_on}".format_map(user_data)
    #result= db.insert(user_data)
    # r="{}".format(result.__inserted_id)

    # writing data in session object, this data can be use in html files, everywhere in the object
    session['name']=user_data["name"]
    session['email']=user_data["email"]
    # session['user_id']=str(user_data[result.__inserted_id])

    return render_template("home.html", name = session['name'], email = session['email'])



@web_app.route("/fetch-user" , methods=['GET' , 'POST'])
def Fetch_user_in_db():
    user_data={
       
        "email":request.form["email"], 
        "password":hashlib.sha256(request.form["pwd"].encode('utf-8')).hexdigest()
    
    }
    collection="doctor"
    db.collection=db.db[collection]
    result=db.fetch(query=user_data)

    

    if len(result)>0:
        session['email']= request.form["email"]
        return render_template("home.html" , email = session['email'])
    else:
        return "User not Found!"
   

@web_app.route("/add-patient-details" , methods=['post'])
def add_patient_details():
    patient_data={
   
        "name":request.form["name"], 
        "phone":request.form["phone"], 
        "email":request.form["email"], 
        "gender":request.form["gender"], 
        "address":request.form["address"], 
        "doctor":session['email'],
        "created_on": datetime.datetime.now()
    }
    # Database Change

    collection="patientNew"
    db.collection=db.db[collection]
    db.insert(patient_data)

    session['patient_name']=patient_data['name']
    
    if len(patient_data) != 0:
        return render_template("home_patientAdded.html" , name=patient_data["name"])
    
    else:
        return "Data not found!"
    
@web_app.route("/fetch-patient")
def fetch_patient_details():
     # "doctor":session["email"] "doctor":"harry@example.com"
    patient_data={
        "doctor":session["email"]
        
    }
    collection="patientNew"
    db.collection=db.db[collection]
    result=db.fetch(query=patient_data)
    print(result)

    # return "done"
    return render_template("viewpatient.html" , patients=result , email=session['email'])
    
@web_app.route("/searchpatient")
def search_patient_html():
    
    collection="patientNew"
    db.collection=db.db[collection]
    return render_template("searchpatient.html" , patients=db.fetch() )
    """
    if len(request.form["search_patient"]) > 0:
        patient_data={
       
        "name":request.form["search_patient"]
        
        }
        collection="patientNew"
        db.collection=db.db[collection]
        result=db.fetch(query=patient_data)

        return render_template("searchpatient.html" , patients=result , email=session['email'])

    elif len(request.form["search_patient"]) == 0:

        patient_data={
        
            "doctor":session["email"]
            
        }
        collection="patientNew"
        db.collection=db.db[collection]
        result=db.fetch(query=patient_data)

        return render_template("searchpatient.html" , patients=result , email=session['email'])
    """

@web_app.route("/searchpateintdetail" , methods=['POST'])
def patientsearch(): 
    if session['email']=='':
        return redirect("index.html")
    
    patient_data={
        "name":request.form['name']
    }
    print(patient_data)
    session['searchpatientname']=request.form['name']
    
    # return render_template("index.html")


    # print(request.form["searchpatient"])
    # session['searchpatientname']=request.form["searchpatient"]
    # print(session['searchpatientname'])
    if len(patient_data['name']) > 0:
        patient_data={
       
        "name":patient_data['name']
        
        }
        collection="patientNew"
        db.collection=db.db[collection]
        result=db.fetch(query=patient_data)

        return render_template("searchpatient.html" , patients=result , email=session['email'])

    elif len(patient_data['name']) == 0:

        patient_data={
        
            "doctor":session["email"]
            
        }
        collection="patientNew"
        db.collection=db.db[collection]
        result=db.fetch()

        return render_template("searchpatient.html" , patients=result , email=session['email'])
    
@web_app.route("/logout")
def logout():
    session['email']=''
    session['name']=''
    return redirect("/")



@web_app.route("/updatepatient/<id>")
def updatepatient(id):
    print("Patinet to be updated:", id)
    
    # Save Patient ID in Session, which needs to be updated
    session["id"] = id
    
    # Fetch document from patient collection, where id matches
    query = {"_id": ObjectId(id)}
    collection="patientNew"
    db.collection=db.db[collection]
    
    # result is a list
    result = db.fetch(query=query)
    
    # As we will get the list of documents, and 0th index will be our document
    # with patient id matching the one we have passed
    patient_doc = result[0]

    return render_template("updatepatient.html",
                           name=session["name"], 
                           email=session["email"], 
                           patient=patient_doc)

@web_app.route("/update-patient-in-db", methods=["POST"])
def update_patient_in_db():

    # Create a Dictionary with Data from HTML Register Form
    patient_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": request.form["age"],
        "address": request.form["address"],
        "doctor_email": session['email'],
    
        "created_on": datetime.datetime.now()
    }

    db.collection = db.db["patientNew"]

    query = {"_id": ObjectId(session["id"])}
    # Save Patient in DataBase i.e. MongoDB
    db.update(patient_data, query)
    # result = db.update(patient_data, query)

    return "done"
    # return render_template("success.html", message = "Patient Updated Successfully",
    #                        name=session["name"], email=session["email"])



@web_app.route("/delete-patient/<id>")
def delete_patient(id):
    print("Patinet to be deleted:", id)
    query = {"_id": ObjectId(id)}
    collection="patientNew"
    db.collection=db.db[collection]
    db.delete(query)
    return "Patient deleted successfully"
    # return render_template("success.html", message = "Patient Deleted Successfully",
    #                        name=session["name"], email=session["email"])



def main():
    # In order to use session tracking, create secreat key in app.object
    web_app.secret_key="Patient_managemnet-system"
    web_app.run(debug=True) 
     #it will run the program in loop which will not ends. in.run(PORTNO.) if empty it automatically allowcates debug=True

if __name__=="__main__":
    main()