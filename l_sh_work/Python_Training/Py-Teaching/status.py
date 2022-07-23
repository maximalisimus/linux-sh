import pathlib
from stat import S_IMODE, filemode

p = pathlib.Path( 'strukture.txt' )
print(p.stat().st_mode)
print(filemode(p.stat().st_mode))
print(oct(S_IMODE(p.stat().st_mode)))

mod = '0o755' # oct: str
a = int(mod, 8)
print(mod, a, oct(a))

pathlib.Path(p).chmod(a)

print(filemode(p.stat().st_mode))
print(oct(S_IMODE(p.stat().st_mode)))
