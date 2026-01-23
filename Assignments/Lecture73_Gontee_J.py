systemMenu = {"cola":20,"candy":1.5,"kfc":289,"milk":25}
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
        product.append([nameProduct, systemMenu[nameProduct]])
        
#Output
showBill()
