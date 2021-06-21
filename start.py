import os
os.system('clear')

##############
#Assignment 1
##############
# name, age, music = "Adit Shah", 12, "Is going to music class"
# print(name, age, music)
# mylist = []
# mylist.append("Samkit Shah")
# mylist.append("Adit Shah")
# mylist.append("Nidhi Shah")
# mylist.append("Ravi shah")
# # print(mylist[0]) # prints 1
# # print(mylist[1]) # prints 2
# # print(mylist[2]) # prints 3

# # print(mylist[3])
# # print(mylist[4])
# # print(mylist[5])
# # prints out 1,2,3

# print("Start the loop")

# for element in mylist:
#     print(element)

# print("Done with the loop")

##############
#Assignment 2
##############
# numbers = []
# strings = []
# names = ["John", "Eric", "Jessica"]
# numbers.append(1)
# numbers.append(2)
# numbers.append(3.333333333333333333333333333333333333333)
# strings.append("hello")
# strings.append("world")
# # write your code here
# second_name = names[1]
# third_name = names[2]
# numbers_3 = numbers[2]


# # this code should write out the filled arrays and the second name in the names list (Eric).
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)
# print("the third name on the names list is %s" % third_name)
# print("The thrid number on the numbers list is %f" % numbers_3)

##############
#Assignment 3 - Print a list of even numbers from 0 to 10
##############

# evenNumbers = []

# evenNumbers.append(0)
# evenNumbers.append(2)
# evenNumbers.append(4)
# evenNumbers.append(6)
# evenNumbers.append(8)
# evenNumbers.append(10)

# for item in evenNumbers:
#     print(item)


##############
#Assignment 4 - if a number is even or odd for numbers between 0 to 10 
##############
# for item in range(11):
#     if item%2 == 0:
#         print("Even number %d" % item)
#     if item%2 == 1:
#         print("Odd number %d" % item)
#     print("Hello")


##############
#Assignment 5 

#The target of this exercise is to create two lists called x_list and y_list, 
# which contain 10 instances of the variables x and y, respectively. 
# ou are also required to create a list called big_list, 
# which contains the variables x and y, 10 times each, 
# by concatenating the two lists you have created.
##############
# x = object()
# y = object()

# TODO: change this code
# x_list = [x]*10
# y_list = [y]*10
# big_list = x_list + y_list

# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))

# # testing code
# if x_list.count(x) == 10 and y_list.count(y) == 10:
#     print("Almost there...")
# if big_list.count(x) == 10 and big_list.count(y) == 10:
#     print("Great!")

    
##############
#Assignment 6

#Create a list with names of all your family members
#print "Hello <family_member_name>" for each member of your family
##############

# names = ["Ravi", "Adit", "Nidhi", "Samkit"]
# ages = [40, 12, 40, 10]

# print("Hello %s" % names[0])
# print("Hello %s" % names[1])
# print("Hello %s" % names[2])
# print("Hello %s" % names[3])
# for item in names:
#     print("Hello %s" % item)

##############
#Assignment 7

#You will need to write a format string which prints out the data using the following syntax: 
# Hello John Doe. Your current balance is $53.44.
##############
# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s Your current balence is $%s."

# # print("%s %s %s Your current balence is $%.2f." % (format_string, data[0], data[1], data[2]))  
# print(format_string, % data)

##############
#Assignment 8

#Change the variables in the first section
# So that each if statement resolves as True.
##############

# change this code
# number = 16
# second_number = 10
# first_array = [1,3,4]
# second_array = [2,3]
# if number > 15:
#     print("1")

# if first_array == [0,3,4]:
#     print("2")

# if len(second_array) == 2:
#     print("3")

# if (len(first_array) + len(second_array)) == 5:
#     print("4")

# if first_array and first_array[0] == 1:
#     print("5")

# if not second_number == 11:
#     print("6")

#############

#Assignment 9

#Loop through and print out all even numbers from the numbers list in the same order they are received. 
# Don't print any numbers that come after 237 in the sequence.

############

# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]

# for item in numbers:
#     if item % 2 == 0 and item <= 237:
#         print(item)
#############

#Assignment 10

# Add a function named list_benefits() that returns the following list of strings: 
# "More organized code", 
# "More readable code", 
# "Easier code reuse", 
# "Allowing programmers to share and connect code together"

# Add a function named build_sentence(info) 
# which receives a single argument containing a string 
# and returns a sentence starting with the given string and ending with the string 
# " is a benefit of functions!"

# Run and see all the functions work together!

############
# Modify this function to return a list of strings as defined above
# def list_benefits():
#     return"More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     return  "% s is a benefit of functions!" % benefit

# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))

# name_the_benefits_of_functions()

        
    