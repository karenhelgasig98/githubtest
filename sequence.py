
# Design an algorithm that generates the first n numbers in the following 
# sequence:; 1, 2, 3, 6, 11, 20, 37


n = int(input("Enter the length of the sequence: ")) # Do not change this line
first=0
second=1
third=2

for i in range(0,n):
    if i == 0:
         print(second) # prints out one for the first number
    elif i == 1:
        print(third) # prints out two for the second number
    else :
        # calculate next number, after 1 and 2
        #  we sum the previous 3 numbers to get the next number
        # for example for 3, first=0, second=1 and third=2
        next_number = first + second + third
        first = second
        second = third
        third = next_number
        print(next_number)