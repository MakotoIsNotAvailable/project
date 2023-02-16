class enc:
	ls = []
	def tambah(self,awal,akhir):
		enc.ls.append([awal,akhir])
	
	def pring(self):
		for i in enc.ls():
			print()
			for j in i:
				print(f'No.{i}, chr = {chr(i)}')
one = enc()

def search(batas1,batas2):
	for i in range(batas1,batas2):
		print(f'No.{i}, chr = {chr(i)}')


one.tambah(33,136)
one.pring()

search(125,200)
