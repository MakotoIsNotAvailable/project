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
def randnum(a,b):
	return random.randint(a,b)

# #Riwayat user
def log():
	print('Menyimpan riwayat pemain...')
	
	def save_log(ls:list):
		with open("log.csv","w",newline="",encoding="utf-8") as csv_file:
			csv.writer(csv_file,delimiter= ",").writerows(ls)
			csv_file.close()
	
	now = time.strftime('%d-%B-%Y,%H:%M:%S')
	data = [[now,no,nilai]]	
	
	xlog = os.path.exists("log.csv")
	if xlog == False:
		print("Log tidak di temukan\nMembuat log...")
		data.insert(0,["Tanggal","No","Nilai"])
		save_log(data)

	elif xlog == True:
		with open('log.csv','r',newline="",encoding='utf-8') as file:
			data_old = [i for i in csv.reader(file,delimiter=",")]
			data_old.append(data[0])
			save_log(data_old)
	print('Succes')
	

def ver():
	while True:
		try:
			jawab = float(input())	
			ver = int(input('Yakin? [1/2] '))
			if ver == 1:
				return jawab
				break
			elif ver == 2:
				print('Masukkan Ulang Jawaban: ',end='')
		except ValueError:
				print('Input Tidak Valid!\nMasukkan Ulang Jawaban:',end=" ")


	
def soal():	
	log()
	
	global no
	global nilai
	operasi = ''.join(random.sample('+-×÷',1))
	operasi = '+'

	print('Operasi =',operasi)

	if operasi == '+':
		a = randnum(0,50)
		b = randnum(0,50)
		print(f'{no}. {a} + {b} = ',end='')
		if ver() == a + b:
			print('Yeay')
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a+b}')
			nilai -= 1

	elif operasi == "-":
		a = randnum(0,50)
		b = randnum(0,a) 
		print(f"{no}. {a} - {b} = ",end="")
		if ver() == a - b:
			print("Yaho")
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a-b}')		
			nilai -= 1

	elif operasi == '×':
		a = randnum(0,50)
		b = randnum(0,20)
		print(f'{no}. {a} × {b} = ',end='')
		if ver() == a * b:
			print('Yeay')
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a*b}')
			nilai -= 1
		
	elif operasi == '÷':
		dummy = randnum(0,50)
		print('Dummy =' ,dummy)
		ls = [i for i in range(50*2+1) if i % 2 == 0]
		print(len(ls))
		a = ls[dummy]
#		b = randnum(0,a)
		b = 2
		print(f'{no}. {a} ÷ {b} = ',end='')
		if ver() == a / b:
			print('Jawaban Benar')
			nilai += 1
		else:
			print(f'Jawaban Salah!\nJawaban Yang Benar: {a/b}')
			nilai -= 1
	no += 1

print('Succes')


nilai = 0
no = 1
if __name__ == '__main__':
	print('Program Dimulai Dalam 3 Detik...')
#	time.sleep(3)
#	os.system('clear')
	while True:
		print(f'Nilai = {nilai}')
		print(f'No = {no}')
		soal()
		input('Pause')

# Fitur:
#	waktu penyelesaian 
#	save and load

