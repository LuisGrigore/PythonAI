from flask import Flask, request, jsonify
from back.model import Model
from back.services import Service

app = Flask(__name__)

try:
    model = Model("mnist_model.h5")
    service = Service(model,"recieved_digit.png")
except Exception as e:
    print(e)



@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/model', methods=['POST', 'GET'])
def process():
    return jsonify({"result": f"{str(service.classify(request.files['image'].read()))}"})

if __name__ == '__main__':
    app.run(debug=True)

