

class Lorentz:
	
	@staticmethod
	def info():
		print("Gaya Lorentz adalah gaya yang ditemukan oleh Hendrik Antoon.Gaya ini timbul akibat adanya arus listrik di dalam suatu medan magnet.Arah gaya Lorentz selalu tegak lurus dengan arah kuat arus listrik ( i ) dan induksi magnetik yang ada ( B )\n")
		print('Gaya Lirentz dirumuskan sebagai berikut:\nF = B × I × a\nKeterangan:\nF = gaya Lorentz, satuannya newton ( N )\nB = kuat medan magnet, satuannya tesla ( T )\na = panjang kawat, satuannya meter ( m )\nI = kuat arus listrik, satuannya ampere ( A )\n')
		print("Fungsi yang ada pada class ini yaitu:\n1.F() \n-Fungsi ini digunakan untuk menset nilai F pada rumus\n2.B() \n- Fungsi ini digunakan untuk menset nilai B pada rumus")
		
	# Setter	
	def set_F(self,N):
		self.__F == N
	
	def set_B(self,m):
		self.__B = m
	
	def set_I(self,A):
		self.__I = A
	
	def set_a(self,m):
		self.__a = m
	
	# Getter
	def F(self):
		return self.__B * self.__I * self.__a


a = Lorentz()


a.set_B(10)
a.set_I(0.002)
a.set_a(5)


print(a.F())