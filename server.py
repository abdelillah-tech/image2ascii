from flask import Flask, escape, request
from skimage.color import rgb2gray
from skimage.transform import rescale
import numpy as np
import jsonpickle
import cv2
import json

app = Flask(__name__)

def image_to_ascii(l, image) :
    chars = ["-", "/", "$"]
    n = len(chars)

    grayscale = rgb2gray(image)

    image_rescaled = rescale(grayscale, l/grayscale.shape[0], anti_aliasing=False)
    
    ascii_img = ""

    dectio = {round(i/n,1):i for i in range(n)}

    for i in image_rescaled :
        for j in i :
            ascii_img += " " + chars[dectio[round(int(j*n)/n, 1)]]
        ascii_img += "\n"

    return {'art' : ascii_img}


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST' :

        length = int(json.load(request.files['data'])['length'])

        nparr = np.fromstring(request.files['image'].read(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        res = jsonpickle.encode(image_to_ascii(length, img))
        return jsonpickle.encode(image_to_ascii(length, img))

    return f'Welcome to ascii art maker'