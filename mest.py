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

class Fellow(Person):
	fellow_counter = 0
	def __init__(self, name, nationalitie):
		if Fellow.fellow_counter < 4:
			super().__init__(name, nationalitie)
			self.happiness = 0
			Fellow.fellow_counter += 1
		else:
			raise Exception('We cannot afford to hire {}'.format(name))


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

	def add_fellow(self, fellow):
		self.fellows.append(fellow)

	def check_eit(self, file):
		try:
			with open(file) as file:
				for line in file:
					eit = line.split(',')
					if eit[1] not in ['South Africa', 'Nigeria', "Cote d'ivoire", "Kenya", "Ghana", "Zimbabwe"] :
						print('{} is not a valid eit'.format(eit[0]))		
		except Exception as e:
			print(e)				

andrew = Fellow('Andrew', 'USA')
faddai = Fellow('Francis', 'GH')
Kerry = Fellow('Kerry', 'USA')
Miishe = Fellow('Miishe', 'USA - GH')
Pascal = Fellow('Pascal', 'DRC')
Simpiwe = Fellow('Simpiwe', 'SA')
# eit = []
# fellow = []
# Mest = School(eit, fellow)
# Mest.add_fellow(andrew)
# Mest.add_fellow(faddai)
# Mest.add_fellow(Kerry)
# Mest.add_fellow(Miishe)
# Mest.add_fellow(Pascal)
# Mest.add_fellow(Simpiwe)
# Mest.check_eit('eits-2018.csv')




