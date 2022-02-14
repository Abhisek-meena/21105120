# Question 1

print("Question 1")
# Taking input from user
string_name = str(input("Enter the string - "))
# Converting the string into lower case
list_1 = string_name.lower()
# Splitting the string into words
new_list = list_1.split()
# Declaring two empty lists
letter_list = []
word_list = []
# Conditioning to distinguish if the entered string is a single word or a sentence
if len(new_list) == 1:
    # If the string is a word
    for i in list_1:
        # Adding each letter in the letter_list
        letter_list.append(i) 
# Introducing an empty dictionary
di1 = {}
# Here letters take place of key and no.of there occurence take place of corresponding values in di1
for j in letter_list:
    if j in di1:
        di1[j] = di1[j]+1
    else:
        di1[j] = 1
    print(di1)

else:
    # IF the string is note a word
    for w in new_list:
        # Adding each word in the letter_list
        word_list.append(w)
# Introducing an empty dictionary
di4 = {}
# Here words take place of key and no. of there occurences take place of corresponding values in di4
for s in word_list:
    if s in di4:
        di4[s] = di4[s]+1
    else:
        di4[s] = 1

print(di4)
#######################################################################################################

# Question 2


print("Question 2")
# Taking input from user
day = int(input('Please enter Day- '))
month = int(input('Please enter Month- '))
year = int(input('Please enter Year- '))


# Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition = False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition = False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition = False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True
if month>12:
    condition=False


# After checking the condition, following if-else statement is executed
if condition:
    # Checking and changing for new year
    if day==31 and month==12:
        n_year=year+1
    else:
        n_year=year
    if month==12 and day==31:
        n_month=1
    else:
        n_month=month

# Changing dates
    # Checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                n_month=month+1
            else:
                n_month=1
        else:
            next_day=day+1
    # Checking for the month of february
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                n_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                n_month=3
            else:
                next_day=day+1

    # Covering all the remaining cases
    else:
        if day==30:
            next_day=1
            n_month=month+1
        else:
            next_day=day+1
    # Printing the calculations
    print(f"Next Date is: {next_day}/{n_month}/{n_year}")

else:
    # Gives a warning and ends the program
    print("That's not a valid date")
    
 
                    


###################################################################################################

# Question 3

print("Question 3")
# Taking input list
list1 = list(map(int,input("Enter the numbers separated by space:").split()))
# Empty list
list2 = []
# Forming square and storing in tuple
for e in list1:
    t = (e,e*e)
    list2.append(t)
# Printing the final result
print("\nList containing (n,n^2) is shown below:")
print(list2)

###################################################################################################

# Question 4

print("Question 4")
# Taking grade point input
grade_point = int(input("Enter grade points:"))
# Forming a dictionary of statements
dic = {10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
# Applying Conditions for correct grade range
if 4<=grade_point<=10:
    # Taking required statement from dictionary
    statement=dic.get(grade_point)
    # printing final result
    print(statement)
else:
    # printing error message when grade is out of range
    print("\nError\nPlease enter grade in range [4,10]")




####################################################################################################

# Question 5

print("Question 5")

string='ABCDEFGHIJK'
j=0
for row in range(1,7):
    for column in range(0,row-1):
        print(' ',end='')


    x=string[0:11-j]
    print(x)
    j+=2
    


###################################################################################################

# Question 6

print("Question 6")
condition = True

# Defining dictionary to store the values
Dictionary = {}
prompt = "y"
while condition:
    if prompt.lower() == "y":
        SID = int(input("Enter the SID of Student- "))
        name = input("Enter the name of the Student- ")
        Dictionary[SID] = name
        prompt = input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict = sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict = sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part D")
SID_tbf = int(input("Enter the student's SID whose detail you need- "))
if SID_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")

#######################################################################################################

# Question 7

print("Question 7")
# Defining a function for fibonacci numbers
def f(n):  
    if n==2 or n==1:
        return 1
    return f(n-1)+f(n-2)
# Taking the input
n=int(input("Enter the number - "))
print("The required series is - ")
# Printing the series
sum=0
for i in range(1,n+1):
    print(f(i),end=" ")
    sum=sum+f(i)
print("\nTotal sum of the series till the entered term = ",sum)
print("The average is = ",sum/n)


#######################################################################################################

# Question 8

print("Question 8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# Finding symmetric difference of both the sets
print("Part a")
set_notboth = Set1^Set2
print(f"set with elements not common in both is {set_notboth}")

# Finding symmetric difference of all sets
print("Part b")
set_onlyinone = Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")

# Finding elements that is common in any two sets
print("Part C")
set_onlyintwo = (Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")

# Finding elements common in set1 and range 1 to 10
print("Part d")
new_set1 = set()
for n in range(1,11):
    new_set1.add(n)
not_common_1 = new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

# Finding elements common in sets 1,2,3 and range 1 to 10
print("Part e")
new_set2 = set()
for n in range(1,11):
    new_set2.add(n)
not_common_2 = new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")









   




 
        






           


    

