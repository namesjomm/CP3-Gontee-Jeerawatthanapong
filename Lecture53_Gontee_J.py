#Input
price = float(input("Enter the price: "))

#Process
def vatCalculate(price):
    result = price + (price * 0.07)
    return result

#Output
print(vatCalculate(price))
