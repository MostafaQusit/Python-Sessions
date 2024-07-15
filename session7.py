instructors = {
    "Alaa": "Alex",     # property -> key: value
    "Nour": "Cairo",
    "Esraa": "Giza",
    "Ahmed": "Asyut"
}
# 11 functions for list:

# print(instructors["Nour"])

instructors["Nour"] = "Cairo-Egypt"     # Change Nour location to Cairo-Egypt.
# print(instructors["Nour"])

# instructors.update({"Nour": "Zaid"})
# print(instructors["Nour"])

instructors["Omar"] = "Alex"    # Adding a new key,value pair to the dictionary
instructors.pop("Alaa")     # Removing Alaa from the dictionary
instructors.clear()         # Clearing all items in the dictionary

unit5 = {
    "title": "Python Language",
    "hours": 30,
    "pages": 40,
    "lessons": ["intro",
                "variables",
                "lists",
                "if condition",
                "loops",
                "functions"]
}
# print(unit5)
# print(unit5["title"])
# print(unit5["lessons"][1])

drinks = {
    "coffee":       2.5,
    "cappuccino":   5.0,
    "mocha":        4.2,
    "latte":        3.0,
    "espresso":     4.3,
    "water":        1.0
}
print("***************** 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝔻𝕣𝕚𝕟𝕜𝕤 𝕄𝕒𝕔𝕙𝕚𝕟𝕖 ********************")
drinks_names = list(drinks.keys())
drink = input(f"What do you want to drink {drinks_names} ? ")
# price = drinks.get(drink, "This drink is not available.")

if drink not in drinks:
    print(f"Sorry, {drink} is not available.")
else:
    price = drinks[drink]
    money = float(input(f"Please enter how much money you have (${price}) : $"))
    if money == price:
        print(f"Congratulations! You paid exactly ${price}. Enjoy your {drink}")
    elif money > price:
        change = money - price
        print(f"You bought a {drink}. Here's your change: ${change}")
    else:
        print("Not enough money! Please insert more money.")
