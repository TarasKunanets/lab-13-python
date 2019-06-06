from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import sys
sys.path.insert(0,'D:\\Projects\\Python\\Python-Lab-13\\ua\\lviv\\iot\\airline\\models')
from Airplane import Airplane


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Product Schema
class AirplaneSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'seatsNumber', 'maxLoadCapacity', 'maxDistance', 'maxSpeed', 'flightRange', 'fuselageDiameter', 'cabinNarrow')

# Init schema
airplane_schema =  AirplaneSchema(strict=True)
airplanes_schema =  AirplaneSchema(many=True, strict=True)

# Create a Product
@app.route('/airplane', methods=['POST'])
def add_airplane():
  name = request.json['name']
  seatsNumber = request.json['seatsNumber']
  maxLoadCapacity = request.json['maxLoadCapacity']
  maxDistance = request.json['maxDistance']
  maxSpeed = request.json['maxSpeed']
  flightRange = request.json['flightRange']
  fuselageDiameter = request.json['fuselageDiameter']
  cabinNarrow = request.json['cabinNarrow']

  new_airplane = Airplane(name, seatsNumber, maxLoadCapacity, maxDistance, maxSpeed, flightRange, fuselageDiameter, cabinNarrow)

  db.session.add(new_airplane)
  db.session.commit()

  return airplane_schema.jsonify(new_airplane)

# Get All Products
@app.route('/airplane', methods=['GET'])
def get_airplanes():
  all_airplanes = Airplane.query.all()
  result = airplanes_schema.dump(all_airplanes)

  return jsonify(result.data)

# Get Single Products
@app.route('/airplane/<id>', methods=['GET'])
def get_airplane(id):
  airplane = Airplane.query.get(id)

  return airplane_schema.jsonify(airplane)

# Update a Product
@app.route('/airplane/<id>', methods=['PUT'])
def update_airplane(id):
  airplane = Airplane.query.get(id)

  name = request.json['name']
  seatsNumber = request.json['seatsNumber']
  maxLoadCapacity = request.json['maxLoadCapacity']
  maxDistance = request.json['maxDistance']
  maxSpeed = request.json['maxSpeed']
  flightRange = request.json['flightRange']
  fuselageDiameter = request.json['fuselageDiameter']
  cabinNarrow = request.json['cabinNarrow']

  airplane.name = name
  airplane.name = name
  airplane.seatsNumber = seatsNumber
  airplane.maxLoadCapacity = maxLoadCapacity
  airplane.maxDistance = maxDistance
  airplane.maxSpeed = maxSpeed
  airplane.flightRange = flightRange
  airplane.fuselageDiameter = fuselageDiameter
  airplane.cabinNarrow = cabinNarrow

  db.session.commit()

  return airplane_schema.jsonify(airplane)

# Delete Product
@app.route('/airplane/<id>', methods=['DELETE'])
def delete_airplane(id):
  airplane = Airplane.query.get(id)
  db.session.delete(airplane)
  db.session.commit()

  return airplane_schema.jsonify(airplane)

# Run Server
if __name__ == '__main__':
  app.run(debug=True, use_reloader=False)
