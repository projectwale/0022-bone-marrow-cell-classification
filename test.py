from flask import Flask,render_template,request,session, url_for, redirect ,flash,jsonify
#from flask_mysqldb import MySQL
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
#from sklearn import datasets
import pymysql
import numpy as np
import tensorflow as tf
import cv2
import os
from werkzeug.utils import secure_filename
# from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'any random string'
model = load_model('EfficientNetB7.hp5')

def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="bonemarrow")
    return connection

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
        
                  
con = dbConnection()
cursor = con.cursor()


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    return render_template('index.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service',methods=['POST','GET'])
def service():
    if request.method == "POST":
       print("===============================================")
       file = request.files['file']

       filename = secure_filename(file.filename)
       print(filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       img = cv2.imread("static/uploads/"+str(filename))
       

       image_size=224
       #img = cv2.imread(path1+"//"+i)
       path="static/uploads/"+"//"+str(filename)
       img = image.load_img(path, target_size=(image_size, image_size))
       x = image.img_to_array(img)
       print(type(x))
       img_4d=x.reshape(1,224,224,3)
      
       predictions = model.predict(img_4d)
       print(predictions)
       pred=np.argmax(predictions[0])
       print("===============================================")
       print(pred)
       print("===============================================")
       dict1 = {0:'ART',1:'BLA',2:'EBO',3:'EOS',4:'LYT',5:'MMZ',6:'MON',7:'MYB',8:'NGB',9:'NGS',10:'NIF',11:'PEB',12:'PLM',13:'PMO'}
       op=dict1[pred]
       
       if  op=="0":
            final_prediction = "Artefact"
            message = "The bone marrow cell is classified as "+ final_prediction
            
            print(final_prediction)
            print(message)
            print(path)
            
            user_dict = {
                "message":message,
                "final_prediction":final_prediction,
                "Image_path":path
            }
            
            return jsonify(user_dict)
        
       if  op=="1":
            final_prediction = "Blast"
            message = "The bone marrow cell is classified as "+ final_prediction
            user_dict = {
                "message":message,
                "final_prediction":final_prediction,
                "Image_path":path
            }
            
            return jsonify(user_dict)
            
            
       if  op=="2":
            final_prediction = "Erythroblast"
            message = "The bone marrow cell is classified as "+ final_prediction
            user_dict = {
                "message":message,
                "final_prediction":final_prediction,
                "Image_path":path
            }
            
            return jsonify(user_dict)
            
       if  op=="3":
             final_prediction = "Eosinophil"
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
            
             
       if  op=="4":
             final_prediction = "Lymphocyte"
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
            
             
       if op=="5":
             final_prediction = "Metamyelocyte" 
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
             
       if  op=="6":
            final_prediction = "Monocyte"
            message = "The bone marrow cell is classified as "+ final_prediction
            user_dict = {
                "message":message,
                "final_prediction":final_prediction,
                "Image_path":path
            }
            
            return jsonify(user_dict)
        
        
            
       if  op=="7":
             final_prediction = "Myelocyte"
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
            
             
       if  op=="8":
             final_prediction = "Band neutrophil"
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
            
             
       if op=="9":
             final_prediction = "Segmented neutrophilt" 
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
            
             
       if  op=="10":
            final_prediction = "Not identifiable"
            message = "The bone marrow cell is classified as "+ final_prediction
            user_dict = {
                "message":message,
                "final_prediction":final_prediction,
                "Image_path":path
            }
            
            return jsonify(user_dict)
        
        
            
       if  op=="11":
             final_prediction = "Proerythroblast"
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
            
             
       if  op=="12":
             final_prediction = "Plasma cell"
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         
            
             
       if op=="13":
             final_prediction = "Promyelocyte" 
             message = "The bone marrow cell is classified as "+ final_prediction
             user_dict = {
                 "message":message,
                 "final_prediction":final_prediction,
                 "Image_path":path
             }
             
             return jsonify(user_dict)
         

       
       print("===============================================")
       
      
     
    return render_template('service.html')



@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
        details = request.form
        username = details['username']
        email = details['email']
        password1 = details['password']
        mobile= details['mobno']
        address = details['address']
        
        sql2  = "INSERT INTO register(username,email,password,mobileno,address) VALUES (%s, %s, %s, %s, %s)"
        val2 = (str(username),  str(email), str(password1), str(mobile), str(address))
        cursor.execute(sql2,val2) 
        con.commit()
        print("username",username)
        return redirect(url_for('login'))
 
    return render_template('register.html') 
 
@app.route('/login', methods=["GET","POST"])
def login():
    msg = ''
    if request.method == "POST": 
            username = request.form.get("username")
            print ("username",username)
            password = request.form.get("password")   
            print ("password",password)
            con = dbConnection()
            cursor = con.cursor()
            cursor.execute('SELECT * FROM register WHERE username = %s AND password = %s' , (username, password))
            result = cursor.fetchone()
            print ("result",result)
            if result:
                session['user'] = result[0]
                
                return redirect(url_for('home'))
     
            else:
                msg = 'Incorrect username/password!'
                return redirect(url_for('register'))
                
      
    return render_template('login.html')

    
# @app.route('/forgotpass', methods=["GET","POST"])
# def forgotpass():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
       
#         print ("username",username)
#         print ("password",password)
#         con = dbConnection()
#         cursor = con.cursor()
       
#         sql_update_query = "Update register set password = %s where username = %s"
#         input_data = (password, username)
#         cursor.execute(sql_update_query, input_data)
#         con.commit()
#         return redirect(url_for('login'))
#     return render_template('forgotpassword.html')
 
if __name__ == "__main__":
    # app.run(debug=True)
    app.run("0.0.0.0")