# usr/bin/bash -tt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from CabinNarrow import CabinNarrow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

class Airplane(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), unique=True)
	seatsNumber = db.Column(db.Integer)
	maxLoadCapacity = db.Column(db.Integer)
	maxDistance = db.Column(db.Integer)
	maxSpeed = db.Column(db.Integer)
	flightRange = db.Column(db.Integer)
	fuselageDiameter = db.Column(db.Integer)
	cabinNarrow = db.Column(db.String(100))

	def __init__(self, name, seatsNumber, maxLoadCapacity, maxDistance, maxSpeed, flightRange, fuselageDiameter, cabinNarrow):
		self.name = name
		self.seatsNumber = seatsNumber
		self.maxLoadCapacity = maxLoadCapacity
		self.maxDistance = maxDistance
		self.maxSpeed = maxSpeed
		self.flightRange = flightRange
		self.fuselageDiameter = fuselageDiameter
		self.cabinNarrow = cabinNarrow

	def __repr__(self):
		return repr((self.name, self.seatsNumber, self.maxLoadCapacity, self.maxDistance, self.maxSpeed, self.flightRange, self.fuselageDiameter, self.cabinNarrow))

	@property
	def get_name(self):
		return self.name


	def set_name(self, x):
		self.name = x

	@property
	def get_seatsNumber(self):
		return self.seatsNumber

	def set_seatsNumber(self, x):
		self.seatsNumber = x

	@property
	def get_maxLoadCapacity(self):
		return self.maxLoadCapacity

	def set_maxLoadCapacity(self, x):
		self.maxLoadCapacity = x

	@property
	def get_maxDistance(self):
		return self.maxDistance

	def set_maxDistance(self, x):
		self.maxDistance = x

	@property
	def get_maxSpeed(self):
		return self.maxSpeed

	def set_maxSpeed(self, x):
		self.maxSpeed = x

	@property
	def get_flightRange(self):
		return self.flightRange

	def set_flightRange(self, x):
		self.flightRange = x

	@property
	def get_fuselageDiameter(self):
		return self.fuselageDiameter

	def set_fuselageDiameter(self, x):
		self.fuselageDiameter = x

	@property
	def get_cabinNarrow(self):
		return self.cabinNarrow

	def set_cabinNarrow(self, x):
		self.cabinNarrow = x

def main():
	print('work!')
if __name__ == "__main__": main()

os.system("PAUSE")
