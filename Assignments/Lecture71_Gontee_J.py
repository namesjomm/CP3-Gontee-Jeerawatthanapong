product = []
price = []

def showBill(): #Bill function
    print("-----------Your Orders-----------")
    for i in range(len(product)):
        print("Product :", product[i], "Price :", price[i])
    
    print("---------------------------------")
    print("Total :", sum(price))
    print("---------------------------------")

#Input   
while True:
    nameProduct = input("Enter name product : ")
    if nameProduct.lower() == "exit":
        break
    else:
        priceProduct = float(input("Enter price product : "))
        product.append(nameProduct)
        price.append(priceProduct)

#Output
showBill()
