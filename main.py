from flask import Flask,make_response,request
from bd import carros

app = Flask(__name__)


@app.route('/carros', methods = ['GET'])
def get_carros():
   # return carros
   # ultilizando o make_response 
   return make_response(carros) 

@app.route('/carros', methods = ['POST'])
def create_carro():
   carro = request.json()
   return carro

app.run(debug=True)