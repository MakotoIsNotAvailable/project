import csv

c = 'Complete'
o = 'OnGoing'


data = [
	
	[1,'Rokka No Yuusha',c]
	[2,'Jaku Chara Tomozaki-kun',c]
	[3,'Kage No Jitsuryokusha Ni Naritakute',o]
	
]

pembatas = ','


with open('Test.csv','w',newline='',encoding='utf-8') as file:
	w = csv.writer(file,delimiter=pembatas)
	
	w.writerows(data)
	
	file.close()
