class DatabaseManage(object):
	
	def extract(self,db, m):
		txtFile = open(db, "r")
		mag = str(m) + ' '
		for line in txtFile:
			if mag in line:
				return str(line.strip( ' \n' ).replace(mag, ''))

			
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

while True:
	
	db = DatabaseManage()
	x = NumbRound(float(raw_input("Skaicius: ")))
	if x.numb > x.rounded:
		print int(round(float(db.extract('pirmas', x.rounded)) - (((float(db.extract('pirmas', x.higher())) - float(db.extract('pirmas', x.rounded)))/ 25) * float(x.rounded - x.numb))))
	if x.numb < x.rounded:
		print int(round(float(db.extract('pirmas', x.rounded)) - (((float(db.extract('pirmas', x.rounded)) - float(db.extract('pirmas', x.lower())))/ 25) * float(x.rounded - x.numb))))
	if x.numb == x.rounded:
		print int(db.extract('pirmas', x.rounded))