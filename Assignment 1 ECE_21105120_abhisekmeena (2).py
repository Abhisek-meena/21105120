# qustion 1st

print('question 1')
number_1 = int(input('enter 1st number-'))
number_2 = int(input('enter 2nd number-'))
number_3 = int(input('enter 3rd number-'))
total = (number_1+number_2+number_3)
average = total/3
print(average)


# question 2nd

print('question 2')
      
tax_rate = 0.2
sd = 10000
# Standard Deduction
dd = 3000
# Dependent Deduction
gi = int(input('Enter Gross Income-'))
# Gross Income
no_of_dependent  = int(input('Enter No Of Dependent-'))
taxable_income = gi-sd-(dd*no_of_dependent)
print('Taxable Income',taxable_income)
tax = taxable_income *tax_rate
print("Tax:",tax)


# question 3rd

print("question 3")
student = ["SID","Name","Gender","department Name","CGPA"]
print("Student:",student)
student = [21105120,"Abhisek Meena","M","ECE",9]
print("student:",student)


# question 4th

print("question 4")
Marks = [63,96,78,36,52]
print("Marks Before Sorting:",Marks)
Marks.sort()
print("Marks After Sorting:",Marks)


# question 5th

print("question 5")
#list of color as given in question         
color = ['Red','Green','White','Black','Pink','Yellow']
print("Color",color)
color.pop(3)
print("(a)Color",color)         

color = ['Red','Green','White','Black','Pink','Yelow']
color[3:5] = ["Purple"]
print("(b)Color",color)         
          
        
                            

                        
          
