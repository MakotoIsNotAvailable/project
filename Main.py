import os
import math


def ver(text:str):
	while True:
		try:
			return int(input(text))
		except ValueError:
			print('Pilih Folder Sesuai Angka')
			continue
		else: print('Terjadi Error Pada Fungsi ver()')



#List File
def lf(format = 'all'):
	if format == 'all':
		#semua format
		a = [i for i in os.listdir() if os.path.isdir(i) == False]
		return a
	
	#Dengan format
	else:
		return [i for i in os.listdir() if os.path.isdir(i) == False and i.endswith(format)]




def main(format = 'all'):#
	listdir = [i for i in os.listdir() if os.path.isdir(i) == True]
	#View
	print('Daftar Folder:'); j = 1
	for i in listdir:
		print(f'{j}.{i}'); j += 1
	
	
	while True:
		try:
			inputU = ver('\nPilih Folder:') - 1
			os.system('clear')
			print(f'Nama Folder\t:{listdir[inputU]}')
			os.chdir(listdir[inputU])
			break
		except IndexError:
			print("Di Luar Index")
	
	
	size = 0
	for i in lf():
		size += math.ceil(os.path.getsize(i))/1024/1024
		
	bt = 'MB'
	if size >= 1000: size /= 1024; bt = "GB"
	print(f"Ukuran Folder\t:{math.ceil(size)}{bt}")
	if size > 0:
		print(f"Rata-Rata/File\t:{math.ceil(size/len(lf()))}MB")
	print('File\t\t:')
	for i in sorted(lf()):
		if i.startswith("."): continue
		print(f'  {i}')
	
	
	#Rename File
	if os.path.exists('.dummy') == False:
		if input("Rename? [y/n] ") == "y":
			j = 1#Episode
			for i in sorted(lf()):
				os.rename(i,f'Episode0{j}.{format}'); j += 1
		#Update Later
		#If len(file) >= 9: file name = Episode010
		
		
		input("Rename Complete!")
		print("File\t:")
		for i in sorted(lf()):
			print(f"   {i}")
		with open('.dummy','w') as file:
			pass
	else:
		print("Tidak Bisa Rename!\nFile Sudah Di Rename Sebelumnya")
###
if __name__ == '__main__':
	while True:
		os.system('clear')
		main('mp4')#format file
		input("Pause")
		os.chdir('..')