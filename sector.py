import random as rand

# Sector Class

class Sector:
	def __init__(self, x, y, ruler="Indepented", speciality=None, capital=False):
		self.x = x
		self.y = y
		self.ruler = ruler
		self.speciality = speciality
		self.population = rand.randint(104, 24650)
		if ruler != None and capital == False:
			self.supporters = rand.randint(1, 108)
			self.rebels = 0
			self.neutrals = self.population - self.supporters
		elif ruler != None and capital == True:
			self.neutrals = rand.randint(1, 1050)
			self.supporters = self.population - self.neutrals
			self.rebels = 0
		
		
