#!/usr/bin/env python3
import os
import sys
sys.path.insert(0,'D:\\Python\\labs\\Python-Lab-11\\__main__\\python\\ua\\lviv\\iot\\airline\\models')
from CabinNarrow import CabinNarrow
from Airplane import Airplane 
from PassengerAircraft import PassengerAircraft


class AirlineManagerImplementation:
	airplane_list = []
	
	@staticmethod
	def getList():
		return AirlineManagerImplementation.airplane_list

	@staticmethod
	def sortByMaxSpeed(is_reversed):
		AirlineManagerImplementation.airplane_list.sort(key=lambda airplane: airplane.maxSpeed, reverse=is_reversed)
			
	@staticmethod	
	def sortByMaxDistance(is_reversed):
		AirlineManagerImplementation.airplane_list.sort(key=lambda airplane: airplane.maxDistance, reverse=is_reversed)
			
	@staticmethod	
	def setNewListOfAirplanes(airplanes):
		AirlineManagerImplementation.airplane_list = airplanes
	
	@staticmethod
	def clearAirplanes():
		AirlineManagerImplementation.airplane_list.clear()
	
	@staticmethod
	def addAirplane(airplane):
		AirlineManagerImplementation.airplane_list.append(airplane)
	
	@staticmethod
	def countMaxLoadCapacity():
		return sum([p.get_maxLoadCapacity for p in AirlineManagerImplementation.airplane_list])

	@staticmethod	
	def countSeats(x):
		return x.get_seatsNumber
	
	@staticmethod
	def printListOfAirplanes():
		for v in AirlineManagerImplementation.airplane_list:
			print(" "+v.get_name+"\n")
			print("name: %s, seats: %d\n" % (v.get_name, v.get_seatsNumber))
			print("name: {:*^80}, seats: {}".format())
		
def main():	

	#dic = {1:10, 2:20, 3:30, 4:40}
	#print(sum([v for k,v in dic.items() if not k & 1]))
	
	m = AirlineManagerImplementation()
	airplane1 = Airplane('Alexa', 120, 3000, 2100, 330, 1000, 9, CabinNarrow.FIVEABREAST.value)
	airplane2 = Airplane('Pico', 130, 5000, 2200, 420, 800, 3, CabinNarrow.FIVEABREAST.value)
	airplane3 = Airplane('Qive', 110, 4000, 2050, 400, 1040, 5, CabinNarrow.FIVEABREAST.value)
	m.addAirplane(airplane1)
	m.addAirplane(airplane2)
	m.addAirplane(airplane3)	
	
	m.printListOfAirplanes()
	print("\n"+"."*20)
	m.sortByMaxDistance(True)
	m.printListOfAirplanes()
	print("\n"+"."*20)
	m.sortByMaxDistance(False)
	m.printListOfAirplanes()
	
	print(m.countMaxLoadCapacity())

if __name__ == "__main__": main()

os.system("PAUSE")