from flask import Flask, request, jsonify
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET', 'POST'])
def classification():
      data = request.get_json()  #숫자가 문자로 넘어옴
      
      return_data = {
        "graph1": [random.randint(1,100) for _ in range(16)],
        "graph2": [random.randint(1,100) for _ in range(16)]
      }


      print(data) 
      return return_data


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
