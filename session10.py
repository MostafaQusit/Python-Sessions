# 3 shapes using range function:
for n in range(12):
    print("number", n)

for n in range(2, 12):
    if n == 5:
        break
    print("number", n)

for n in range(2, 12, 2):
    if n == 6:
        continue
    print("number", n)

# for loops with list/dict:
animals = ["lion", "cat", "tiger", "dog"]
drinks = {
    "coffee":       2.5,
    "cappuccino":   5.0,
    "mocha":        4.2,
    "latte":        3.0,
    "espresso":     4.3,
    "water":        1.0
}

# 4 shapes to access list:
for i in range(4):
    print(animals[i])

for i in range(len(animals)):
    print(animals[i])

for element in animals:
    print("animal", element)

for index, element in enumerate(animals):
    print("index", index, "animal", element)


# 3 shapes to access dict:
for element in drinks:
    print("drink", element)

for element in drinks.keys():
    print("drink", element)

for key in drinks:
    print("drink", key, "price", drinks[key])
