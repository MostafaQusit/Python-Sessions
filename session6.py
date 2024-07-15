students = ["mostafa", "ahmed", "mahmoud", "mahmoud"]
print(students[2])      # Accessing the third element in the list (mahmoud)
print(students[-1])     # Accessing the last element in the list (qusit)

# 11 functions for list:
print(students[3:5])
print(len(students))
print(students.index("ahmed"))      # Returns the index of 'ahmed' which is 1
print(students.count("mahmoud"))    # Count how many times mahmoud appears in the list
students[3] = "mohamed"             # Replacing the first two elements with new values
students.append("qusit")            # Adding a new item to the end of the list
students.remove("ahmed")            # Removing an item by its value
students.insert(1, "ahmed")         # Inserting a value at a specific index
popped = students.pop()             # Removes and returns the last item of the list
popped2 = students.pop(0)           # Removes and returns the first item of the list

c3 = ["abdullah", "ahmed"]
c4 = ["mahmoud", "mohamed"]

# c3.extend(c4)
c3 = c3 + c4
print(c3)

arr1 = c3   # Making arr1 point to the same memory location as c3
arr2 = c3.copy()    # Creating a copy of c3 and assigning it to arr2

c3.append("qusit")
print(arr1)
print(arr2)

if "qusit" in c3:
    print("Yes, 'qusit' exists in the list.")

salaries = [1000, 500, 2500, 4000, 8000]
print(sum(salaries))
print(min(salaries))
print(max(salaries))

numbers = (5, 6.5, "s")
# 2 functions for tuples: index, count