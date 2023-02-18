import sqlite3

conn = sqlite3.connect('mydb.db')
cur = conn.cursor()

def make_table():
	sql = """	
		CREATE TABLE Barang(
		No CHAR(4) NOT NULL PRIMARY KEY,
		Nama VARCHAR(25),
		Harga REAL)
	"""
	cur.execute(sql)
	


def Insert():
	cur.execute('INSERT INTO Barang VALUES("Q001","Flask Disk 16G",50000)')
	cur.execute('INSERT INTO Barang VALUES("Q002","Core Two Duo E8400",2000)')




Insert()

cur.close()
conn.close()