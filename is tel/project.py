# Moduliai reikalingi programai:

import math
import os
import urwid


# Skaiciuoja krypti ir atstuma iki taikinio:

class Calculate(object):

        def angle(self, tx, ty, lx, ly):                
                if (lx - tx) > 0:
                        return ((math.acos( (ly-ty) / (((lx-tx)**2)+((ly-ty)**2))**0.5 )) * (3200 / math.pi))
                elif (lx - tx) < 0:
                        return (3200 - ((math.acos( (ly - ty) / (((lx - tx)**2)+((ly - ty)**2))**0.5 )) * (3200 / math.pi)) + 3200)
                else:
                        return ((math.acos( (ly-ty) / (((lx-tx)**2)+((ly-ty)**2))**0.5 )) * (3200 / math.pi))

        def magnitude(self, lx, ly, tx, ty):
                return 10*float((((lx - tx)**2)+((ly - ty)**2))**0.5)

	def sutelkta(tarpas, atstumas):
		return (tarpas / atstumas) * 0.001
		
	def isskleista(frontas, atstumas):
		return (frontas / (5 * atstumas)) * 0.01

# Tai klase nustatanti stebetoju buvimo vieta ir ju taikini:

class SeekersNest(object):

	
	def __init__(self, x, y, vector, magnitude):
		self.x = float(x)
		self.y = float(y)
		self.vector = float(vector)
		self.magnitude = float(magnitude) / 10
		
		if vector == 6400 or vector == 3200:
			self.targetx = float(0)
			self.tarx = x

                if vector != 6400 and vector !=3200:
			self.targetx = float((magnitude * math.sin((vector  + 154) * (math.pi / 3200))))
			self.tarx = float(((magnitude / 10) * math.sin((vector + 154) * (math.pi / 3200)))) + x

		if vector == 1600 or vector == 4800:
			self.targety = float(0)
			self.tary = y
                
                if vector != 1600 and vector !=4800:
			self.targety = float((magnitude * math.cos((vector + 154) * (math.pi / 3200))))
			self.tary = float(((magnitude / 10) * math.cos((vector + 154) * (math.pi / 3200)))) + y
	
	def  kairiau(self, kiek):
		
		self.vector = (math.atan2((kiek / 10), self.magnitude) * (3200 / math.pi)) + ((math.atan2(self.targety, self.targetx)) * (3200 / math.pi))

		if self.vector == 6400 or self.vector == 3200:
			self.targetx = 0
			self.tarx = self.x

                if self.vector != 6400 and self.vector !=3200:
			self.targetx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200))))
			self.tarx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200)))) + self.x
		     
		if self.vector == 1600 or self.vector == 4800:
			self.targety = 0
			self.tary= self.y
                
                if self.vector != 1600 and self.vector !=4800:
			self.targety = float((self.magnitude * math.cos(self.vector * (math.pi / 3200))))
			self.tary = float((self.magnitude * math.cos(self.vector * (math.pi / 3200)))) + self.y

	
	def desiniau(self, kiek):
		
		self.vector = (math.atan2(self.targety, self.targetx) * (3200 / math.pi)) - ((math.atan2((kiek / 10), self.magnitude)) * (3200 / math.pi))

		if self.vector == 6400 or self.vector == 3200:
                    self.targetx = 0
		    self.tarx = self.x

                if self.vector != 6400 and self.vector !=3200:
                     self.targetx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200))))
		     self.tarx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200)))) + self.x
		     
		if self.vector == 1600 or self.vector == 4800:
                    self.targety = 0
		    self.tary = self.y
                
                if self.vector != 1600 and self.vector !=4800:
                    self.targety = float((self.magnitude * math.cos(self.vector * (math.pi / 3200))))
		    self.tary = float((self.magnitude * math.cos(self.vector * (math.pi / 3200)))) + self.y
	def plius(self, kiek):
	
		self.magnitude = self.magnitude + (kiek / 10)
		
		if self.vector == 6400 or self.vector == 3200:
                    self.targetx = 0
		    self.tarx = self.x

                if self.vector != 6400 and self.vector !=3200:
                     self.targetx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200))))
		     self.tarx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200)))) + self.x
		     
		if self.vector == 1600 or self.vector == 4800:
                    self.targety = 0
		    self.tary = self.y
                
                if self.vector != 1600 and self.vector !=4800:
                    self.targety = float((self.magnitude * math.cos(self.vector * (math.pi / 3200))))
		    self.tary = float((self.magnitude * math.cos(self.vector * (math.pi / 3200)))) + self.y
		
	def minus(self, kiek):
	
		self.magnitude = self.magnitude - (kiek / 10)
		
		if self.vector == 6400 or self.vector == 3200:
                    self.targetx = 0
		    self.tarx = self.x

                if self.vector != 6400 and self.vector !=3200:
                     self.targetx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200))))
		     self.tarx = float((self.magnitude * math.sin(self.vector * (math.pi / 3200)))) + self.x
		     
		if self.vector == 1600 or self.vector == 4800:
                    self.targety = 0
		    self.tary = self.y
                
                if self.vector != 1600 and self.vector !=4800:
                    self.targety = float((self.magnitude * math.cos(self.vector * (math.pi / 3200))))
		    self.tary = float((self.magnitude * math.cos(self.vector * (math.pi / 3200)))) + self.y


# Klase reikalinga valdyti duombaze

class DatabaseManage(object):
	
	def extract(self,db, m):
		txtFile = open(db, "r")
		mag = str(m) + ' '
		for line in txtFile:
			if mag in line:
				return int(line.strip( ' \n' ).replace(mag, ''))

# Klase, apvalinanti skaiciu iki 25 dalies ir grazinanti tarpa kuriame randasi apvalinamas skaicius			

class NumbRound(object):

	def __init__(self, number):
		self.numb = number
		self.rounded = int(round(round(number)/25) * 25)
		self.hundred = round(number/100) * 100

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
os.system('clear')
db = DatabaseManage()
calc = Calculate()
minx = raw_input("Minosvaidzio koordinates: \nX - ")
miny = raw_input("Y - ")
print "\n"
seekx = raw_input("Stebetoju koordinates: \nX - ")
seeky = raw_input("Y - ")
print "\n"
kryptis = raw_input("Kryptis : ")
atstumas = raw_input("Atstumas : ")
print "\n"
mina = raw_input("Minos tipas ( 1 - skeveldrine, 2 - dumine, 3 - apsvieciamoji ) : ")
veduokle = raw_input("Veduokle ( 1 - sutelkta, 2 - isskleista ) : ")
ob = SeekersNest(float(seekx), float(seeky), float(kryptis), float(atstumas))
print "\n"
print "Taikinio koordinates:", int(ob.tarx), int(ob.tary)
print "Atstumas iki taikinio:",  int(calc.magnitude(float(minx), float(miny), float(ob.tarx), float(ob.tary)))
rnd = NumbRound(int(calc.magnitude(float(minx), float(miny), float(ob.tarx), float(ob.tary))))
print "\n"
uztaisas = raw_input("Pasirinkite uztaisa ( 1: 800-1825m ; 2: 1000-2475m ; 3: 1300-3275m ; 4: 1500-4000m ; 5: 1800-4500m ; 6: 2100-5200m ; 7: 2300-5750m ; 8: 2500-6300m )\n")
print "\n"
print "Kampis:", int(calc.angle(float(minx), float(miny), float(ob.tarx), float(ob.tary))), "\nTaikiklis:", db.extract(uztaisas, rnd.rounded)

import npyscreen
class MainForm(npyscreen.FormBaseNew):
	
	def while_waiting(self):\

		ob = SeekersNest(self.stebx.get_value(), self.stebx.get_value(), self.kryptis.get_value(), self.atstumas.get_value())
		db = DatabaseManage()

		self.rodatstumas.value =  int(calc.magnitude(float(self.koordx.get_value()), float(self.koordy.get_value()), float(ob.tarx), float(ob.tary)))

		if self.veduokle.get_value() == [0]:
			self.tarp.value = 'Tarpas'
		if self.veduokle.get_value() == [1]:
			self.tarp.value = 'Frontas'
				
		self.display()
		
	def create(self):
		self.koordx = self.add(npyscreen.TitleText, name = 'X:', relx = 19, rely = 2, width=12, begin_entry_at=5)
		self.koordy = self.add(npyscreen.TitleText, name = 'Y:', relx = 19, rely = 3, width=12, begin_entry_at=5)
		self.rodatstumas = self.add(npyscreen.TitleText, name = 'Atstumas iki taikinio:', rely = 6, relx = 6, value = 3999, editable=False, begin_entry_at= 25)
		self.rodkoord = self.add(npyscreen.TitleText, name = 'Taikinio koordinates:', rely = 6, relx = 57, value = "1500   1233", editable=False, begin_entry_at= 24)
		self.stebx = self.add(npyscreen.TitleText, name = 'X:', relx = 62, rely = 2, width = 12, begin_entry_at=5)
		self.steby = self.add(npyscreen.TitleText, name = 'Y:', relx = 62, rely = 3, width = 12, begin_entry_at=5)
		self.kryptis = self.add(npyscreen.TitleText, name = 'Kryptis:', relx = 80, rely= 2, max_width=11, width = 11, begin_entry_at=12)
		self.atstumas = self.add(npyscreen.TitleText, name = 'Atstumas:', relx = 80, rely = 3, max_width=11, width = 12, begin_entry_at = 12)
		self.mina =  self.add(npyscreen.TitleSelectOne, max_height=4, value = [0], name="Mina", values = ["Skeveldrine","Apsvieciamoji", "Dumine"], scroll_exit=True, rely = 15, relx =4, begin_entry_at=12, max_width = 32)
		self.veduokle = self.add(npyscreen.TitleSelectOne, max_height=2, value = [0], name="Veduokle", values = ["Sutelkta","Isskleista"], scroll_exit=True, rely = 20, relx =4, begin_entry_at=12, max_width = 32)
		self.uztaisas = self.add(npyscreen.TitleSelectOne, max_height=9, value = [3], name="Uztaisas", values = ["Pirmas 800-1825m", "Antras 1000-2475m", "Trecias 1300-3275m", "Ketvirtas 1500-4000m", "Penktas 1800-4500m", "Sestas 2100-5200m", "Septintas 2300-5750m", "Astuntas 2500-6300m"], scroll_exit=True, rely = 24, relx =4, begin_entry_at=12, max_width = 40)
		self.tarp = self.add(npyscreen.TitleText, name = 'Tarpas', relx = 4, rely = 34, max_width=32, begin_entry_at = 17)
		self.koord = self.add(npyscreen.FixedText, value='Koordinates', relx = 4, max_width=14, rely =2, editable=False)
		self.steb = self.add(npyscreen.FixedText, value= 'Sekykla', relx = 50, rely = 2, max_width=12, editable=False)
		self.duomenys = self.add(npyscreen.BoxBasic, name = "Duomenys", values = ['testing'], rely = 10, relx = 50, max_width = 50, editable = False)
		
class MyApplication(npyscreen.NPSAppManaged):
	
	keypress_timeout_default = 3
	def onStart(self):
		N = self.addForm('MAIN', MainForm, name= 'Tampella 120mm')	
		N.edit()
	
	
	
if __name__ == '__main__':
	App = MyApplication().run()