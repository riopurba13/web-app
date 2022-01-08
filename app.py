from flask import Flask, render_template, request
# import sqlite3 as sql
# conn = sql.connect('pendapatan.db')
# print ("membuat database baru");
# conn.execute('CREATE TABLE IF NOT EXISTS mingguan (id INTEGER NOT NULL PRIMARY KEY, biayaiklan INTEGER, keuntungan INTEGER)');
# print ("Tabel berhasil dibuat");
# conn.close()
app = Flask(__name__)
@app.route('/')
def home():
   return render_template('index.html')
# @app.route('/enternew')
# def new_student():
#    return render_template('datamingguan.html')
# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#    if request.method == 'POST':
#       try:
#          id = request.form['id']
#          bi = request.form['bi']
#          keu = request.form['keu']
                  
#          with sql.connect("pendapatan.db") as con:
#             cur = con.cursor()
#             cur.execute("INSERT INTO mingguan (id,biayaiklan,keuntungan) VALUES (?,?,?)",(id,bi,keu) )
#             con.commit()
#             msg = "Record berhasil ditambahkan"
#       except:
#          con.rollback()
#          msg = "error in insert operation"
      
#       finally:
#          return render_template("result.html",msg = msg)
#          con.close()
# @app.route('/list')
# def list():
#    con = sql.connect("pendapatan.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from mingguan")
   
#    rows = cur.fetchall();
#    return render_template("list.html",rows = rows)
if __name__ == '__main__':
   app.run(debug = True)


# from flask import Flask, render_template, request, send_from_directory
# from tensorflow.keras.models import load_model
# import numpy as np
# import os
# import cv2

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = './static/uploads/'
# model = load_model('Belimbing wuluh_dan_Nangka.h5')

# class_dict = {0: 'Belimbing wuluh', 1: 'Nangka'}


# def predict_label(img_path):
#     query = cv2.imread(img_path)
#     output = query.copy()
#     query = cv2.resize(query, (32, 32))
#     q = []
#     q.append(query)
#     q = np.array(q, dtype='float') / 255.0
#     q_pred = model.predict(q)
#     predicted_bit = int(q_pred)
#     return class_dict[predicted_bit]



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if request.files:
#             image = request.files['image']
#             img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
#             image.save(img_path)
#             prediction = predict_label(img_path)
#             return render_template('index.html', uploaded_image=image.filename, prediction=prediction)

#     return render_template('index.html')


# @app.route('/display/<filename>')
# def send_uploaded_image(filename=''):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# if '__name__' == '__main__':
#     app.run(debug=True)
