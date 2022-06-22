#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(y,t):
	k = 0.5
	dydt = -k * y
	return dydt

def main():
	y0 = 5
	t = np.linspace(0,20,30)
	y = odeint(f,y0,t)
	plt.plot(t,y)
	plt.grid()
	plt.show()

if __name__ == '__main__':
	main()
