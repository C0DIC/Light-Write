from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import filedialog

def open_file():
	try:
		global new_item
		files = filedialog.askopenfile(mode = 'r')
		in_d = files.read()
		txt_place.delete('1.0', END)
		txt_place.insert('1.0', in_d)
	except (UnicodeDecodeError, AttributeError):
		pass


def save_file():
	try:
		files = filedialog.asksaveasfile(mode = 'w')
		in_d = txt_place.get('1.0', END)
		files.write(in_d)
	except AttributeError:
		pass


def new_file():
	global new_item
	txt_place.delete('1.0', END)

win = Tk()
win.title('Light Write')
win.config(bg = '#323233')
#win.iconbitmap(r'/home/Naza/TIMA/Python/Idea/s600.')

txt_place = Text(win, insertbackground = 'gray', bd = 1)
txt_place.pack(fill = BOTH, expand = True)
txt_place.config(bg = '#323233',fg = 'gray',selectbackground = 'gray')
txt_place.config(highlightbackground = '#323233', font = ('Sans', 11))
txt_place.insert(INSERT, '')

txt_place2 = Entry(win, width = 20, bg = '#323233' , bd = 1)
txt_place2.config(font = ('Sans', 11), highlightbackground = '#323233')
txt_place2.config(fg = 'gray')
txt_place2.pack(fill = BOTH, expand = True)

menu = Menu(win, bd = 0)
new_item = Menu(menu, tearoff=0, bd = 1)
theme_menu = Menu(menu, tearoff = 0, bd = 1)
font_menu = Menu(menu, tearoff = 0, bd = 1)

menu.config(bg = '#323233',fg = 'gray')
new_item.config(bg = '#323233',fg = 'gray')
theme_menu.config(bg = '#323233',fg = 'gray')
font_menu.config(bg = '#323233',fg = 'gray')

def black_theme():
	win.config(bg = 'black')
	new_item.config(bg = 'black',fg = 'white')
	theme_menu.config(bg = 'black',fg = 'white')

	txt_place.config(highlightbackground = 'black')
	txt_place.config(selectbackground = 'white')
	txt_place.config(bg = 'black',fg = 'white', insertbackground = 'white')

	txt_place2.config(highlightbackground = 'black')
	txt_place2.config(selectbackground = 'white')
	txt_place2.config(bg = 'black',fg = 'white', insertbackground = 'white')

	font_menu.config(bg = 'black',fg = 'white')

	menu.config(bg = 'black',fg = 'white')

def white_theme():
	win.config(bg = 'white')
	new_item.config(bg = 'white',fg = 'black')
	theme_menu.config(bg = 'white',fg = 'black')

	txt_place.config(highlightbackground = 'white')
	txt_place.config(selectbackground = 'gray')
	txt_place.config(bg = 'white',fg = 'black', insertbackground = 'black')

	font_menu.config(bg = 'white',fg = 'black')

	txt_place2.config(highlightbackground = 'white')
	txt_place2.config(selectbackground = 'gray')
	txt_place2.config(bg = 'white',fg = 'black', insertbackground = 'black')

	menu.config(bg = 'white',fg = 'black')

def dark_theme():
	win.config(bg = '#323233')
	new_item.config(bg = '#323233',fg = 'gray')
	theme_menu.config(bg = '#323233',fg = 'gray')

	txt_place.config(highlightbackground = '#323233')
	txt_place.config(selectbackground = 'gray')
	txt_place.config(bg = '#323233',fg = 'gray', insertbackground = 'gray')

	txt_place2.config(highlightbackground = '#323233')
	txt_place2.config(selectbackground = 'gray')
	txt_place2.config(bg = '#323233',fg = 'gray', insertbackground = 'gray')


	font_menu.config(bg = '#323233',fg = 'gray')
	menu.config(bg = '#323233',fg = 'gray')

def font_size():
	try:
		i = txt_place2.get()
		if i == '\n':
			pass
		elif int(i) < 18 and int(i) > 9:
			txt_place.config(font = ('Sans', i))
	except ValueError:
		pass

new_item.add_command(label = 'New', command = new_file)
new_item.add_command(label = 'Open', command = open_file)
new_item.add_command(label = 'Save', command = save_file)

theme_menu.add_command(label = 'Light', command = white_theme)
theme_menu.add_command(label = 'Black', command = black_theme)
theme_menu.add_command(label = 'Dark', command = dark_theme)

font_menu.add_command(label = 'Size', command = font_size)


menu.add_cascade(label= 'File', menu = new_item)
menu.add_cascade(label = 'Themes', menu = theme_menu)
menu.add_cascade(label = 'Commands', menu = font_menu)

win.config(menu=menu)

win.mainloop()