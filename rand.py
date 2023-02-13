class Hero:
	__count = 0
	def __init__(self, name, health, attack, defense):
		self.__name = name
		self.__health = health
		self.__attack = attack
		self.__defense = defense
		self.__level = 0
		self.__exp = 0
		Hero.__count += 1
		
	def buff(dummy):
		self.__health + (dummy * self.__level)		

	def debuff(dummy):
		self.__health -= (dummy/self.__level)
	
	def get_name(self):
		return self.__name

	def get_health(self):
		return self.__health
	
	def get_armor(self):
		return self.__defense
	
	
	def attack(self,orang):
		dampakD = (self.__attack / orang.__defense)
		orang.__health -= dampakD
		dampakP = (self.__attack / orang.__defense)
		orang.__defense -= dampakP
		print(f"{orang.get_name()} Telah Di Serang Oleh {self.get_name()}")
		
		print(f"Health {orang.get_name()} Berkurang Sebesar {dampakD}\nArmor {orang.get_name()} Berkurang Sebesar {dampakP}")



yuusha = Hero("Carla",100,20,10)
party = Hero("Survivor",1000,50,5)

print(f"""\n
Yuusha Darah = {yuusha.get_health()}
Party Darah = {party.get_health()}
""")


yuusha.attack(party)

print(f"""\n
Yuusha Darah = {yuusha.get_health()}
Party Darah = {party.get_health()}
""")