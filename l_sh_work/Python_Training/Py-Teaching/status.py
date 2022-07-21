import pathlib
from stat import S_IMODE, filemode

p = pathlib.Path( 'color.py' )
mydir = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("parent"))

print(filemode(p.stat().st_mode))
print(oct(S_IMODE(p.stat().st_mode)), '\n')

print(filemode(pathlib.Path(mydir).stat().st_mode))
print(oct(S_IMODE(pathlib.Path(mydir).stat().st_mode)), '\n')

pathlib.Path(mydir).mkdir(parents=True, exist_ok=True)
pathlib.Path(mydir).chmod(0o700)

print(filemode(pathlib.Path(mydir).stat().st_mode))
print(oct(S_IMODE(pathlib.Path(mydir).stat().st_mode)))
