import math

input = open("./input.txt")
lines = input.read().split("\n")[:-1]
masses = [int(i) for i in lines]
sum = 0
for m in masses:
  sum = sum + (math.floor(m / 3) - 2)
print("Total fuel needed: " + str(int(sum)))
