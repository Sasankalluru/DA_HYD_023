''''
contral Statements --> control of Flow of execution of the program
                        -->conditional Statements --> if,elif,else...
                -->Repetition Statements(Loops) --> for,while (for with else)
                                                        (while with else)
                -->Jumping statements -->break,continue,pass
'''
#Loops --> Loops are helpful for repetition (Automative tasks)
#for keyword will be helpful to iterate over a sequence / range
#Syntax for (for keyword):
'''

for <temp_var> in sequence/range:
    statement(s)....
    ........
'''
#range(start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
#In above case we got 10 iterations
'''
for i in range(1,10):
    print(f'value of i is -->{i}')
'''
'''
for i in range(1,10):
    if i > 5:'''
'''
       #print(f'value of i is -->{i}')
    #Now i want to get only even numbers with above condition
if i > 5 and i%2 ==0:
        print(f'Final value of i is --> {i}')
        '''
#range(start,stop,step) -->there step --> interval..
'''
for i in range(1,10,2):
    print(i)
    print("Done")
'''
'''
for i in range(10,0,-1):
    print(i)
    print("Done")
'''
'''
for i in range(10,1,-2):
    print(i)
    print("Done")
'''
    
#[] --> we generally Lists
'''names = ['saketh','sairam','akash']
print(len(names)) #len(obj)-->>>>return the number of items in a container
for name in names:
    print(name)
    print(f'student Name is {name}')
    '''

#Calculate the sum of first 10 numbers
#first understand your input --> range(11) -->10 numbers
#second understand your output --> sum (number)
#third we need to map the logic
'''
result = 0 #target variable
for i in range(11):
    #print(i)
    #print(f'result is {i=i}')
    result = result + i #result += i4
    print(f'Now the result is {result}')
print(f'sum of 10 even numbers is {result}')
'''

#understand the loops usage with Fitness streak wxample
#work_out -->1,work_out_missed --> 0

work_log = [0,1,1,1,0,1,0]
#result variables -->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0 #streak breaks
print(f'longest streak is {longest_streak}')
