class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		#self.info =  "name = {} \n \thealth = {}"  .format(self.__name,self.__health)

	#decorator property merubah method seperti variable private
	@property
	def info(self):
		return  "name = {} \n\thealth = {} \n\tarmor = {}"  .format(self.name,self.__health,self.__armor)

	@property
	def armor(self):
		pass

	@armor.getter
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self, input):
		self.__armor = input

	@armor.deleter
	def armor(self):
		print("Armor Di Delete")
		self.__armor  = None




sniper = Hero("sniper", 100, 20)

print(sniper.info)
sniper.name = "Riki maru"
print(sniper.info)
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)
del sniper.armor
print(sniper.__dict__)
print(sniper.armor)
