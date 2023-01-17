

class Raport:
	def __init__(self,nama,nisn):
		self.nama = nama
		self.nisn = nisn
	
	def setNilaiPraktek(self,qh):
		self.__AlQuranHadistP = qh
		
	
	def setNilaiKeterampilan(self,h):
		self.__AlquranHadistK = qh
	
	def info():
		print(f'''
		Al Quran Hadist = {self.AlQuranHadist
		''')


aspian7Ganjil = Raport('aspian','0083936728')

aspian.setNilaiPraktek(9)

aspian.info()
