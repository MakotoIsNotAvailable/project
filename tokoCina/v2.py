#Entah kenapa orang orang banyak membuat program kasir sederhana jadi gua ikutan deh hehe


#membuat system save data

import random
import os
import time


def load():
	cek = os.path.exists('data.csv') 
	Tjumlah = []
	for i in range(0,len(barang)):
		Tjumlah.append(0)
	#Membuat data baru
	if cek is False:
		print(f'Si Pembuat Memberi Anda Uang Sebesar 50,000 Rupiah')
		with open('data.csv','w') as f:
			w = csv.writer(f,delimiter=',')
			w.writerows('Tjumlah')
			f.close()
	
	




dompet = 50000
#dompet = 500000000000

#Template

def sp():
	print('-'*59)
def randstok(a):
#	try:
	return random.randint(0,a)
	
barang = [
	#Barang,harga,stok,keterangan
	['Pensil',1000,0,'2b'],
	['Pulpen',2000,randstok(100),'Pilott'],
	['Buku',3000,randstok(30),'Sidu'],
	['Aer Mineral',3000,randstok(20),'Aquah'],
	['Flask Disk',50000,1,'50GB'],
	['Play Station 10',10000000,10,'Sony'],
	['Suara Rakyat',1000000000,25000000,'Negri Odni'],
#	['Lampu',10000,]
]








Tjumlah = []
for i in range(0,len(barang)):
	Tjumlah.append(0)






def Nge():#Ngepet
	global dompet
	print('Berhubung Uang Sudah Habis Dan Tidak Ada Mekanisme Bekerja Di Program In Jadi Mari Kita Ngepet')
	batas = int(input('Masukkan Uang Yang Anda Inginkan: '))
	print('Sedang Ngepet Tunggu Hingga Selesai')
	while True:
		print(f'Uang Yang Terkumpul: {format(dompet,",")}')
		if dompet >= batas:
			break
		dompet += 1

#Tampilan
def view():
	#Toko
	a = 18
	b = 13
	c = 8
	d = 16
	# Holder
#	print('Selamat Datang Di Toko Cina')
	sp()
	print(f"|{'Nama Barang'.center(a)}|",end='')
	print(f"{'Harga(Rupiah)'.center(b)}",end='')
	print(f"|{'Stok'.center(c)}|",end='')
	print(f"{'Keterangan'.center(d)}|")
	sp()
	x = 0
	
	#Menampilkan Barang
	for i in barang:
		print(f"|{x+1}.{str(i[0]).ljust(a-2)}|{format(i[1],',').rjust(b)}|{str(i[2]).rjust(c)}|{str(i[3]).rjust(d)}|"); x += 1
	sp()
	
	#Tas
	print(f'|{"Isi Tas".ljust(a)}|{"Jumlah".center(b)}|'); sp(); x = 0
	for i in barang:
		print(f'|{i[0].ljust(a)}|{str(Tjumlah[x]).rjust(b)}|'); x += 1
	sp()
	print(f'Isi Dompet = {format(dompet,",")}|',end='')
	print('[ ! ]Pilih Barang Sesuai Nomor|')
	sp()
	


def userI():
	global dompet
	global barang
	global Tjumlah
	#Interaksi User
	while True:
		try:
				inputU = int(input('Mau Beli Apa? ').lower())
				if inputU > len(barang):
					print('Barang Tidak Ada ')
					continue
				ver = input('Yakin? [y/n] ')
				if ver == 'y':
					break
				else:
					continue
		except ValueError:
			print('Terjadi Kesalahan')
		
	if inputU >= 1 and inputU<= len(barang):
		dompet -= barang[inputU-1][1]
		barang[inputU-1][2] -= 1
		Tjumlah[inputU-1] += 1
		
		if dompet < 0:
			dompet += barang[inputU-1][1]
			barang[inputU-1][2] += 1
			Tjumlah[inputU-1] -= 1
			print('Uang Tidak Cukup')
		
		if barang[inputU-1][2] < 0:
			dompet += barang[inputU-1][1]
			barang[inputU-1][2] += 1
			Tjumlah[inputU-1] -= 1
			print('Stok Barang Habis')
	
	if input('ketik Sembarang Untuk Melanjutkan!') == '122912':
		print('🤨')





while True:
	os.system('clear')
	view()
	userI()
	time.sleep(1)


#Menulis kedalam file.txt
#read  input dari file.txt ke integer dan mengubahnya menjadi list



