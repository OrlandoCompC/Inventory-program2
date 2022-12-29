'''
Assignment No.: 4
Course: PROG12974
Name: Orlando Companioni
Your Sheridan Student Number:991437087
Submission date: 2022/12/13
Instructor's name: Syed Tanbeer

This program is an Inventory Management System with fruits, vegetables and dairy products
This time in multiple text files some with the whole inventory while others have the most expensive items by category
or the total price of each of the items

Please note that if the file pointer is changed from where it is now in the file then it wont be able to add an item
Also note that if you keep pressing option 9 which sends to another file, it will keep repeating the information on the file
'''
import sys

def main():#This function will be the controller of the program
    process()

def menu(): #This function will display the menu options
    print()
    print("-------Inventory Database Operations--------")
    print(f"1. Show all items")
    print(f"2. Look up at the inventory")
    print(f"3. Add an item to the inventory")
    print(f"4. Change an item")
    print(f"5. Delete an item")
    print(f"6. Find items given category")
    print(f"7. Item count, average price by category")
    print(f"8. Most expensive item by category")
    print(f"9. Total price by item")
    print(f"10. Quit the program")
    print()

def menu_selection(): #This function will ask the user to select an option from the menu
    menu()
    #User input validation
    while True:
        try:
            option=int(input("Enter your option: "))
            if option not in range(1,11):
                print("ERROR: Enter a valid option") #if its a number but not in the range of 1 to 10
                continue
            break
        except ValueError:
            print("ERROR: Enter a numeric value") #if its not a number the program will ask the user to enter a number
            continue
    return option

def process(): #This function will process the user's choice
    option=menu_selection() #The menu_selection function will return the user's choice as well as the menu
    while True:
        options={1:inventory_chart,2:item_LookUp,3:add_item,4:change_item,5:delete_item,6:find_items,7:item_count,8:most_expensive,9:total_price,10:quit}
        options[option]() #This will call the function that corresponds to the option chosen by the user
        option=menu_selection()

def quit(): #This function will quit the program
    print("Thank you for using the Inventory Management System")
    sys.exit()

def inventory_chart(): #This function will display the inventory chart
    #Print table from the inventory myPersistentInventory.txt
    print()
    print(f"{'Product Id':<18}{'Product Name':18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
    #reads line from the inventory and outputs it
    with open("inventory_Orlando.txt", "r") as inventory:
        record = inventory.readline().rstrip()
        while record != "":
            fields = record.split(" ")
            print(f"{fields[0]:<18}{fields[1]:<18}{fields[2]:<18}{fields[3]:<18}{fields[4]:<18}")
            record = inventory.readline().rstrip()
      

def item_LookUp(): #This function will look up an item in the inventory
    itemId=input("Enter the product Id: ").capitalize()
    with open("inventory_Orlando.txt", "r") as inventory:
        record = inventory.readline().rstrip() #reads line from the inventory and strips the new line character
        while record != "": #while the record is not empty
            fields = record.split(" ") #splits the record into a list
            if itemId in fields:
                print(f"{'Product Id':<18}{'Product Name':18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
                print(f"{fields[0]:<18}{fields[1]:<18}{fields[2]:<18}{fields[3]:<18}{fields[4]:<18}")
                break
            record = inventory.readline().rstrip() #reads the next line and strips the new line character
        else:
            print()
            print("The product Id does not exist")

def idValidation(itemId): #This function will validate the item Id entered by the user
    with open("inventory_Orlando.txt", "r") as inventory:
        record = inventory.readline().rstrip()
        while record != "":
            fields = record.split(" ")
            if itemId in fields:
                return True
            record = inventory.readline().rstrip()
        
def typeValidation(type): #This function will validate the category entered by the user
    if type in ["Fruit","Vegetable","Dairy"]:
        return True #if the type is valid it will return true
    else: 
        return False

def price_quantityValidation(): #This function will validate the price and quantity until the user enters a valid input
    while True: #User input validation
        try:
            price=float(input("Enter the product price: "))
            break
        except ValueError:
            print("ERROR: Enter a numeric value")
            continue
    while True:
        try:
            quanity=int(input("Enter the product quantity: "))
            break
        except ValueError:
            print("ERROR: Enter a numeric value")
            continue
    return price,quanity

def add_item(): #This function will add an item to the inventory
    with open("inventory_Orlando.txt", "a") as inventory:
        itemId=input("Enter the product Id: ").capitalize()
        if idValidation(itemId): #if the item Id is already in the inventory the program will ask the user to enter a new Id
            print("The product Id already exists")
        else:
            itemName=input("Enter the product name: ").capitalize()
            while True:
                itemType=input("Enter the product type: ").capitalize()
                if typeValidation(itemType): #if the category is valid the program will break out of the loop
                    break
                else:
                    print("ERROR: Enter a valid category")
                    print("Valid categories are: Fruit, Vegetable, Dairy")
                    continue
            itemPrice,itemQuantity=price_quantityValidation()#This function will return the price and quantity validated
            #write to a new line in the inventory
            inventory.write(f"{itemId} {itemName} {itemType} {itemPrice} {itemQuantity}\n")
            print(f"{'Product Id':<18}{'Product Name':18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
            print(f"{itemId:<18}{itemName:<18}{itemType:<18}{itemPrice:<18}{itemQuantity:<18}")
            print("The item has been added to the inventory")

def change_item(): #This function will change an item in the inventory
    itemId=input("Enter the product Id: ").capitalize()
    if idValidation(itemId):
        with open("inventory_Orlando.txt", "r") as inventory:
            record = inventory.readlines() #reads all the lines in the inventory and puts them in a list
            for lines in range(len(record)): #loops through the list
                fields = record[lines].split(" ") #splits the list into a list of lists
                if itemId in fields:
                    itemName=input("Enter the product name: ").capitalize()
                    while True:
                        itemType=input("Enter the product type: ").capitalize()
                        if typeValidation(itemType): #if the type is valid it will break the loop
                            itemPrice,itemQuantity=price_quantityValidation()#This function will return the price and quantity validated
                            record[lines]=f"{itemId} {itemName} {itemType} {itemPrice} {itemQuantity}\n"
                            print(f"\n{'Product Id':<18}{'Product Name':18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
                            print(f"{itemId:<18}{itemName:<18}{itemType:<18}{itemPrice:<18}{itemQuantity:<18}")
                            print("The item has been changed")
                            break
                        else:
                            print("The Invalid item category")
                            continue          
        with open("inventory_Orlando.txt", "w") as inventory:
            inventory.writelines(record) #Writes the full changed line to the file
    else:
        print("The product Id incorrect or it doesn't exist")

def delete_item(): #This function will delete an item from the inventory
    itemId=input("Enter the product Id: ").capitalize()
    if idValidation(itemId):
        with open("inventory_Orlando.txt", "r") as inventory:
            record = inventory.readlines()
            for lines in range(len(record)):
                fields = record[lines].split(" ")
                if itemId in fields:
                    del record[lines] #deletes the line from the list
                    print("The item has been deleted")
                    break
        with open("inventory_Orlando.txt", "w") as inventory:
            inventory.writelines(record)
    else:
        print("Item not found")
    

def find_items(): #This function will find an item in the inventory depending on the type
    itemType=input("Enter the product type: ").capitalize()
    if typeValidation(itemType):
        with open("inventory_Orlando.txt", "r") as inventory:
            record = inventory.readline().rstrip()
            print(f"{'Product Id':<18}{'Product Name':18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
            while record != "":
                fields = record.split(" ")
                if itemType in fields: #if the type is in the list it will print the item
                    print()
                    print(f"{fields[0]:<18}{fields[1]:<18}{fields[2]:<18}{fields[3]:<18}{fields[4]:<18}")
                record = inventory.readline().rstrip()
    else:
        print("Invalid item category")

def item_count(): #This function will count the number of items in the inventory
    #variables to count the number of items and the average price
    fruit_count=0
    vegetable_count=0
    dairy_count=0
    fruit_price=0
    vegetable_price=0
    dairy_price=0
    with open("inventory_Orlando.txt", "r") as inventory:
        record = inventory.readline().rstrip()
        while record != "":
            fields = record.split(" ")
            if "Fruit" in fields: 
                #if the type is fruit it will add 1 to the fruit count and add the price to the fruit price
                fruit_count+=1
                fruit_price+=float(fields[3])
            elif "Vegetable" in fields:
                #if the type is vegetable it will add 1 to the vegetable count and add the price to the vegetable price
                vegetable_count+=1
                vegetable_price+=float(fields[3])
            elif "Dairy" in fields:
                #if the type is dairy it will add 1 to the dairy count and add the price to the dairy price
                dairy_count+=1
                dairy_price+=float(fields[3])
            record = inventory.readline().rstrip()
    print(f"Total number of fruits: {fruit_count}")
    print(f"Average price of fruits: {fruit_price/fruit_count}\n")
    print(f"Total number of vegetables: {vegetable_count}")
    print(f"Average price of vegetables: {vegetable_price/vegetable_count}\n")
    print(f"Total number of dairy products: {dairy_count}")
    print(f"Average price of dairy products: {dairy_price/dairy_count}")

def most_expensive():
    #This function will find the most expensive item in each category then it will write it to a different file
    max_fruit=0 
    max_dairy=0
    max_vegetable=0
    expensive_fruit=""
    expensive_fruitName=""
    expensive_dairy=""
    expensive_dairyName=""
    expensive_vegetable=""
    expensive_vegetableName=""
    with open("inventory_Orlando.txt", "r") as inventory:
        record = inventory.readline().rstrip()
        while record != "":
            fields = record.split(" ")
            #If the type is valid and the price is greater than the max at that type,it will replace the max price
            if "Fruit" in fields and float(fields[3])>max_fruit:
                max_fruit=float(fields[3])
                expensive_fruit=fields[1]+" "+fields[2]+" "+fields[3]
                expensive_fruitName=fields[1]
            elif "Vegetable" in fields and float(fields[3])>max_vegetable:
                max_vegetable=float(fields[3])
                expensive_vegetable=fields[1]+" "+fields[2]+" "+fields[3]
                expensive_vegetableName=fields[1]
            elif "Dairy" in fields and float(fields[3])>max_dairy:
                max_dairy=float(fields[3])
                expensive_dairy=fields[1]+" "+fields[2]+" "+fields[3]
                expensive_dairyName=fields[1]
            record = inventory.readline().rstrip()
    with open("expitem_Orlando.txt", "w") as inventory:
        #It will write the most expensive item in each category to a different file
        inventory.write(expensive_fruit+"\n")
        inventory.write(expensive_dairy+"\n")
        inventory.write(expensive_vegetable+"\n")
    print() #It will print the most expensive item in each category
    print(f"-----Most expensive item by category-----")
    print(f"{'Product Name':<18}{'Product Type':<18}{'Price':<18}")
    print(f"{expensive_fruitName:<18}{'Fruit':<18}{max_fruit:<18}")
    print(f"{expensive_dairyName:<18}{'Dairy':<18}{max_dairy:<18}")
    print(f"{expensive_vegetableName:<18}{'Vegetable':<18}{max_vegetable:<18}")

def total_price(): #This function will calculate the total price of all the items in the inventory
    total_price=0
    name=""
    inventory=open("inventory_Orlando.txt", "r")
    record = inventory.readline().rstrip()
    while record != "":
        fields = record.split(" ")
        total_price=float(fields[3])*int(fields[4])#It will multiply the price by the quantity after converting them to float
        name=fields[1] #It will get the name of the item
        record = inventory.readline().rstrip()
        with open("total_Orlando.txt", "a") as total:#appends the total price to a different file each time
            total.write(name+" "+str(total_price)+"\n")
        print(f"Total price of: {name} {total_price}")
    inventory.close() #closes the file after the loop is done and everything is appended
    
try:
    if __name__ == "__main__": #This will run the main function
        main()
except KeyboardInterrupt:
    print("Program terminated by user") #This will catch a keyboard interrupt and print a message