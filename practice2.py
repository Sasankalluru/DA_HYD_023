#list=[4,6,1,0,2,4,0,6]
#write a python program to calculate the innings of a bats man and count boundary,dot
'''
runs = list(map(int, input("Enter runs: ").split()))

score = 0
boundaries = 0
dots = 0

for i in runs:
    score = score + i

    if i == 4 or i == 6:
        boundaries = boundaries + 1

    if i == 0:
        dots = dots + 1

print("Total Score:", score)
print("Boundaries:", boundaries)
print("Dot Balls:", dots)
'''

password = "1234"
chance = 5

while chance > 0:
    user = input("Enter Password: ")

    if user = password:
        print("Phone Unlocked")
        break
    else:
        chance = chance - 1
        print("Wrong Password")
        print("Chances Left:", chance)

if chance == 0:
    print("Phone Locked")
