'''
Tokens --> variables,punctuators

variables --> Named memory location,its a placeholder for data
#Rules are to be followed
'''

#multiAssignment of variables
'''
name,age,place = 'codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='---->')'''

#a,b=2,4,5 #valueeError as too many values to unpack
#Reassigning variables
'''
name = "codegnan"
a,b = 45,1.5
print(a,b)
a,b = b,a
print(a,b,sep=',')

a,b = b,c #NameError as c is not defined
print(a,b)

#Deleting the variables -->de[
#del a
del a,b
print(a,b)
'''
#punctuators --> [](Lists),()(tuples),{}(Dict,sets)
name = "codegnan";age = 7;course = 'Data_Analysis'
print(name,age,course)

#Datatypes --> Numeric (int,float,complex),boolean,None,
           #-->Sequences -->Lists,Tuples,Sets,String,
                #         Frozensets,mapping(dict)

#Numeric type -->int,float,complex
#int datatype -->quantity,age..
'''                
age = 7
print(age)
print(type(age)) #type --> returns the datatype of object

print(type(234))
'''

#quantity + 03 #it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
'''
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))
'''

#complex -->combination of real and imag

i2 = 4
data = 5 + i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))

#Boolean --> True / False
valid = True
print(type(valid))

error = False
print(type(error))

#Typecasting --> Converting one type to another type
#python by default follows implicit Type (we nned not mention the datatype)

#we will go for Exlicit converstion

#Every built-in datatype is a built-in function
#int,float,complex,bool

#Typecasting --> int -->float,complex,bool
'''
age =35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d= = bool (age) #returns True for existing data
print(d)
e = bool(0)
print(e)
'''
'''

age = 35.5
print(type(age))
d = int(age)
print(d)
print(type(d))
e = complex(age)
print(e)
print(type(e))
f = bool(age)
print(f)
'''
'''

#complex -->Typecasting --> int,float,bool
data = 2+5j
print(type(data))
#b = int(data) #TypeError
#print(data)
#print(c)
d = bool(data)
print(d)
print(type(d))
'''

e = int(float(bool(45)))
print(e)

f = 45+ 2.5 +2 +3j +False
print(f)

