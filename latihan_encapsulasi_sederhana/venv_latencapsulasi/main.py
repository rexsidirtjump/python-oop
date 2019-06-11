class Hero: 

	#private class variable
	__jumlah = 0

	def __init__(self, name, health, attack, armor):
		self.__name = name
		self.__starthealth = health
		self.__startattack = attack
		self.__startarmor = armor
		self.__level = 1
		self.__exp = 0

		self.__maxhealth = self.__starthealth * self.__level
		self.__attack = self.__startattack * self.__level
		self.__armor =  self.__startarmor * self.__level

		self.__health = self.__maxhealth

		Hero.__jumlah += 1

	@property
	def info(self):
		return "{} Level = {} \n\tHealth ={}/{} \n\tAttack = {} \n\tArmor = {}".format(self.__name,self.__level, self.__starthealth,self.__maxhealth,self.__attack,self.__armor)


	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self, addExp):
		self.__exp += addExp
		if(self.__exp >= 100):
			print(self.__name,'Level Up')
			self.__level += 1
			self.__exp -= 100

			self.__maxhealth = self.__starthealth * self.__level
			self.__attack = self.__startattack * self.__level
			self.__armor =  self.__startarmor * self.__level

	def attack(self, musuh):
		self.gainExp = 50

		

sniper = Hero("Sniper", 100, 5, 10)
riki = Hero("Riki Maru", 100, 5, 20)
print(sniper.info)
riki.attack(sniper)
riki.attack(sniper)
riki.attack(sniper)
print(riki.info)
