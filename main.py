import random

def isUnique(list, index):
    unique = True
    for i in range(0, index):
        if list[index] == list[i]:
            unique = False
    return unique

#get 3 unique random numbers
random_numbers = [""] * 3

for i in range(0,3):
    random_numbers[i] = random.randint(1, 10)
    while not isUnique(random_numbers, i):
        random_numbers[i] = random.randint(1, 10)

print("Enter 3 unique numbers between 1 and 10")

correct_count = 0

while correct_count < 3:

    correct_count = 0

    #returns false on isnumeric()
    input_numbers = [""] * 3

    #inputs are stored as strings
    #isnumeric() to check if input string may be converted to integers or not
    #prevent user from entering 1 correct number 3 times and winning
    #while loop to prompt user to enter valid input

    for i in range(0,3):
        while input_numbers[i].isnumeric() == False:
            input_numbers[i] = input("Number {}: ".format(i+1))
        while int(input_numbers[i]) > 10 or int(input_numbers[i]) < 1:
            input_numbers[i] = input("Number {}: ".format(i+1))
            while input_numbers[i].isnumeric() == False:
                input_numbers[i] = input("Number {}: ".format(i+1))
        while not isUnique(input_numbers,i):
            input_numbers[i] = input("Number {}: ".format(i+1))
            while input_numbers[i].isnumeric() == False:
                input_numbers[i] = input("Number {}: ".format(i + 1))

    print(input_numbers)
    for i in range(0,3):
        if int(input_numbers[i]) in random_numbers:
            correct_count += 1

    print("You have gotten " + str(correct_count) + " number(s) correct")

print("Congratulations You Won")
