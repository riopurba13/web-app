from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
import numpy as np
import os
import cv2
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static/uploads/..')
model = load_model('Belimbing wuluh_dan_Nangka.h5')

class_dict = {0: 'Belimbing wuluh', 1: 'Nangka'}


def predict_label(img_path):
    query = cv2.imread(img_path)
    output = query.copy()
    query = cv2.resize(query, (32, 32))
    q = []
    q.append(query)
    q = np.array(q, dtype='float') / 255.0
    q_pred = model.predict(q)
    predicted_bit = int(q_pred)
    return class_dict[predicted_bit]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(img_path)
            prediction = predict_label(img_path)
            return render_template('index.html', uploaded_image=image.filename, prediction=prediction)

    return render_template('index.html')


@app.route('/display/<filename>')
def send_uploaded_image(filename=''):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if '__name__' == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(debug=True, host='0.0.0.0', port=port)
    # app.run(debug=True)
