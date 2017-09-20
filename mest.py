import csv
class Eit:
	def __init__(self, names, nationalities):
		self.names = names
		self.nationalities = nationalities

	def __repr__(self):
		return '''
		Names : {}
		Nationalities : {}'''.format(self.names, self.nationalities)

	def fun_facts(self):
		return "Hey python is cool, but php is the master"

class Fellows:
	def __init__(self, name, nationality):
		self.name = name
		self.nationality = nationality
		self.happiness = 0

	def __repr__(self):
		return '''
		Name : {}
		Nationality : {}'''.format(self.name, self.nationality)

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
				if eit[1] not in ['South Africa', 'Nigeria', "Cote d'ivoire", "Kenya", "Ghana"] :
					print('{} is not a valid eit'.format(eit[0]))				

sami = Eit('samuel', 'nigeria')
arinze = Eit('arinze', 'nigeria')
eit = []
fellow = []
Mest = School(eit, fellow)
Mest.check_eit('eits-2018.csv')
Mest.add_eit(sami)
Mest.add_eit(arinze)



