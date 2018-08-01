from tkinter import *
from ctypes import windll, wintypes
import time
import winsound
import re

root = Tk()
root.wm_attributes("-topmost", 1)
root.winfo_toplevel().title("Printer Timer")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

def test():
	try:
		m = re.search(r'\d', entry.get())
		timeleft = round(int(m.group()))
	except:
		timeleft = 9
	print("Tested")
	minutes.config(text="You have been bamboozled")
	button.config(bg="green", text='Timer Started.', command=reset())
	minutes.config(text='Time Remaining: {} Minutes'.format(timeleft))
	root.update()
	while timeleft > 0:
		root.after(60000)
		timeleft = timeleft - 1
		print(timeleft)
		minutes.config(text='Time Remaining: {} Minutes'.format(timeleft))
		root.update()
	winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
	reset()

def reset():
	button.config(bg='red', text='Start Timer.')
	minutes.config(text='Timer Not Running.')

button = Button(root, text='Start Timer.', command=test, bg="red", state="normal")
button.pack()

amount = StringVar()
amount.set('Timer: 9')

entry = Entry(root, justify='center', textvariable=amount)
entry.pack()

minutes = Label(root, text="Timer Not Running.")
minutes.pack(side=LEFT)

root.geometry('260x60+' + str(round((ws / 1.2))) + '+' + str(round((hs / 105.3))))
root.iconbitmap('icon.ico')

root.mainloop()