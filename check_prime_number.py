#number = input("Enter the number:")
number = 3
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("It is not an Prime Number")
            print(i, "times", number // i, "is", number)
            break
        else:
            print("Its a Prime Number")
else:
    print("It is not an Prime Number")