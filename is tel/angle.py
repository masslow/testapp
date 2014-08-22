# Moduliai reikalingi programai:

import math
import os
    
# Skaiciuoja krypti ir atstuma iki taikinio:

class Calculate(object):

        def location(self, l, t): 
                return (l - t)

        def angle(self, lx, ly, tx, ty):                
                if (lx - tx) > 0:
                        return ((math.acos( (ly-ty) / (((lx-tx)**2)+((ly-ty)**2))**0.5 )) * (3200 / math.pi))
                elif (lx - tx) < 0:
                        return (3200 - ((math.acos( (ly - ty) / (((lx - tx)**2)+((ly - ty)**2))**0.5 )) * (3200 / math.pi)) + 3200)
                else:
                        return ((math.acos( (ly-ty) / (((lx-tx)**2)+((ly-ty)**2))**0.5 )) * (3200 / math.pi))

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
calc = Calculate()
print calc.angle(1,2,1,1)
