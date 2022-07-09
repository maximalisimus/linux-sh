#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def main():
	win = tk.Tk()
	win.title('Apps')
	label_1 = tk.Label(win, text='''Hello!
World!''',
						bg='red',
						fg='white',
						font=('Arial', 15, 'bold'),
						padx=20,
						pady=40,
						width=20,
						height=10,
						anchor='sw',
						relief=tk.RAISED,
						bd=10,
						justify=tk.CENTER # tk.LEFT tk.RIGHT				
						)
	label_1.pack()
	win.mainloop()

if __name__ == '__main__':
	main()
