# Moduliai reikalingi programai:

import math
import os
    
# Skaiciuoja krypti ir atstuma iki taikinio:

class Calculate(object):

        def location(self, l, t): 
                return (l - t)

        def angle(self, difx, dify):                
                if difx < 0:
                        return (math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi)
                elif difx > 0:
                        return (3200 - ((math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi)) + 3200)
                else:
                        return (math.acos( dify / ((difx**2)+(dify**2))**0.5 )) * (3200 / math.pi)

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


# Klase reikalinga valdyti duombaze

class DatabaseManage(object):
	
	def extract(self,db, m):
		txtFile = open(db, "r")
		mag = str(m) + ' '
		for line in txtFile:
			if mag in line:
				return int(line.strip( ' \n' ).replace(mag, ''))

# Klase, apvalinanti skaiciu iki 25 dalies ir grazinanti tarpa kuriame randasi apvalinamas skaicius			

class QuarterRound(object):

	def __init__(self, number):
		self.numb = number
		self.rounded = round(number/25) * 25

	def higher(self):
		
		if self.rounded > self.numb:
			return self.rounded

		elif self.rounded < self.numb:
			return self.rounded + 25
		
	def lower(self):
		
		if self.rounded > self.numb:
			return self.rounded - 25
		
		elif self.rounded < self.numb:
			return self.rounded

	
# Programa:

calc = Calculate()
seek = SeekersNest(3042, 10020 , 1500, 1500)
print seek.tarx(3042, 10020 , 1500, 1500)
print seek.tary(3042, 10020 , 1500, 1500)
print 3042 + (seek.tarx(3042, 10020 , 1500, 1500) / 10)
print 10020 + (seek.tary(3042, 10020 , 1500, 1500) / 10)
db = DatabaseManage()
print db.extract(str(8), 3800)