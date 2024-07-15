def welcome():
    print("Welcome to the Python Quizzer!")


def clac(n1, n2):
    print(n1 + n2)


def netPrice(price, tax):
    return price + tax


total = netPrice(1000, 80) + 50
# print(total)


def max_num(n1, n2, n3):
    if (n1 >= n2) and (n1 >= n3):
        return n1
    elif (n2 >= n1) and (n2 >= n3):
        return n2
    else:
        return n3


def getPrice(price, discount):
    return price - discount


print(getPrice(700, 200) + 50)
