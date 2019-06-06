# usr/bin/bash -tt
import os
from Airplane import Airplane
from ComfortLevel import ComfortLevel

class PassengerAircraft(Airplane):
	
	def __init__(self, name, seatsNumber, maxLoadCapacity, maxDistance, maxSpeed, flightRange, fuselageDiameter, wifi, comfortLevel):
		self.name = name
		self.seatsNumber = seatsNumber
		self.maxLoadCapacity = maxLoadCapacity
		self.maxDistance = maxDistance
		self.maxSpeed = maxSpeed
		self.flightRange = flightRange
		self.fuselageDiameter = fuselageDiameter
		self.wifi = wifi
		self.comfortLevel = comfortLevel
		
	@property
	def get_wifi(self):
		return self.wifi		
		
	def set_wifi(self, x):
		self.wifi = x
		
	@property
	def get_comfortLevel(self):
		return self.comfortLevel

	def set_comfortLevel(self, x):
		self.comfortLevel = x
	
		
def main():		
	pA = PassengerAircraft('AbI-23', 120, 5000, 2000, 430, 1200, 9, True, ComfortLevel.FIRST.value)
	
	#test name
	print(pA.get_name)	
	pA.set_name("NEwName")
	print(pA.get_name)
	
	#test enum
	print(pA.get_comfortLevel)
	
if __name__ == "__main__": main()

os.system("PAUSE")

