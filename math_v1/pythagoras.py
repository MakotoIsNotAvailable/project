import random
import time

awal = time.time()
q = True
while q:
	c = random.randint(0,100)**2
		
	#c = 25
		
	for i in range(101):
		for j in range(101):
			if i ** 2 + j ** 2 == c and i != 0 and j != 0:
				print(f'I = {i ** 2}\nJ = {j ** 2}\nC = {c}\n\n')
				
				
				q = False

print(f"Waktu penyelesaian program = { time.time()-awal}")			