from tkinter import * 
from tkinter import scrolledtext, filedialog

def save_file(event):
	try:
		files = filedialog.asksaveasfile(mode = 'w', 
		filetypes = (('Python', '*.py'), ('Text', '*.txt'),('Ruby', '*.rb'), ('Nim', '*.nim'), ('HTML', '*.html'),
		('C##', '*.csharp'), ('C++', '*.cpp'), ('Rust', '*.rust'), ('CSS', '*.css'),
		('GO', '*.go'), ('PHP', '*.php'),('Java', '*.java'), ('JavaScript', '*.js'), ('TypeScript', '*.ts'),
		('Scala', '*.sc')))
		app.title("Light Write: " + str(files.name))
		data = write.get('1.0', END)
		files.write(data)
	except AttributeError:
		pass

def open_file(event):
	try:
		files = filedialog.askopenfile(mode = 'r')
		app.title("Light Write: " + str(files.name))
		data = files.read()
		write.delete('1.0', END)
		write.insert('1.0', data)
	except (UnicodeDecodeError, AttributeError):
		comm_line.insert(2, "It's not a text file")

def new_file(event):
	app.title("Light Write - [UNSAVED]")
	write.delete('1.0', END)

def black(event):
	app.config(bg = 'black')
	write.config(bg = 'black', fg = 'white', highlightbackground = 'black', insertbackground = 'white')
	comm_line.config(bg = 'black', fg = 'white', highlightbackground = 'black', insertbackground = 'white')

def white(event):
	app.config(bg = 'white')
	write.config(bg = 'white', fg = 'black', highlightbackground = 'white', insertbackground = 'black')
	comm_line.config(bg = 'white', fg = 'black', highlightbackground = 'white', insertbackground = 'black')

def sky(event):
	app.config(bg = '#2a2d4a')
	write.config(bg = '#2a2d4a', fg = 'white', highlightbackground = '#2a2d4a', insertbackground = 'white')
	comm_line.config(bg = '#2a2d4a', fg = 'white', highlightbackground = '#2a2d4a', insertbackground = 'white')

def size(event):
	try:
		comm = comm_line.get()
		if int(comm) > 9 and int(comm) < 18:
			write.config(font = ('Sans', int(comm)))
		else:
			comm_line.insert(3, " | Only from 10 to 17")
	except ValueError:
		pass

def focusing_d(event):
	comm_line.focus()

def focusing_u(event):
	write.focus()

def esc(event):
	app.destroy()

app = Tk()
app.title('Light Write')
app.config(bg = 'white')
app.minsize(width = '660', height = '500')
app.maxsize(height = '800')

app.bind('<Control-s>', save_file)
app.bind('<Control-o>', open_file)
app.bind('<Control-n>', new_file)
app.bind('<Control-b>', black)
app.bind('<Control-k>', sky)
app.bind('<Control-w>', white)

app.bind('<Control-d>', size)
app.bind('<Control-Up>', focusing_u)
app.bind('<Control-Down>', focusing_d)
app.bind('<Escape>', esc)

write = Text(app, bg = 'white', bd = 1)
write.pack(expand = True, fill = BOTH)
write.focus()

comm_line = Entry(app, bg = 'white', bd = 1)
comm_line.pack(side = RIGHT, fill = BOTH, expand = True)

app.mainloop()