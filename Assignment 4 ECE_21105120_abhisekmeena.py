# Question 1

print("Question 1")

# Defining tower of Honoi function
def tower_of_hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    tower_of_hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    tower_of_hanoi(n-1, aux, to, fro)
    
# Taking number of disk input from user
num_of_disk = int(input("Enter the number of disk in tower of honoi:"))

# Calling funtion for 3 disks
# Using the function of tower of honoi
tower_of_hanoi(num_of_disk,"{fro} tower","{to} tower","aux")

###################################################################################

# Question 2

print("Question 2")

# Input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

# Using recursions
print("\nThe pascle's Ttiangle using ""recursions approach is:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    # Printing the spaces
    print('  '*(originaln-n), end='')

    # First number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        # Using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

# Iterative Approach


print("\nThe Pascle's Triangle using ""iterative approach is:\n")
# Taking number of rows as input
row = int(input("Enter number of rows:"))
# Forming fuction that will return next row of pascle triangle
def psum(list1, row):
    i1 = 0
    i2 = 1
    l = []
    for i1 in range(row - 1):
        l.append(list1[i1] + list1[i2])
        i1 = i1 + 1
        i2 = i2 + 1
    l.insert(0, 1)
    l.append(1)
    return (l)

# Forming function that will print all rows using previous function
def ptriangle(rows):
    if rows == 1:
        print("{a:^100}".format(a="1"))
    elif rows == 2:
        print("{b:^100}".format(b="1"))
        print("{b:^100}".format(b="1 1"))
    else:
        f = "{p:^100}".format(p=1)
        print(f)
        f = "{p:^100}".format(p="1  1")
        print(f)
        l1 = [1, 1]
        row = 2
        for i in range(rows - 2):
            v = psum(l1, row)
            v2 = v.copy()
            v2 = list(map(str, v2))
            n = rows
            k = "  ".join(v2)
            f = "{p:^100}".format(p=k)
            print(f)
            row = row + 1
            l1 = v
ptriangle(row)

#######################################################################################

# Question 3

print("Question 3")

# Taking input from user
a=int(input("Enter the first integer: "))
b=int(input("Enter the first integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))

#########################################################################################

# Question 4

print("Question 4")

# Forming a class named student
class student:
    # Using constructor to create class objects
    def __init__(self,name,sid):
        self.name = name
        self.sid = sid
    # Defing print function
    def pfun(self):
        print(f"Hello, My name is {self.name} and my "
              f"sid is {self.sid}")
    # Calling destructor
    def __del__(self):
        print("Destructor Called")
# Makin abhisek an object of student
abhisek = student("Abhisek",21105120)
abhisek.pfun()
del abhisek

########################################################################################

# Question 5

print("Question 5")

# Making class employees

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

# Creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# Part a, updating salary of Mehak to 70000
print("\nQuestion 5a")
employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

# Part b, deleting a record
print("\nQuestion 5b")
print("b. ", end='')
del employee3

########################################################################################

# Question 6

print("Question 6")
gap=""*10
print(f"\n{gap}GAME THAT CHECK TRUE FRIENDSHIP")

# Taking player name input
player1 = str(input("\nEnter player1 name:"))
player2 = str(input("\nEnter player2 name:"))

# Inputting a word from the first friend
word = input("Enter the first word: ")

# Inputting a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")

# Defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count


# Test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

# Shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
        

        
        





#####################################################################################
























