product = []

def showBill(): #Bill function
    totalPrice = 0
    print("-----------Your Orders-----------")
    for i in range(len(product)):
        print("Product :", product[i][0],"---","Price :", product[i][1])
        totalPrice = totalPrice + float(product[i][1])
    print("---------------------------------")
    print("Total :", totalPrice)
    print("---------------------------------")

#Input   
while True:
    nameProduct = input("Enter name product : ")
    if nameProduct.lower() == "exit":
        break
    else:
        priceProduct = float(input("Enter price product : "))
        product.append([nameProduct, priceProduct])
        

#Output
showBill()
