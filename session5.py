# x = 10 > 5
# print(x)

# # Exercise 1:
# job = "Backend"
# if job == "Frontend":
#     print("You are a Frontend Devveloper")
# elif job == "Backend":
#     print("You are a Backend Developer")
# else:
#    print("Invalid Job Title")

# # Exercise 2:
# employee = "Mostafa"
# rate = 5
# experience = 1
# salary = 8000

# if rate >= 5 and experience >= 2:
#     newSalary = salary + 2000
# elif rate >= 3 and experience >= 2:
#     newSalary = salary + 1500
# elif rate >= 3 or experience >= 5:
#     newSalary = salary + 2000
# else:
#     newSalary = salary + 1000

# print(f"You deserve a bonus, your new salary will be {newSalary}")

# # Exercise 3:
# num1 = float(input("Please Enter the first number      : "))
# op =         input("Please Enter the operator (+,-,*,/): ")
# num2 = float(input("Please Enter the second number     : "))
# result = "undefined"

# if  op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "*":
#     result = num1 * num2
# elif op == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         print("Error! Division by zero == not allowed.")
# else:
#     print("Error! Invalid operator. Please enter +, -, *, or /.")

# print(f"The Result of {num1} {op} {num2} equals {result}")

# Exercise 4: currency exchange
USD_to_EUR = 0.99
USD_to_SAR = 3.75

print("=================================")
print(" Welcome to $$ EXCHANGE STORE $$ ")
print("=================================\n")

input_currency = print(input("Exchanging from (USD/EUR/SAR)? ").upper())
input_amount = float(input("How much do you want to convert? "))
output_currency = input("Exchanging to (USD/EUR/SAR)? ").upper()
output_amount = 0

if input_currency == output_currency: 
    print("\nthe amount will be the same you idiot, {input_amount} {input_currency}.\n")
elif input_currency == "USD" and output_currency == "EUR":  output_amount = input_amount * USD_to_EUR
elif input_currency == "USD" and output_currency == "SAR":  output_amount = input_amount * USD_to_SAR
elif input_currency == "EUR" and output_currency == "USD":  output_amount = input_amount / USD_to_EUR
elif input_currency == "EUR" and output_currency == "SAR":  output_amount = input_amount / USD_to_EUR * USD_to_SAR
elif input_currency == "SAR" and output_currency == "USD":  output_amount = input_amount / USD_to_SAR
elif input_currency == "SAR" and output_currency == "EUR":  output_amount = input_amount * USD_to_SAR / USD_to_EUR
else:
    print("\n Error! Wrong Currency Input.\n")

print(f"\nYou will give {input_amount} {input_currency}, and you will take {output_amount} {output_currency}")