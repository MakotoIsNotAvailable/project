import pytube as pt

def inpi(text=" "):
	while True:
		try:
			return int(input(text))
		except ValueError:
			print('Input Harus Angka!')
#else: print("Error inpi")

def video(link):
	v1 = pt.YouTube(link).streams.all()
	for i in list(enumerate(v1)):
		print(i); print()
		
	inputU = inpi('Pilih Opsi: ')
	print('Downloading.......')
	v1[inputU].download()
	print('Download Complete!')

def playlist(link):
	#Not Recomend
	pl = pt.Playlist(link)
	print(f'Playlist: {pl.title}')
	for v in pl.videos:
		print('Downloading...')
		v.streams.first().download()

if __name__ == '__main__':
	video(input('Link: '))
