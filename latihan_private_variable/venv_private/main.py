class Hero:
	
	def __init__(self, name, health):

		# var instance private
		self.__name = name
		# var instanve public
		self.health = health

hero1 = Hero("Riki maru", 100)

print(hero1.__dict__)

