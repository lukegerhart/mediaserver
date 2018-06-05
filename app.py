from flask import Flask, Response, jsonify, render_template
from PIL import Image
from utils import generateDir
import io
app = Flask(__name__)
basedir = '/media/pi/Seagate Backup Plus Drive1/'
@app.route('/')
def home():
    dir = generateDir(basedir)
    return render_template('home.html', dir=jsonify(dir))
def something():
    filename = 'Xiao Bai/AIMG_4202.JPG'
    im = Image.open(basedir+filename)
    bio = io.BytesIO()
    im.save(bio, format='JPEG')
    return Response(bio.getvalue(), mimetype='image/jpeg')



