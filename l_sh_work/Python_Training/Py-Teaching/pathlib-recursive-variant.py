from pathlib import Path

p = Path('./')

for child in p.iterdir():
	print(str(child))

#paths = sorted(Path('.').glob('**/*'))
paths = Path('.').glob('**/*')

for i in paths:
	print(str(i))
