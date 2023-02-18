from random import randint as randnum
from time import sleep as turu

while True:
	a = randnum(0,10)
	b = randnum(0,10)
	c = [a,b,a+b]
	
	print(c)
	
	turu(1)