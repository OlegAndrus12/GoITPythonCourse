import sys

print(sys.argv)

name = sys.argv[1]

for arg in sys.argv:
    print(arg)

person = {"name": name, "age": sys.argv[2], "lang": sys.argv[3]}
print(person)
