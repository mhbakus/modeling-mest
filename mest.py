import csv
class Person:
	def __init__(self, name, nationalitie):
		self.name = name
		self.nationalitie = nationalitie

	def __repr__(self, name, nationalitie):
		return '''
		Names : {}
		Nationalities : {}'''.format(self.name, self.nationalitie) 


class Eit(Person):
	def __init__(self, name, nationalitie):
		super().__init__(name, nationalitie)

	def __repr__(self):
		super().__repr__(self)

	def fun_facts(self):
		return "Hey python is cool, but php is the master of the web"

class Fellows(Person):
	def __init__(self, name, nationalitie):
		super().__init__(name, nationalitie)
		self.happiness = 0

	def __repr__(self):
		super().__repr__(self)

	def eat(self):
		self.happiness += 1

	def teach(self):
		self.happiness -= 1


class School:
	def __init__(self, eits = [], fellows = []):
		self.eits = eits
		self.fellows = fellows
	def add_eit(self, eit):
			self.eits.append(eit)

	def print_all_eits(self):
		for eit in self.eits:
			print(eit)

	def check_eit(self, file):
		with open(file) as file:
			for line in file:
				eit = line.split(',')
				if eit[1] not in ['South Africa', 'Nigeria', "Cote d'ivoire", "Kenya", "Ghana", "Zimbabwe"] :
					print('{} is not a valid eit'.format(eit[0]))				

sami = Eit('samuel', 'nigeria')
arinze = Eit('arinze', 'nigeria')
eit = []
fellow = []
Mest = School(eit, fellow)
Mest.check_eit('eits-2018.csv')
Mest.add_eit(sami)
Mest.add_eit(arinze)



