import os
import random
import time
import csv

op = '[ © ]'
kon = False
timer = False

def setup():
	global nilai
	global kon
	print(f'{op}Memeriksa Data...')
	cek = os.path.exists('Data')
	if timer is True: time.sleep(1)
	if cek is True:
		os.chdir('Data')
		cekh = os.path.exists('soal.py')
		cekhg = os.path.exists('__init__.py')
		cekgf = os.path.exists('log.csv')
		
		if cekh is True and cekhg is True:
			print(f'{op}Memuat Progres...')
			cekhj = os.path.exists('data.txt')
			if timer is True: time.sleep(2)
			
			if cekhj is True:
				with open('data.txt','r') as f:
					try:
						nilai = int(f.read())###
						kon = True
					except:
						print(f'{op}Terjadi Kesalahan Saat Membaca File!\n{op}Membuat Ulang File...')
			if cekgf is False:
						with open('log.csv','w') as log:
							logh = csv.writer(log,delimiter=',')
							logh.writerows([('Sekarang'),('Tanggal')])
						os.remove('data.txt')
						with open('data.txt','w') as f:
							f.write('0')
							nilai = 0
							kon = True
			else:
				print(f'{op}data.txt Tidak Ditemukan!\n{op}Membuat File Baru...')
				with open('data.txt','w') as f:
					f.write('0')
					nilai = 0
					kon = True


def main():
	while True:
		if nilai < 10:
			a1()
		elif nilai >= 10:
			a2()




setup()
if kon is True:
	if timer is True: time.sleep(0.5)
	print(f'{op}All Done;')
	print(f'{op}Nilai = {nilai}')
	if timer is True: time.sleep(0.5)
	for x in [3,2,1,0]:
		print(f'{op}Program Akan Dijalankan Dalam {x}')
		if timer is True: time.sleep(1)
	if timer is True: os.system('clear')
	from Data import *
	main()
else:
	print(f'{op}Data Tidak Ditemukan!\n{op}Tidak Bisa Menjalankan Program')