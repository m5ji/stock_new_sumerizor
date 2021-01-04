import os
from flask import Flask, escape, request, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
APP_PORT = os.getenv('APP_PORT')

@app.route('/hello', methods=['GET'])
@cross_origin()
def hello():
    name = request.args.get("name", "World")
    return {
        'result': f'Hello, {escape(name)}!'
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=APP_PORT)
