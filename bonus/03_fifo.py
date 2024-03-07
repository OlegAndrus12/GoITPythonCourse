# FIFO


from collections import deque

MAX_LEN = 10

fifo = deque(maxlen=MAX_LEN)


def push(el):
    fifo.append(el)


def pop():
    return fifo.popleft()


push("Volodymyr")
push("Vitaliy")
push("Olexander")
push("Alexandr")
print(fifo)
name = pop()
print(name)
print(fifo)
