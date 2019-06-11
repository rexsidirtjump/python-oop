class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

# class ini mengambil sifat class dari class Hero

class HeroIntelligent(Hero):
	pass

class HeroStrength(Hero):
	pass


lina = Hero("Lina", 100)
teaches = HeroIntelligent("Teaches", 50)
axe = HeroStrength("Axe", 200)

print(lina.name)
print(teaches.name)
print(axe.name)
