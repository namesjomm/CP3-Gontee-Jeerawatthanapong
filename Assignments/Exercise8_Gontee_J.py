#Input username and password
username = input("Enter username: ")
password = input("Enter password: ")

#Check username and password
if username == "admin" and password == "1234":
    print("-------------------------")
    print("--Welcome to the Shop--")
    print("-------------------------")
    print("Product List")
    print("-------------------------")
    print("Product 1 : 100THB")
    print("Product 2 : 200THB")
    print("Product 3 : 300THB")
    print("-------------------------")
    
    #Select product and quantity
    selectProduct = int(input(("Enter product number: ")))
    quantity = int(input("Enter quantity: "))

    #Check product number and calculate total price
    if selectProduct == 1:
        print("-------------------------")
        print("Total price: ", quantity * 100)
        print("-------------------------")
    elif selectProduct == 2:
        print("-------------------------")
        print("Total price: ", quantity * 200)
        print("-------------------------")
    elif selectProduct == 3:
        print("-------------------------")
        print("Total price: ", quantity * 300)
        print("-------------------------")
    else:
        print("Invalid product number")
else:
    print("Invalid username or password")