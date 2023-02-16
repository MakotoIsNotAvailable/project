print('Memuat Program...')

# Import module 
import os
import random
import time
import csv


# Load data user dari file txt/csv
def load():
	pass

# #Save data user dari file txt/csv
def save():
	pass

# #Bilangan random untuk soal
def randnum(a=0,b=100):
	return random.randint(a,b)

# Fungsi Tambahan Untuk log
def save_log(ls:list):
		with open("log.csv","w",newline="",encoding="utf-8") as csv_file:
			csv.writer(csv_file,delimiter= ",").writerows(ls)
			csv_file.close()

# #Riwayat user
def log():
	# Cara Kerja:
		#Menbaca File, kemudian menyimpan nya kedalam sebuah list, lalu ditambahkan data baru, setelah itu di tulis lagi
		
	print('Menyimpan riwayat pemain...')	
	now = time.strftime('%d-%B-%Y,%H:%M:%S')
	data = [[now,no,nilai]]	
	
	xlog = os.path.exists("log.csv")
	if xlog == False:
		#Membuat File Csv Jika Tidak Ada
		print("Log tidak di temukan\nMembuat log...")
		data.insert(0,["Tanggal","No","Nilai"])
		save_log(data)

	elif xlog == True:
		with open('log.csv','r',newline="",encoding='utf-8') as file:
			data_old = [i for i in csv.reader(file,delimiter=",")]
			data_old.append(data[0])
			save_log(data_old)
	print('Tersimpan')
	os.system('clear')
	

def jawab(v=True):
	# Fungsi ini berfungsi supaya tidak terjadi runtime eror, fungsi ini akan mengembalikan nilai yang di input pada variable input_user
	while True:
		try:
			input_user = float(input())	
			if v == True:
				ver = int(input('Yakin? [1/2] '))
				if ver == 1:
					return input_user
					break
				else:
					print('Masukkan Ulang Jawaban: ',end='')
			elif v == False:
				return input_user
				break
		except ValueError:
				print('Input Tidak Valid!\nMasukkan Ulang Jawaban:',end=" ")


	
def soal():
	global no
	global nilai
	log()
	
	operasi = ''.join(random.sample('+-×÷',1))
	operasi = '+'

	print('Operasi =',operasi)

	if operasi == '+':
		a = randnum(0,50)
		b = randnum(0,50)
		print(f'{no}. {a} + {b} = ',end='')
		if jawab() == a + b:
			print('Yeay')
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a+b}')
			nilai -= 1

	elif operasi == "-":
		a = randnum(0,50)
		b = randnum(0,a) 
		print(f"{no}. {a} - {b} = ",end="")
		if jawab() == a - b:
			print("Yaho")
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a-b}')		
			nilai -= 1

	elif operasi == '×':
		a = randnum(0,30)
		b = randnum(0,10)
		print(f'{no}. {a} × {b} = ',end='')
		if jawab() == a * b:
			print('Yeay')
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a*b}')
			nilai -= 1
	
	# Later
#######################
	elif operasi == '÷':
		dummy = randnum(0,50)
		print('Dummy =' ,dummy)
		ls = [i for i in range(50*2+1) if i % 2 == 0]
		print(len(ls))
		a = ls[dummy]
#		b = randnum(0,a)
		b = 2
		print(f'{no}. {a} ÷ {b} = ',end='')
		if jawab() == a / b:
			print('Jawaban Benar')
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a/b}')
			nilai -= 1
	no += 1
##############################
print('Succes')
nilai = 0
no = 1
if __name__ == '__main__':
	if os.path.exists('log.csv') == False:
		log()
	with open('log.csv','r',newline="",encoding='utf-8') as file:
		a = [i for i in csv.reader(file,delimiter=",")]
		nilai = a[-1][2]; nilai = int(nilai)
		no = a[-1][1]; no = int(no)
			
	print(f'Nilai = {nilai}')
	print(f'No = {no}')
	print(type(nilai),type(no))
	
	input('Klik Enter Untuk Melanjutkan')	
	while True:
		soal()

# Fitur:
#	waktu penyelesaian 
#	save and load

