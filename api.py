import os
from IPython import embed
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/hello', methods=['GET'])
def hello():
  params = request.args
  if not params['name']:
    return '', 400
  response = {
      "message": 'Hello %s' % params['name']
    }
  return jsonify(response), 200
