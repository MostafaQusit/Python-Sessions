i = 1
while i <= 10:
    print(i)
    i += 1

x = 7
while x != 0:
    print("Number is:", x)
    x -= 1
else:
    print("stop x =", x)

i = 0
while i <= 10:
    i += 1
    if i == 5:
        #break   # skip the rest of this loop's code for this iteration.
        continue # Skip the rest of this loop’s code for this iteration, but do
    print(i)
print("Loop stopped at", i)
