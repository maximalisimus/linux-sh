import pathlib

import shutil

my_dir = './Primer'
my_dir1 = './Primer2'

p = pathlib.Path(my_dir)

for child in p.iterdir():
	print(str(child))

paths = sorted(pathlib.Path(my_dir).glob('**/*'))

for i in paths:
	print(str(i))

try:
	shutil.rmtree(my_dir1)
except FileNotFoundError as e:
	#print(e.message, e.args)
	pass

