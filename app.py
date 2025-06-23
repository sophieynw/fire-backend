from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

############
## for deployment, uncomment the following lines to download the model from S3

import urllib.request
from dotenv import load_dotenv
load_dotenv()
model_url = os.environ.get("MODEL_URL")
model_path = "/tmp/fire_model.pkl"
if not os.path.exists(model_path):
    urllib.request.urlretrieve(model_url, model_path)
model = joblib.load(model_path)
##############

##############
## for local development, load the model from the local file system

# model_path = os.path.join(os.path.dirname(__file__), 'fire_model.pkl')
# model = joblib.load(model_path)
##############

# create get request
@app.route('/api', methods=['GET'])
def index():
  return jsonify({'message': 'Welcome to the Fire Model API!'}), 200

# create post request
@app.route('/api', methods=['POST'])
def test():
  if request.is_json:
    record = request.get_json()
    record_array = np.array([list(record.values())])
    result = model.predict(record_array)
    return jsonify({'result': result.tolist()})
  else:
    return jsonify({'error': 'Request must be JSON'}), 400
  
if __name__ == '__main__':
  app.run()