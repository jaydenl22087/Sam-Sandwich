import datetime
#This program will allow the user to enter in a name 
def force_name(message, lower, upper):
    while True:
        name = str(input(message)).title()
        if len(name) >= lower  and len(name) <= upper and name.isalpha():
            print("The name is valid")
            break
        else:
            print("Invalid name")
    return(name)

def force_phone(message, lower, upper):
    while True: #Make it an infinite loop that keeps repeating until a valid number is entered
        cell = str(input(message))
        if len(cell) >= lower and len(cell) <= upper and cell.isnumeric():
            break
        else:
            print(f"Error! please enter between a {lower} - {upper}")
    return cell #returning back a valid number between the range


def force_number(message, lower, upper):
    while True: 
        try:
            number = int(input(message))
            if number >= lower and number <= upper:
                print("Good choice")
                break
            else:
                print("This number is not a valid number, try again")
        except:
            print("Error, please a number and not text")
    return(number)
        
def bread_selection():
    bread_list = ["White","Brown","Italian","Granary"]
    count = 0
    print("We have the following breads:")
    while count < len(bread_list): #Prints out each item on the list
        print(count +1," ", bread_list[count])
        count += 1 
    bread_selected = force_number("Which bread would you like? Enter a number",1,4)
    return bread_list[bread_selected-1] #Returns back a string 

def meat_selection():
    meat_list = ["Ham", "Salami","Turkey","Roat Beef","Chicken","Pork Belly"]
    count = 0
    print("We have the following meats avalible:")
    while count < len(meat_list): #Print out each item on the list
        print(count +1," ", meat_list[count])
        count += 1
    meat_selected = force_number("Which meat would you like? Enter a number",1,7)
    return meat_list[meat_selected-1]

def cheese_selection():
    cheese_list = ["Cheese","American","Swiss","Provolone","Mozzarella","Havarti","Brie"]
    count = 0
    print("We have the following cheese avalible:")
    while count < len(cheese_list): #Print out each item on the list
        print(count +1," ", cheese_list[count])
        count += 1
    cheese_selected = force_number("Which cheese would you like? Enter a number",1,8)
    return cheese_list[cheese_selected-1]

def salad_selection():
    salad_list = ["lettuce","Tomato","Mixed Greens","Coleslaw","Beetroot","Carrots","Capcicum","Onions"]
    count = 0 
    print("We have the following Salad selection avalible")
    while count < len(salad_list):
        print(count+1," ", salad_list[count])
        count += 1
    print("Press ENTER when you have finished choosing your salad")
    salad_added = "" #Will hold a string of more than one item
    selected_salad = " "#Promtps the user to enter a number to select a salad. 

    while selected_salad != "":
        selected_salad = input("What salad do you want? ")
        if selected_salad != "": #If you press enter the if statement won't run
            selected_salad = int(selected_salad)
            #This variable keeps adding on each selected item from the salad list
            salad_added = salad_added + " " + salad_list[selected_salad-1]
            print(f"You have selected {salad_added}")
    return salad_added.strip() #Removes empty space at the start of the string 

def dressing_selection():
    dressing_list = ["BBQ","Tomato Sause","teriyaki","Garlic aioli","Mustard","Mayonnaise","None"]
    count = 0 
    print("We have the following dressings avalible")
    while count < len(dressing_list):
        print(count+1," ",dressing_list[count])
        count+=1
    dressing_selected = force_number("Which cheese would you like? Enter a number",1,7)
    return dressing_list[dressing_selected-1]

def main_menu():
    sandwich_order = []
    print("Welcome to Sam's Sandwich Shop")
    first_name = force_name("Please enter your first name ",2,20)
    cellphone_number = force_phone("Please enter your phone number ",8,10)
    bread_choice = bread_selection()
    meat_choice = meat_selection()
    cheese_choice = cheese_selection()
    salad_choice = salad_selection()
    dressing_choice = dressing_selection()

    print("----------Your Order----------")
    print(f"First Name: {first_name}")
    print(f"Phone Number: {cellphone_number}")
    print(f"Your selected bread: {bread_choice}")
    print(f"Your selected meat: {meat_choice}")
    print(f"Your selected cheese: {cheese_choice}")
    print(f"Your selected salad: {salad_choice}")
    print(f"Your selcted dressing: {dressing_choice}")
    print("----------End----------")

    sandwich_order.append(f"First Name: {first_name}")#First Name
    sandwich_order.append(f"Phone Number: {cellphone_number}")#Phone number
    sandwich_order.append(f"Your selected bread: {bread_choice}")#Bread Choice
    sandwich_order.append(f"Your selected meat: {meat_choice}")#Meat Choice
    sandwich_order.append(f"Your selected cheese: {cheese_choice}")#Cheese Choice
    sandwich_order.append(f"Your selected salad: {salad_choice}")#Salad Choice
    sandwich_order.append(f"Your selcted dressing: {dressing_choice}")#Dressing Choice
    output_textfile(first_name,cellphone_number,sandwich_order)

def output_textfile(first_name,cellphone_number,sandwich_order):
    date_time = datetime.datetime.now()
    outFile = open("sams_sandwich.txt","a")#Opening up a new text file 
    print(f"***Order for {first_name} - {cellphone_number}***")
    outFile.write(f"\nDate of Order: {date_time}\n")
    for booking in sandwich_order:
        print(booking)#printing each 
        outFile.write(f"{booking}")
        outFile.write("\n")
    print("\nOrder Complete")
    print(f"Your confirmation has been saved to 'sams_sandwich.txt.")
    outFile.close()#Closes off the text file
    #once the file prints, it goes back to the menu

#Main Program 
main_menu()


