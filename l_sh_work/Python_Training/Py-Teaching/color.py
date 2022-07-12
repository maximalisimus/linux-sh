#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
	print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
	print('Normal Text')
	print("Text: " + bcolors.HEADER + " Header " + bcolors.ENDC + " end.")
	print("Text: " + bcolors.OKBLUE + " OKBLUE " + bcolors.ENDC + " end.")
	print("Text: " + bcolors.OKCYAN + " OKCYAN " + bcolors.ENDC + " end.")
	print("Text: " + bcolors.OKGREEN + " OKGREEN " + bcolors.ENDC + " end.")
	print("Text: " + bcolors.WARNING + " WARNING " + bcolors.ENDC + " end.")
	print("Text: " + bcolors.FAIL + " FAIL " + bcolors.ENDC + " end.")
	print("Text: " + bcolors.BOLD + " BOLD " + bcolors.ENDC + " end.")
	print("Text: " + bcolors.UNDERLINE + " UNDERLINE " + bcolors.ENDC + " end.")

if __name__ == '__main__':
	main()
