
# Program Ini Berfungsi Untuk Menulis Ulang Nama File 
# Menyimpan Daftar File Kedalam Variable
# Mengurutkan File
# Rename File

import os
from math import ceil

def sp(): print()

def ver(text):
	while True:
		try:
			return int(input(text)) - 1
		except ValueError:
			print('Pilih Folder Sesuai Angka')
			continue
		else: print('Terjadi Error Pada Fungsi ver()')#

#def bubblesort(alist):
#	for i in range(0,len(alist) - 1):
#		for j in range(len(alist)-1,i,-1):
#			if alist[j] < alist[j-1]:
#				temp = alist[j]
#				alist[j] = alist[j -1]
#				alist[j-1] = temp
#	return alist

# List Folder
def ld():
	return [i for i in os.listdir() if os.path.isdir(i) == True]

#List File
def lf(format = 'mp4'):
	##use len file 
	if format == 'all':
		#semua format
		a = [i for i in os.listdir() if os.path.isdir(i) == False]
		return sorted(a)
	
	#Dengan format
	a = [i for i in os.listdir() if os.path.isdir(i) == False and i.endswith(format)]
	return sorted(b)


def main():	
	listDir = ld()
	
	print('Daftar Folder:'); j = 1
	for i in listDir:
		if os.path.isdir(i):
			print(f'{j}.{i}'); j += 1
###
	sp()
	
	inputU = ver('Pilih Folder:')#Index list
	os.chdir(listDir[inputU])
	
	for i in lf('all'):
		print(i)
	
###
if __name__ == '__main__':
	main()