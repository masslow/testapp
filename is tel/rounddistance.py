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
		
