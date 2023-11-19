#Create 3 lists
numbers = []
strings = []
names = []
 
#Add numbers to the list "numbers"
numbers.append(1)
numbers.append(2)
numbers.append(3)

#Add words to "strings"
strings.append("hello")
strings.append("world")

#Add names to "names" list
names.append("John")
names.append("Eric")
names.append("Jessica")

#New variable (3rd name has index 2)
third_name = names[2]

print(numbers)
print(strings)
print(names)
print(f"The new variable is: {third_name}")
