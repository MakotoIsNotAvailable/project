print('Memuat Program...')
import os
import random
import time

def load():
	print('Memuat Data User...')
	cek = os.path.exists('data.txt')
#	if cek is True:
#		with open('data.txt','r') as f:
	
def ver():
	while True:
		try:
			jawab = int(input())

			ver = int(input('Yakin? [1/2] '))
			if ver == 1:
				return jawab
				break
			elif ver == 2:
				print('Masukkan Ulang Jawaban: ',end='')
				continue
		except ValueError:
				print('Input Tidak Valid!\nMasukkan Ulang Jawaban:',end=" ")

def randnum(a,b):
	return random.randint(a,b)
	
def soal():
	global no
	global nilai
	operasi = ''.join(random.sample('+-×÷',1))
#	operasi = '+'

	print('Operasi =',operasi)

	if operasi == '+':
#		a = random.randint(0,100)
#		b = random.randint(0,100)
		a = randnum(0,50)
		b = randnum(0,50)
		print(f'{no}. {a} + {b} = ',end='')
		if ver() == a + b:
			print('Yeay')
			nilai += 1
		else:
			print('Jawaban Salah!\nJawaban Yang Benar: {a+b}')
			nilai -= 1

	elif operasi == "-":
		a = randnum(0,50)
		b = randnum(0,a) 
		print(f"{no}. {a} - {b} = ",end="")
		if ver() == a - b:
			print("Yaho")
			nilai += 1
		else:
			print('Jawaban Salah!\nJawaban Yang Benar: {a+b}')		
			nilai -= 1

#	elif operasi == '×':
#		print(f'{no}. {a} × {b} = ',end='')
#		if ver() == a * b:
#			print('Yeay')
#			nilai += 1
#		else:
#			print('Jawaban Salah!\nJawaban Yang Benar: {a*b}')
#			nilai -= 1
#		
#	if operasi == '÷':
#		a = randnum(0,50)
#		b = randnum(0,50)
#		print(f'{no}. {a} + {b} = ',end='')
#		if ver() == a + b:
#			print('Yeay')
#			nilai += 1
#		else:
#			print('Jawaban Salah!\nJawaban Yang Benar: {a/b}')
#			nilai -= 1


	no += 1

nilai = 0
no = 1
print('Succes')
if __name__ == '__main__':
	print('Program Dimulai Dalam 3 Detik...')
#	time.sleep(3)
	while True:
		print(f'Nilai = {nilai}')
		soal()

# Fitur:
#	waktu penyelesaian 
#	save and load