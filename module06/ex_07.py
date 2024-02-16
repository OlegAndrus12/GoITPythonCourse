
from pathlib import Path

current_dir = Path('.')

for el in current_dir.iterdir():
    print(f'{el.name}. Dir: {el.is_dir()}. File: {el.is_file()}. Exist: {el.exists()}')

# Check for non-existing file
file = current_dir / 'bin' / 'utils' / 'paint.drawio.svg'
# print(file.exists())

# If recursive is true, the pattern “ ** ” will match any files and zero or more directories, 
# subdirectories and symbolic links to directories. If the pattern is followed by an os.sep or os.altsep then files will not match.
# If include_hidden is true, “ ** ” pattern will match hidden directories

#  SEarch by pattern
for el in current_dir.glob('**/*.jpg'):
    print(el)

# file removal
tmp = Path('empty.txt')
if tmp.exists():
    tmp.unlink()
