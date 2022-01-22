# question 1st

print("question 1")

string = "python is a case sensitive language"

# a. Find the length of the input string.
length = len(string)
print("The length of string is %d"%(length))

# b. Reverse the order of the string in one line code.
reversed_string = string[::-1]
print(reversed_string)

# c. Using Slice function store "a case sensitive" in new string.
new_str = string[slice(10,35)]
print("New sliced string:- ",new_str)

# d. Replace "a case sensitive" with "object oriented".
replaced_string = string.replace("a case sensitive" , "object oriented")
print("New string:- ",replaced_string)

# e. Find index of substring "a" in the given input string.
req_index = string.index("a")
print("Index of required substring is- ",req_index)

# f. Remove the white spaces from the given input string.
without_spaces_string = string.replace(" " ,"")
print("New string:- ",without_spaces_string)

###############################################################################

# question 2nd

print("question 2")

#Initializing variables
name = input("Enter your name here:- ")
SID = int(input("Enter your SID here:- "))
Dep_name = input("Enter your Department Name here:- ")
CGPA = float(input("Enter your CGPA here:- "))

# printing statements in the given format.
print("Hey, %s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %f"%(Dep_name,CGPA))

###############################################################################

# questuon 3rd

print("question 3")

a = 56
b = 10

print(" a&b : ", a & b)
print(" a/b : ", a / b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 ; ", a >> 2, "\tb>>2 :", b >> 4)

###############################################################################

# question 4th

print("question 4")

# Taking input of 3 numbers from the user.
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

# Finding the highest number.
if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c

print(f"Highest number = {highest_number}")

#################################################################################

# question 5th

print("question 5")

# Taking input string from user.
input_string = input("Enter input string : ")

if "name" in input_string:
    print("Yes")
else:
    print("No")

###################################################################################

# question 6th

print("question 6")

# Taking input lengths from user.
a = int(input("Enter the 1st length : "))
b = int(input("Enter the 2nd length : "))
c = int(input("Enter the 3rd length : "))

# Checking that given input lenght cannot form triangle.
if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")

###################################################################################


    

             
    
      
      
