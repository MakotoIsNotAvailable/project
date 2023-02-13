import csv

with open('data.csv','r') as csv_file:
	end = csv.reader(csv_file)
	
	print(end)
	
	