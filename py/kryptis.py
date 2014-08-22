# Moduliai reikalingi programai:

import math
import os
    
# Skaiciuoja krypti ir atstuma iki taikinio:

class Calculate(object):

        def location(self, l, t): 
                return (l - t)

        def angle(self, difx, dify):                
                if difx < 0:
                        return 6400 - ((math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi))
                elif difx > 0:
                        return 6400 - (3200 - ((math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi)) + 3200)
                else:
                        return 6400 - ((math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi))

        def magnitude(self, difx, dify):
                return 10*float(((difx**2)+(dify**2))**0.5)


# Tai klase nustatanti stebetoju buvimo vieta ir ju taikini:

class SeekersNest(object):
	
	def __init__(self, x, y, vector, magnitude):
		self.x = x
		self.y = y
		self.vector = vector
		self.magnitude = magnitude
		
	def tarx(self, x, y, vector, magnitude):
            
                if vector == 6400 or vector == 3200:
                    return self.x

                else:
                    return (magnitude * math.sin(vector * (math.pi / 3200)))

        def tary(self, x, y, vector, magnitude):
            
                if vector == 1600 or vector == 4800:
                    return self.y
                
                else:
                    return (magnitude * math.cos(vector * (math.pi / 3200)))

	def changevector(self):
                self.vector = float(raw_input("Kryptis: "))
                
        def changemagnitude(self):
                self.magnitude = float(raw_input("Atstumas: "))

		
# Programa:
os.system('clear')

print "Krypties nustatytojas. 6400 skale."
print " "
x = 0
y = 0
seek = SeekersNest(x, y, float(raw_input("Kryptis: ")), float(raw_input("Atstumas: ")))
print seek.tarx(seek.x, seek.y, seek.vector, seek.magnitude)
print seek.tary(seek.x, seek.y, seek.vector, seek.magnitude)
