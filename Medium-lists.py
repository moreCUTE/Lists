#Medium llists###############################################

crunch = []

for e in range(12):
    crunch.append(random.randrange(1,11))
    crunch.sort()
print(crunch)
print(crunch[0])
print(crunch[-1])

for i in range(1):
    if crunch[i] +1 == crunch[i+1] and crunch[i+1] +1 == crunch[i+2] and crunch[i+2] +1 == crunch[i+3] and crunch[i+3] +1 == crunch[i+4] and crunch[i+4] +1 == crunch[i+5] and crunch[i+5] +1 == crunch[i+6] and crunch[i+6] +1 == crunch[i+7] and crunch[i+7] +1 == crunch[i+8] and crunch[i+8] +1 == crunch[i+9] and crunch[i+9] +1 == crunch[i+10] and crunch[i+10] +1 == crunch[i+11]:
        print("yes")
    else:
        print("no")

crunch.sort(reverse = True)
print(crunch)

