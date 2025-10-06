import datetime

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
    bread_selected = bread_selected-1
    return bread_list[bread_selected] #Returns back a string 

def meat_selection():
    meat_list = ["Ham", "Salami","Turkey","Roat Beef","Chicken","Pork Belly"]
    count = 0
    print("We have the following meats avalible:")
    while count < len(meat_list): #Print out each item on the list
        print(count +1," ", meat_list[count])
        count += 1
    meat_selected = force_number("Which meat would you like? Enter a number",1,7)
    meat_selected = meat_selected-1
    return meat_list[meat_selected]

def cheese_selection():
    cheese_list = ["Cheese","American","Swiss","Provolone","Mozzarella","Havarti","Brie"]
    count = 0
    print("We have the following cheese avalible:")
    while count < len(cheese_list): #Print out each item on the list
        print(count +1," ", cheese_list[count])
        count += 1
    cheese_selected = force_number("Which cheese would you like? Enter a number",1,8)
    cheese_selected = cheese_selected-1
    return cheese_list[cheese_selected]

def salad_selection():
    salad_list = ["lettuce","Tomato","Mixed Greens","Coleslaw","Beetroot","Carrots","Capcicum","Onions"]
    count = 0 
    print("We have the following Salad selection avalible")
    while count < len(salad_list):
        print(count," ", salad_list[count])
        count += 1
    print("Press ENTER when you have finished choosing your salad")
    salad_added = "" #Will hold a string of more than one item
    selected_salad = " "#Promtps the user to enter a number to select a salad. 

    while selected_salad != "":
        selected_salad = input(f"What salad do you want? \nYou have selected: {salad_added}")
        if selected_salad != "": #If you press enter the if statement won't run
            selected_salad = int(selected_salad)
            #This variable keeps adding on each selected item from the salad list
            salad_added = salad_added + " " + salad_list[selected_salad]
    return salad_added.strip() #Removes empty space at the start of the string 







#Main Program 
sandwich_order = []
print("Welcome to Sam's Sandwich Shop")
bread_choice = bread_selection()
print(f"Your selected bread: {bread_choice}")
meat_choice = meat_selection()
print(f"Your selected meat: {meat_choice}")
cheese_choice = cheese_selection()
print(f"Your selected cheese: {cheese_choice}")
salad_choice = salad_selection()
print(f"Your selected salad(s) are: {salad_choice}")
