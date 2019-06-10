class Hero:

	# private class variable
	__jumlah = 0

	def __init__(self, name):
		self.__name = name
		Hero.__jumlah += 1

	# this method just valid on object
	def getJumlah(self):
		return Hero.__jumlah

	# this method can access using class  but no for object
	def getJumlah1():
		return Hero.__jumlah

	# method statis (decorator) add @staticmethod on top class, to acces def can acces using class and object no argument
	@staticmethod
	def getJumlah2():
		return Hero.__jumlah
	# classmethod for change class here to self, using argument
	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah

hero1 = Hero("sniper")
#print(Hero.getJumlah())
print(hero1.getJumlah2())
print(Hero.getJumlah2())

hero2 = Hero("sniper2")
hero3 = Hero("sniper3")
hero4 = Hero("sniper4")
print(hero2.getJumlah3())
