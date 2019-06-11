class Hero:
	def __init__(self, name, health):
		self.name = name
		self.health = health 

	def showInfo(self):
		print("{} Health {}".format(self.name, self.health))

class HeroIntelligent(Hero):
	def __init__(self, name):
		super().__init__(name, 100)

	#Override showInfo
	def showInfo(self):
		print("{} Health {}, Type = Intelligent".format(self.name, self.health))


class HeroStrength(Hero):
	def __init__(self, name):
		super().__init__(name, 200)

sniper = HeroIntelligent("Sniper")
axe = HeroStrength("Axe")

axe.showInfo()
sniper.showInfo()
