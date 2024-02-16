'''
The same as previous but read last n lines (from a tail)
'''
NUMBER_LINES = 4


try:
    lines = []
    with open("test.txt", 'r', encoding='utf-8') as file:
        for line in file:  # file.readline()
            lines.append(line)
            if len(lines) > NUMBER_LINES:
                lines.pop(0)

    print(lines)

except OSError as err:
    print(f'Error happened: {err}')
