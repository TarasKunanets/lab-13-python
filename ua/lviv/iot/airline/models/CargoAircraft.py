# usr/bin/bash -tt
import os
from Airplane import Airplane
 
class CargoAircraft(Airplane):
	
	def __init__(self, name, seatsNumber, maxLoadCapacity, maxDistance, maxSpeed, flightRange, fuselageDiameter, loadingAndUnloadingSystem, cargoAircraftCategory):
		self.name = name
		self.seatsNumber = seatsNumber
		self.maxLoadCapacity = maxLoadCapacity
		self.maxDistance = maxDistance
		self.maxSpeed = maxSpeed
		self.flightRange = flightRange
		self.fuselageDiameter = fuselageDiameter
		self.loadingAndUnloadingSystem = loadingAndUnloadingSystem
		self.cargoAircraftCategory = cargoAircraftCategory
		
	@property
	def get_loadingAndUnloadingSystem(self):
		return self.loadingAndUnloadingSystem		
		
	def set_loadingAndUnloadingSystem(self, x):
		self.loadingAndUnloadingSystem = x
		
	@property
	def get_cargoAircraftCategory(self):
		return self.cargoAircraftCategory

	def set_cargoAircraftCategory(self, x):
		self.cargoAircraftCategory = x
	
		
def main():		
	cA = CargoAircraft('AbI-23', 120, 5000, 2000, 430, 1200, 9, True, "B1")
	print(cA.get_name)
	
	cA.set_name("NEwName")
	print(cA.get_name)

	print(cA.get_cargoAircraftCategory)
	
if __name__ == "__main__": main()

os.system("PAUSE")

