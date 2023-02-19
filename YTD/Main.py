import pytube as pt

def inp(text=" ",intr=True):
	while True:
		try:
			if intr == True: return int(input(text))
			else: return input(text)
		except:
			print('Input Tidak Valid!')


def video(link):
	v1 = pt.YouTube(link).streams.all()
	for i in list(enumerate(v1)):
		print(i); print()
		
	inputU = inp('Pilih Opsi: ')
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