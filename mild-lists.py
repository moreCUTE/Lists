#Mild lists##############################################################
colors = ["Purple", "Red", "Blue", "Green", "Black"]
print(colors[0])
print(colors[2])
print(colors[-1])
print(colors)
colors.append("Yellow")
print(colors)

#-----------------------------
totalpay = 0
paychecks = [100, 200, 300, 400]

for i in range(len(paychecks)):
   totalpay +=  paychecks[i]
print (totalpay)

#-----------------------------

foods = []

print("how much food u want?")
num = int(input())

for j in range(num):
   print("what food you want")
   fod = input()
   foods.append(fod)

print(foods)
