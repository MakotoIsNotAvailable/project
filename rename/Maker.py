

#a = int(input('Masukkan Angka:'))
import os
os.chdir('Rand')
for i in range(101):
	with open(f"data{i}.txt",'w') as f:
		pass



#import os

#listDir = os.listdir()
#folder = []
#for i in listDir:
#	if os.path.isdir(i):
#		folder.append(i)          
# Menampilkan Folder
#print("Folder Yang Terdeteksi:")
#j = 1
#for i in folder:
#	print(f"{j}.{i}"); j += 1

#while True:
#	try:
#		inputU = int(input("Pilih Folder: "))
#		extension = "mp4"
#		break
#	except ValueError:
#		print('Masukkan Angka Saja! ')
#	



#os.chdir(folder[inputU-1])
#listDir = sorted(os.listdir())
#print('\nDaftar File: ')
#for i in listDir:
#	if i.endswith(extension): print(i)

#newName = 'Youjo Senki'

# Mengubah Spasi Menjadi Dash
#newName = newName.replace(' ','-')
#for i in range(len(listDir)):
#	newName = newName + str(i)
#	os.rename(listDir[i],newName +'.'+ extension)

#print(os.listdir())