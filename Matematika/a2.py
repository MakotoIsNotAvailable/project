import os
import random
import time
#import marshal as mas

op = '[ © ]'
kon = False
print(f'{op}Memeriksa Data...')
time.sleep(1)
cek = os.path.exists('Data')
if cek is True:
	os.chdir('Data')
	cekh = os.path.exists('soal.py')
	cekhj = os.path.exists('data.txt')
	cekhg = os.path.exists('__init__.py')
	if cekh is True and cekhj is True and cekhg is True:
		print(f'{op}Memproses Data...')
		from Data import *
		with open('data.txt','r') as file:
			nilai = int(file.read())
			time.sleep(2)
		print(f'{op}All Done\n{op}')

	elif cekh is True and cekhg is True and cekhj is False:
		print(f'{op}Memproses Data...')
		time.sleep(1)
		print(f'{op}data.txt Tidak Di Temukan,Membuat data Baru...')
		with open('data.txt','w') as file:
			file.write('0')#### Pake Pickle
			nilai = 0
			time.sleep(1)
		from Data import *
		print(f'{op}All Done\n{op}')
	elif cekh is False or cekhg is False:
		print(f'{op}Data Tidak Ditemukan !')
		print(f'{op}Tidak Bisa Menjalankan Program')
		kon = True
else:
	print(f'{op}Data Tidak Ditemukan\n{op}Tidak Bisa Menjalankan Program')
	print('Tidak Bisa Menjalankan Program')
	kon = True

if kon is False:
	for i in [5,4,3,2,1]:
		print(f'{op}Program Akan Di Mulai Dalam {i}')
		time.sleep(1)
	print(op)




while True:
	with open('data.txt','r') as file:
		print('Nilai = ',file.read())
	a1()