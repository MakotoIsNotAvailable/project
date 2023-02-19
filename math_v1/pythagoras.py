import random
import time
from math import sqrt


ran = 10

awal = time.time()
q = True
while q:
	c = random.randint(0,ran)**2
		
	#c = 25
		
	for i in range(ran):
		for j in range(ran):
			if i ** 2 + j ** 2 == c and i != 0 and j != 0:
				#print(f'I = {i ** 2}\nJ = {j ** 2}\nC = {c}\n\n')
				print(f'I = {i}\nJ = {j}\nC = {int(sqrt(c))}\n\n')
				
				
				q = False

print(f"Waktu penyelesaian program = { time.time()-awal}")			