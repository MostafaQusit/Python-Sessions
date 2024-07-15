# Example 1:
order1 = "Pizza"
order1Qut = 1
order1Price = 20

order2 = "Cola"
order2Qut = 2
order2Price = 5

order3 = "Water"
order3Qut = 2
order3Price = 1.5

order1Cost = order1Qut * order1Price
order2Cost = order2Qut * order2Price
order3Cost = order3Qut * order3Price

total =  order1Cost + order2Cost + order3Cost
tax = total * .15 
totalcost = total + tax

print("Resturant Bill")
print(f"1: {order1} = {order1Qut} x {order1Price} = {order1Cost}$")
print(f"2: {order2} = {order2Qut} x {order2Price} = {order2Cost}$")
print(f"3: {order3} = {order3Qut} x {order3Price} = {order3Cost}$")
print("------------------------------")
print(f"Total = {total}$")
print(f"Tax ({.15}%) = {tax}$")
print("------------------------------")
print(f"Total Cost = {totalcost}$")
print("Thank You!")


#Example 1 v2.0:
orders = [["Pizza", 1, 20.0], 
          ["Cola",  2,  5.0], 
          ["Water", 2,  1.5]]

orders_cost = [order[1]*order[2] for order in orders]
totalCost = sum(orders_cost)
tax = totalCost * .15
totalCost_withTaxes =  totalCost + tax

print("Resturant Bill")
for i in range(0,3):
    print(f"1: {orders[i][0]} = {orders[i][1]} x {orders[i][2]} = {orders_cost[i]}$")    
print("------------------------------")
print(f"Total = {totalCost}$")
print(f"Tax ({.15}%) = {tax}$")
print("------------------------------")
print(f"Total Cost = {totalCost_withTaxes}$")
print("Thank You!")

# Example 1 v3.0:
class order:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
def calculateOrderCost (orderList):
    costList=[]
    for item in orderList:
        costList.append(item.quantity*item.price)
    return costList

pizza = order ("Pizza", 1, 20.0)
cola = order ("Cola", 2, 5.0)
water = order("Water", 1, 1.5)

totalCost = calculateOrderCost([pizza, cola, water])

print("\n\nSupermarket Checkout")
print("=====================")
print(f"Name: Price/Quantity: Total:")
for item in [pizza, cola, water]:
    print(f"{item.name}: ${item.price}/{item.quantity} = ${calculateOrderCost([item])}[0]$")

print("-----------------------")
print(f"Total = ${totalCost}")