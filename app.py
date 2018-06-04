from flask import Flask, Response
from PIL import Image
import io
app = Flask(__name__)

@app.route('/')
def home():
    basedir = '/media/pi/Seagate Backup Plus Drive/'
    filename = 'Xiao Bai/AIMG_4202.JPG'
    im = Image.open(basedir+filename)
    bio = io.BytesIO()
    im.save(bio, format='JPEG')
    return Response(bio.getvalue(), mimetype='image/jpeg')



