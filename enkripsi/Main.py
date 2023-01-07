
# #Membuat Dict Yang Isinya Alphabet
chara = {' ':32}
def sp():
	print(end='\n\n\n')
def new(a,b):
	global chara
	for i in range(a,b+1):
		chara[chr(i)] = i
new(65,90)#Upper
new(97,122)#Lower
print(chara)

sp()







kunci = {}
outText = ''
#	#Encrypt Messege
key1 = list('KoRe Wa NaNI')
text = 'HeheTeNandayoH'

print(key1)

for i in text:
	chara[i] + 2

print(outText)