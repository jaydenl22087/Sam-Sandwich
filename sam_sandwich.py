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
    bread_selected = bread_selected*2-2
    return bread_list[bread_selected] #Returns back a string 

#Main Program 
print("Welcome to Sam's Sandwich Shop")
bread_choice = bread_selection()
print(f"Your selected bread: {bread_choice}")


