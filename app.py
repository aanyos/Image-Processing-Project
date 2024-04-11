import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import Image

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    #write the code from here
    operation_selection = request.form['image_type_selection']
    image_file = request.files['file']
    filename = secure_filename(image_file.filename)
    image_file.save(os.path.join('static/',filename))
    image = Image.open(image_file)
    #image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
    #image_flip.save(os.path.join('static/','flip.jpg'))
    #flipped_image = 'flip.jpg'

    if operation_selection == 'FLIP_LEFT_RIGHT':
        file_data = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif operation_selection == 'FLIP_TOP_BOTTOM':
        file_data = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif operation_selection == 'ROTATE_90':
        file_data = image.transpose(Image.ROTATE_90)
    elif operation_selection == 'ROTATE_180':
        file_data = image.transpose(Image.ROTATE_180)
    elif operation_selection == 'ROTATE_270':
        file_data = image.transpose(Image.ROTATE_270)
    
    else:
        print('No Image')

    #with open(os.path.join('static/', filename),
    #              'wb') as f:
    #    f.write(file_data)
    file_data.save(os.path.join('static/','image.jpg'))
    new_image = 'image.jpg'


    return render_template('upload.html', filename=new_image)





@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
