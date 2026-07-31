'''
Identity Operators -->checks the identity of an object --> id()
#is,is not
'''
'''
a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)
'''
'''
a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have Lists (mulable Collection) both c and a lists will have different
#ids whereas values are same
print(c is a) #output False
print(c == a) #output True
print(a is not c)
'''

#Bitwise Operators --> we perform bitwise operations over operands
#& (and) , | (or),^(XOR),shifting operators (<<,>>)
#Number will be converted to binary format
'''
print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise OR

print(5^3) #Bitwise XDR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3) #returns 3 in this case 
'''
'''
#Leftshift Operator <<,Right shift Operator >>
print(5 < 1) #False comparision
print(5 << 1) #Left shift operation by 1 position
print( >> 1) #Right shift operation
'''

print(15 << 2) #convert 15 to binary and perform 2 times left shifting

print (15 >> 2) #same 2 times right shifting

#Input Formatting --> input(),int(input()),float(input())
#you now -->single input
#2 or 3 inputs -->map()
#group of integers --> list(map(int,input().split(','))
'''
names = input("Enter the names:").split(',')
print(names)
'''

#Tokens -->Numeric Datatypes --> Operators -->Flow of the program
#control Block statement --> they control the flow of the program
#when to execute,how to execute
#conditional statement --> if,else,elif (rely on condition to be executed)
#Repetition statement (loops) --> for,while

#conditional statement -->if usage
'''
syntax :

if <condition>:
    statement(s)...
    ......

'''
'''
#age = 25
age = int(input("Enter the age:"))
if age >=18 and age in [19,21,20]:
    print('your age is:',age)
print(age)

#else keyword --> if-else

else:
    statement(s)..

if-else usage as below:

if <condition>:
    statement(s)...
    ....
'''

#vote Elibility ->To check his/her voter eligibility and give access...
'''
age = int(input("Enter the age:"))
if age>=18:
    print("you have voter eligibility and age is",age)
    print("Access Granted")
else:
    age = 18-age
    #print("you dont have eligibility as your age is",age,"years")
    print("you need to wait for more",age,"years")

else:
    print("you have entered -ve values/zero enter only +ve")

'''
task : student marks and grade analayzer
 90 - 100 --> 'A'
 80 - 89 --> 'B'
 70 - 79 --> 'c'
 60 - 69 --> 'd'
 >60 --> Fail
 #also -ve cases should not be allowed and marks shouldnt be greater 100
