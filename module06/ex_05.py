'''
pathlib example
'''

from pathlib import Path

folder = Path('./Temp')
filename = folder / 'temp.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

except OSError as err:
    print(f'Can not access file: {err}')
finally:
    print('')
    print('File operation completed')
