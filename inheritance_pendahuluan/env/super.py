class Hero:
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("{} dengan Health {}".format(self.name,self.health))

class HeroIntelligent(Hero):
	def __init__(self, name):

		#Hero.__init__(self, name , 100)
		#Super DI gunakan unutk menggunakan sifat dari class super
		super().__init__(name, 100)
		super().showInfo()

class HeroStrength(Hero):
	def __init__(self, name):
		#Hero.__init__(self, name, 200)
		#Super DI gunakan unutk menggunakan sifat dari class super
		super().__init__(name, 200)
		super().showInfo()



lina = HeroIntelligent("Lina")
axe = HeroStrength("Axe")

print(lina.name ," ", lina.health)
print(axe.name ," ", axe.health)

