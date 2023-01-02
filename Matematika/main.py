import random
import os


cek = os.path.exists('data.txt')
if cek is False:
	with open('data.txt',mode='w') as file:
		file.write('0')

#

#


with open('data.txt','r') as file:
	nilai = int(file.read())


def soal1():
	global nilai
	a = random.randint(0,99)
	b = random.sample(range(0,a),1)
	q = ''.join(random.sample('+-',1))
	print(f'[ ~ ] {a} {q} {b[0]} = ')
	jawab = int(input('Jawab: '))
	if jawab == 1+1:
		print('Jawaban Benar')
		nilai += 1
	else:
		print('Jawaban Salah')
		



while True:
	print(f'Nilai = {nilai}')
	soal1()




#Ketika Program Baru Di Jalankan, Program Akam Mengecek Apakah Ada Data File Yang Bernama data.txt
#Jika Tidak Ada Maka Program Akan Membuat File Dengan Nama data.txt Dan Menulis Kedalam Text Tersebut Nama Dam Nilai, Nama Di Ambil Dari Input,Sedangkan Nilai Adalah 0
#Jika Ada Maka Program Akan Memindahkan Nama Dan Nilai Ke Dalam Sebuah Variable