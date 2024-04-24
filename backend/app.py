from flask import Flask, request, jsonify
#from api import FaceRecognitionAPI


#faceRecognitionAPI = FaceRecognitionAPI()
app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    print(data)
    username = data.get('username')
    photo = data.get('photo')
    #try:
    #    faceRecognitionAPI.register_user(username, photo)
    #except Exception:
    #    return jsonify({"failed"})
    return jsonify({'success'})


@app.route('/retrieve', methods=['POST'])
def retrieve_username():
    data = request.json
    photo = data.get('photo')
    #try:
    #    username = faceRecognitionAPI.detect_user(photo)
    #except Exception:
    #    return jsonify("failed")
    return jsonify({'username': username})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=40)
