'''
Больше возможностей pathlib
'''
from pathlib import Path

current_dir = Path('.')

# for el in current_dir.iterdir():
#     print(f'{el.name}. Dir: {el.is_dir()}. File: {el.is_file()}. Exist: {el.exists()}')

file = current_dir / 'bin' / 'utils' / 'paint.drawio.svg'
# print(file.exists())

for el in current_dir.glob('**/*.jpg'):
    print(el)

tmp = Path('./empty.txt')
if tmp.exists():
    tmp.unlink()
