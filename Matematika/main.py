import os
import random
import time

op = "[ © ]"
program = False
timer = False

def turu(a):
	if timer is True: time.sleep(a)



print(f'{op}Memeriksa Data...')
cek = os.path.exists('Data')
if timer is True: time.sleep(1)
if cek is True: 
	os.chdir('Data')
	cekj = os.path.exists('soal.py')
	cekjh = os.path.exists('__init__.py')
	cekjhg = os.path.exists('file.txt')
	cekjhgf = os.path.exists('log.txt')
	if cekj is True and cekjh is True:
		program = True is False:
			print(f"{op}Tidak Ada Save File\n{op}Membuat File Baru")
			with open('file.txt',mode=w) as f:
				f.write('0')
				nilai = 0
		
		elif cekjhg is True:
			with open('file.txt','w') as f:
				nilai = int(f.read())
				
		if cekjhgf is False: #Log
			pass




#os.remove('file.txt')

while program:
	print('Anjay Bisa Jalan.')
	