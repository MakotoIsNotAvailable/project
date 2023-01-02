import os
import random
import time
import csv

op = '[ © ]'
play = False




if os.path.exists('Folder') is True:
	os.chdir('Folder')

elif os.path.exists('__init__.py') is False or os.path.exists('soal.py') is False:
	print(f'{op}Berkas Tidak Ditemukan!\n{op}Tidak Bisa Menjalankan Program')

elif os.path.exists('data')