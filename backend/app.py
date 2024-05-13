from flask import Flask, request, jsonify
from api import FaceRecognitionAPI
import base64
from io import BytesIO
from PIL import Image
import re


faceRecognitionAPI = FaceRecognitionAPI()
app = Flask(__name__)


@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Hello, world!"


@app.route("/auth")
def auth_welcome():
    """Function to test the functionality of the API"""
    return "Hello, world!"


@app.route('/auth/register', methods=['POST'])
def register_user():
    data = request.json
    login = data.get('login')
    img64 = re.sub('^data:image/.+;base64,', '', data['img'])
    img = Image.open(BytesIO(base64.b64decode(img64)))
    try:
        faceRecognitionAPI.register_user(login, img)
        response = jsonify({'success': "true"})
    except Exception as e:
        response = jsonify({'success': "false", 'message': str(e)})
        response.status_code = 409
    return response


@app.route('/auth/login', methods=['POST'])
def retrieve_username():
    data = request.json
    img64 = re.sub('^data:image/.+;base64,', '', data['img'])
    img = Image.open(BytesIO(base64.b64decode(img64)))
    try:
        login = faceRecognitionAPI.detect_user(img)
        response = jsonify({"login": login})
    except Exception as e:
        response = jsonify({'success': "false", 'message': str(e)})
        response.status_code = 409
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=40)
