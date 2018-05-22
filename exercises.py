#Loops allow you to automate repetitive tasks.
#Read the directions in the exercises below and don't forget to print your results and commit and push your code after each exercise!

#Now, go ahead and get loopy!

#1 Order Up
#Create a for loop that will iterate through 8 numbers starting from 1 and print the following:
#'Number 1, your order is ready.'
#'Number 2, your order is ready.'
# ...
# ...
# ...
##'Number 8, your order is ready.'

for num in range (1, 9):
    print("Number " + str(num) + ", your order is ready.")


#2 Now Serving
#Create a while loop that will print the following message:
#'Now serving number 1.'
#'Now serving number 2.'
# ...
# ...
# ...
# 'Now serving number 5.'

for num in range (1, 6):
    print("Now serving number " + str(num) + ".")

#3 3 is a Magic Number
#Create a while loop that will generate a multiplication table for the number 3 and print out the following:
# 1 x 3 = 3
# 2 x 3 = 6
# 3 x 3 = 9
# 4 x 3 = 12
# ...
# ...
# ...
# 9 x 3 = 27

num = 0
while num < 9:
    num += 1
    print(str(num) + " x 3 = " + str(num * 3))


#4. Uber This!
# Declare a variable named cars and assign it a list of 5 of your favorite car brands. Next create a for loop that will iterate through the cars list and prints the following: 'My next car will be a red x.' Where x represents each item in the list.

cars = ["lexus", "audi", "mazda", "scion", "subaru"]

for types in range(len(cars)):
    print("My next car will be a red " + cars[types] + ".")

#5 Uber This Again
#Print each item in the above cars list using a while loop.

length = 0
while length < len(cars):
    print(cars[length])
    length += 1

#6  No More Tears
# Create a for loop that will iterate through the cyber attacks list and prints the following: 
#The attack at 0 is Wannacry.
#The attack at 1 is Petya.
#The attack at 2 is Locky.
#The attack at 3 is Krack Attack
#The attack at 4 is Sambacry.
#DO NOT use numbers in your string.

cyber_attacks = ['Wannacry', 'Petya', 'Locky', 'Krack Attack', 'Sambacry']

attacks = 0
while attacks < len(cyber_attacks):
    print("The attack at " + str(attacks) + " is " + cyber_attacks[attacks] + ".")
    attacks += 1
    

#7 Even
# Declare a variable named even_list and assign it an empty list. Next, write a for loop that will place 25 even numbers starting from 0 into the even_list list. Print the even_list variable to see your results. 

even_list = []

for num in range (0 , 25, 2):
    even_list.append(num)
    
print(even_list)

#8 Sum Up
# Create a function named add_up which takes a parameter num. In the code block inside the function, create a variable named sum and assign it a number value of 0. Next, create a for loop that will iterate through a list of numbers using the range function that will be determined by the num parameter and will sum up all the numbers in the list and store it to the sum variable. Print the sum variable to see your results.

#i.e a number list of 10 will have a sum total of 45

def add_up(num):
    sum = 0
    for i in range(num):
        sum += i
    return print(sum)

add_up(99)

#9 East Coast vs West Coast - A Hip Hop Rivalry
#The East Coast - West Coast hip hop rivalry was a feud between artist and fans of the East Coast hip hop and West Coast hip hop scenes from the mid to last 1990s. 

#Your job is to create a function that will loop through the rappers list and place all the odd indexed items in a list named weessst_side and all the even indexed items in a list named east_side. Print your results.

rappers = ['Tupac', 'Biggie', 'Ice Cube', 'Nas', 'Snoop', '50 Cent', 'Nate Dogg', 'Wu Tang Clan', 'Kendrick Lamar']

def rap_city(artists):
    weessst_side = []
    east_side = []
    for rap in artists:
        if artists.index(rap)% 2 == 0:
            weessst_side.append(rap)
        else:
            east_side.append(rap)
    return print("weessst_side: " +str(weessst_side) + "\neast_side: " + str(east_side))

rap_city(rappers)

        

#10 Breaking Up is Easy
#Create a for loop that will iterate through 10 even numbers (starting from 0) and stop printing at 10.

for num in range(0, 12, 2):
    print(num)
    if num == 10:
        break

#11 Zip Codes
#Create a for loop that will iterate through the zip codes list below and print all the zip codes except for 96822.

zip_codes = [90001,90002,90003,90004,90005,96822,90007,90008,90010,90011,90012,90013,90014,90015, 90016,90017,90018,90019]

for zip in zip_codes:
    if zip == 96822:
        skip = True
        continue
    print(zip)


#12 Fizz Buzz!
#The classic programming task is back! Use a for loop that will iterate through 100 numbers starting from 1. Your job is to program the following:

#  a) if the number is a multiple of 3, it should print 'Fizz'
#  b) if the number is a multiple of 5, it should print 'Buzz'
#  c) if the number is a multiple of 3 and 5, it should print 'Fizz Buzz'
#  d) if the number is neither a multiple of 3 and 5, it should print the number

#example output:
# 1
# 2
# Fizz
# 4
# Buzz
# ...
# ...
# ...
# 14
# Fizz Buzz

for i_hate_this_problem in range(1, 100):
    if i_hate_this_problem % 3 == 0 and i_hate_this_problem % 5 == 0:
        print("fizz buzz")
    elif i_hate_this_problem % 3 == 0:
        print("fizz")
    elif i_hate_this_problem % 5 == 0:
        print("buzz")
    else:
        print(i_hate_this_problem)

#13 Fizz Buzz Again 
#Do the same thing again using a while loop.

not_again = 0

while not_again <= 100:
    if not_again % 3 == 0 and not_again % 5 == 0:
        print("fizz buzz")
    elif not_again % 3 == 0:
        print("fizz")
    elif not_again % 5 == 0:
        print("buzz")
    else:
        print(not_again)
    not_again += 1