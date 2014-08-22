# Moduliai reikalingi programai:

import math
import os
    
# Skaiciuoja krypti ir atstuma iki taikinio:

class Calculate(object):

        def location(self, l, t): 
                return (l - t) * -1

        def angle(self, difx, dify):                
                if difx < 0:
                        return (math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi)
                elif difx > 0:
                        return 3200 - ((math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi)) + 3200
                else:
                        return (math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi)

        def magnitude(self, difx, dify): 
                return 10*float(((difx**2)+(dify**2))**0.5)


# Tai klase nustatanti stebetoju buvimo vieta ir ju taikini:

class SeekersNest(object):
	
	       def __init__(self, x, y, vector, magnitude):
                self.tarx = (magnitude * math.sin(vector * (math.pi / 3200)))  *  -1
                self.tary = (magnitude * math.cos(vector * (math.pi / 3200)))  *  -1
                self.x = x
                self.y = y
                self.vector = vector
                self.magnitude = magnitude / 10

        	def changevector(self):
               self.vector = float(raw_input("Kryptis: "))
                
        def changemagnitude(self):
                self.magnitude = float(raw_input("Atstumas: "))

		
# Programa:
os.system('clear')

print "Skaiciuotojas. 6400 skale."
print " "
x = float(raw_input("Koordinates X: "))
y = float(raw_input("Koordinates Y: "))
os.system('clear')
seekx = float(raw_input("Stebetojai X: "))
seeky = float(raw_input("Stebetojai Y: "))
calc = Calculate()
nest = SeekersNest(seekx, seeky, float(raw_input("Kryptis: ")), float(raw_input("Atstumas: ")))
os.system('clear')
print 'Atstumas', int(calc.magnitude(calc.location(calc.location(x, seekx), nest.tarx), calc.location(calc.location(y, seeky), nest.tary))),'m'
print 'Kryptis', int(calc.angle(calc.location(calc.location(x, seekx), nest.tarx), calc.location(calc.location(y, seeky), nest.tary))