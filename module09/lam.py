import re

fruits = ["apple", "mango", "banana", "cherry", "apricot", "raspberry", "avocado"]

filtered_fruits = filter(lambda fruit: re.match("^a", fruit), fruits)


fruits = ["banana", "fig", "grapefruit"]

# sort fruits based on the number of vowels
fruits.sort(key=lambda x: len(re.findall("[aeiou]", x)))
print(fruits)
