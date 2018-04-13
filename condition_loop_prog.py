num = 45
if num > 0:
    print(num, "is a positive number.")
else:
    print(num, "is a negative number.")


# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sumof = 0

# iterate over the list
for val in numbers:
    sumof = sumof + val

print("The sum is", sumof)

# while loop

addition = 0
i = 1

while i <= 20:
    addition = addition + i
    i = i+1    # update counter

# print the sum
print("The sum is", addition)
