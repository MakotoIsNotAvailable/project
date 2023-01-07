
# #Membuat Dict Yang Isinya Alphabet
#chara = {' ':32}
#def sp():
#	print(end='\n\n\n')
#def new(a,b):
#	global chara
#	for i in range(a,b+1):
#		chara[chr(i)] = i
#new(65,90)#Upper
#new(97,122)#Lower
#print(chara)

#sp()







#	#Encrypt Messege
pesan = 'Hel O wh aTTshu p  Bnah'
pesanList = []
#	#Mengubah Pesan Dan Kunci  Menjadin Sekumpulan Angka/Ord Sesuai Indexnya
for i in pesan:
	pesanList.append(ord(i))

key1 = 'IzbIVeisvI'
key1List = []
for i in key1:
	key1List.append(ord(i))

#print(pesanList)
#print(key1List)

#	#Enkripsi
x1 = 0
for i in range(len(pesanList)+1):
	#print(i)
	if x1 >= len(key1List):
		x1 -= len(key1List)
	print(pesanList[i])
	#pesanList[i] ** key1List[x1]
	x1 += 1



