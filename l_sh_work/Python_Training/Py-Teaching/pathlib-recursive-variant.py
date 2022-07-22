import pathlib

import shutil

my_dir = './Primer'
my_dir1 = './Primer2'

p = pathlib.Path(my_dir)

for child in p.iterdir():
	print(str(child))

paths = sorted(pathlib.Path(my_dir).glob('**/*'))

dir_count = 0
file_count = 0
for item in paths:
	if pathlib.Path(item).is_dir():
		dir_count+=1
	if pathlib.Path(item).is_file():
		file_count+=1
print('\nFile count =', file_count)
print('Dir count =', dir_count)

try:
	shutil.rmtree(my_dir1)
except FileNotFoundError as e:
	#print(e.message, e.args)
	pass
