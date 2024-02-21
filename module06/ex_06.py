from pathlib import Path

current_path = Path(".")
# print(current_path)
# print(current_path.cwd())

# path
file = current_path / "bin" / "utils" / "paint.drawio.svg"
print(file)
# print(current_path.joinpath('bin', 'utils', 'paint.drawio.svg'))

print(file.parts)

print(file.name)
print(file.name.split(".")[0])

print(file.parent)

# file extension
print(file.suffix)
print(file.suffixes)
