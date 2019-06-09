class Hero:
	#main def	
	def __init__(self, name, health, attack):
		self.__name = name
		self.__health = health
		self.__attack = attack
	# Getter to get name from private instance variable
	def getName(self):
		return self.__name
	# Getter to get health from private instance variable
	def getHealth(self):
		return self.__health
	# Setter
	def diserang(self, serangan):
		self.__health -= serangan

hero1 = Hero("eartshaker",100,10)

print(hero1.getName())
print(hero1.getHealth())
hero1.diserang(5)
print(hero1.getHealth())

