#Belajar MVC
from flask import Flask, render_template, request



# Model
class Model:
	def __init__(self,name,nim):
		self.nama = name
		self.nim = nim

# View
class View:
	def show(self,mahasiswa):
		return render_template("index.html",mahasiswa=mahasiswa)

# Controller
class Controller:
	def __init__(self,model,view):
		self.model = model
		self.view = view
	
	def set_nama(self,nama):
		self.model.nama = nama
	
	def set_nim(self,nim):
		self.model.nim = nim
	
	def update_view(self):
		return self.view.show(self.model)


# Flask
app = Flask('Root')

@app.route('/mahasiswa', methods=['GET','POST'])


def mahasiswa():
	mahasiswa = Model('Fadil',999)
	view = View()
	controller = Controller(mahasiswa,view)
	if request.method == 'POST':
		controller.set_nama(request.form['nama'])
		controller.set_nim(request.form['nim'])
	return controller.update_view()

if __name__ == "__main__":
	app.run()