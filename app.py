from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import MongoClient
import bcrypt
#set app as a Flask instance 
app = Flask(__name__)
#encryption relies on secret keys so they could be run
app.secret_key = "testing"

client = MongoClient("mongodb+srv://M249388:MadhurilBhaskar@cluster0.whdth.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.get_database('total_records')

records = db.register

# #connect to your Mongo DB database
# def MongoDB():
#     client = MongoClient("mongodb+srv://M249388:MadhurilBhaskar@cluster0.whdth.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     db = client.get_database('total_records')
#     records = db.register
#     return records
# records = MongoDB()

@app.route("/", methods=['post','get'])
def index():
    message = ''
    #if method post in index
    if "fullname" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        # password2 = request.form.get("password2")
        #if found in database showcase that it's found 
        user_found = records.find_one({"fullname": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('mainLogin.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            # return render_template('mainLogin.html', message=message)
        # if password1 != password2:
        #     message = 'Passwords should match!'
        #     return render_template('index.html', message=message)
        else:
            #hash the password and encode it
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            #assing them in a dictionary in key value pairs
            user_input = {'name': user,'email':email, 'password': hashed}
            #insert it in the record collection
            records.insert_one(user_input)
            
            #find the new created account and its email
        
            user_data = records.find_one({"fullname": user})
            
            if user_data is not None:
                new_user = user_data['fullname']
                #if registered redirect to logged in as the registered user
                return render_template('user_dashboard.html', user=new_user)
    # return render_template('mainLogin.html')


if __name__ == "__main__":
    app.run(debug=True)