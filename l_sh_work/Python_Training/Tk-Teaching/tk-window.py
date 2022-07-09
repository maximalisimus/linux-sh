#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def main():
	win = tk.Tk()
	h = 400
	w = 300
	logo = tk.PhotoImage(file='logo.png')
	win.iconphoto(False, logo)
	win.config(bg='#FFE4C4')
	win.title('Apps')
	win.eval('tk::PlaceWindow . center')
	win.geometry(f"{h}x{w}")
	win.minsize(400, 300)
	win.maxsize(800, 600)
	win.mainloop()

if __name__ == '__main__':
	main()
