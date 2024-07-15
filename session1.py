# Variables:
n1 = 7
n2 = 5
total = n1 + n2
#print(total)


# Dynamic Data Types:
x = 5
print(x, type(x))

x = "mostafa"
print(x, type(x))


# Casting:
x = 5
y = str(x)
print(y, type(y))


#concatenation:
name = "Mostafa"    
age = 23  
country = "Egypt"        

full_info = name + " is " + str(age) + " years old and lives in " + country + "."      
print(full_info)
print(f"{name} is {age} years old and lives in {country}.")


# Arithmetic Operators:
print(5+2) # Addition (+): It adds two numbers.    
print(5-2) # Subtraction (-): It subtracts the second number from the first one.   
print(5*2) # Multiplication (*): It multiplies two numbers.          
print(5/2) # Division (/): It divides the first number by the second number. If there is a remainder it will be discarded and only the quotient will be printed.            
print(5%2) # Modulus (%): It gives the remainder of the division between the first number and the second number.

# Piority of operators: Parentheses -> Exponents -> Multiplication / Division / Modulus ->   Addition / Subtraction