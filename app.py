from flask import Flask, Response, render_template
from PIL import Image
from utils import generateList
from conf import conf
import io, json
app = Flask(__name__)
basedir = conf['BASEDIR']
# basedir = '/media/pi/Seagate Backup Plus Drive1/'
# basedir = 'G:\\'
@app.route('/')
def home():
    dir = generateList(basedir)
    return render_template('index.html', dir=dir)
def something():
    filename = 'Xiao Bai/AIMG_4202.JPG'
    im = Image.open(basedir+filename)
    bio = io.BytesIO()
    im.save(bio, format='JPEG')
    return Response(bio.getvalue(), mimetype='image/jpeg')



