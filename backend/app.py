from flask import Flask, request, jsonify
from api import FaceRecognitionAPI
import base64
from io import BytesIO
from PIL import Image
import re


faceRecognitionAPI = FaceRecognitionAPI()
app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    login = data.get('login')
    img64 = re.sub('^data:image/.+;base64,', '', data['img'])
    img = Image.open(BytesIO(base64.b64decode(img64)))
    faceRecognitionAPI.register_user(login, img)
    response = jsonify({'success': "true"})
    return response


@app.route('/login', methods=['POST'])
def retrieve_username():
    data = request.json
    img64 = re.sub('^data:image/.+;base64,', '', data['img'])
    img = Image.open(BytesIO(base64.b64decode(img64)))
    login = faceRecognitionAPI.detect_user(img)
    response = jsonify({"login": login})
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=40)
