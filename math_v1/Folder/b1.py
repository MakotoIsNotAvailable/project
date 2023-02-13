import random

with open('data.txt','r') as file:
	nilai = int(file.read())

op = '[ © ]'
sp = '[ • ]'
usr = '[ ~ ]'

def jawa():
	global jawab
	while True:
		try:
			jawab = int(input(usr))
			var = input(f'{op}Yakin Dengan Jawaban Anda? [y or 1 / n or 2]: ')
			if var == 'y' or var == '1':
				break
			elif var == 'n' or var ==  '2':
				print(f'{op}Masukkan Ulang Jawaban!')
			else:
				print(f'{op}    (•ˋ _ ˊ•)')
				continue
		except ValueError:
			print(f'{op}Masukkan Jawaban Dengan Benar!')

def save():
	with open('data.txt','w') as f:
		f.write(str(nilai))


def a1():
	global nilai
	while True:
		if nilai >= 10:
			break
		try:
			q = ''.join(random.sample('+-',1))#÷×
			a = random.randint(0,99)
			b = random.randint(0,99)
			c = random.randint(0,50)
			d = random.randint(0,20)
			e = random.randint(0,50)
			f  = random.randint(0,e)
			g = random.randint(0,99)
			h = random.randint(0,20)
		except:
			continue
		
		if q == '+':
			print(f'{op}{a} + {b} = ')
			jawa()
			if jawab == a + b:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()
			
		if q == '-':
			print(f'{op}{e} - {f} = ')
			jawa()
			if jawab == e - f:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()
			
		if q == '×':
			print(f'{op}{g} × {h} = ')
			jawa()
			if jawab == a * b:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()
			
		if q == '÷':
			print(f'{op}{c} ÷ {d} = ')
			print(f'{op}Bulatkan Jika Jawaban Memiliki ( , )')#######
			jawa()
			if jawab == c // d:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()




def a2():
	global nilai
	while True:
		if nilai > 20:
			break
		try:
			q = ''.join(random.sample('+-',1))#×÷
			a = random.randint(0,999)
			b = random.randint(0,999)
			c = random.randint(0,a)
			
		except:
			continue
		
		if q == '+':
			print(f'{op}{a} + {b} = ')
			jawa()
			if jawab == a + b:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()

		if q == '-':
			print(f'{op}{a} - {c} = ')
			jawa()
			if jawab == a - c:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()
		if q == '×':
			print(f'{op}{a} × {b} = ')
			jawa()
			if jawab == a * b:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()

		if q == '÷':
			print(f'{op}{a} ÷ {b} = ')
			print(f'{op}Bulatkan Jika Jawaban Memiliki ( , )')
			jawa()
			if jawab == a // b:
				print(f'{op}Jawaban Benar\n{sp}')
				nilai += 1
				save()
			else:
				print(f'{op}Jawaban Salah!\n{sp}')
				nilai -= 1
				save()







a2()