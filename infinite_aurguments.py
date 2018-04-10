
# Passing infinite argument to a function

def  sum_of_numbers (*number):
    for num in number:
        #numbersum = sum(num)
        print(num)
    #print("Sum of passing numbers=",numbersum)
    sum_of_numbers(2,4,3,4)