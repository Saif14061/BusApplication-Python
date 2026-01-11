import csv
import pandas
pandas.set_option("display.max_row", None)
from getpass import getpass #modual which allow the password to be blured out and stop others from seeing it
from datetime import datetime #date and time for customer ticket purhcese
import os #modual i found which make the TUI (Terminal User Interface) look much clearner
import time#modual i found which make the interface go slower 
#class for purchses for customer
class purchases: #class used to store purhcase ticket from the customer showing the price time and ticket they bought
    def __init__(self, title, price, time):
        self.title = title
        self.price = price
        self.time = time
    def to_list(self):
        return[self.time, self.title, self.price]
class caterogies: #class to show off all the caterogies for the users to pick from also added a dictornery
    def __init__(self,name): #self is the object for a category
        self.name = name #value which passs when the object is crated 
        self.tickets = [] #link the catoery to the right ticket which is belongs to 

def clear():
    os.system("cls" if os.name == "nt" else "clear")
purches_ticket = "ticket.csv" #csv file for the tickets which be purchsed by a customer

#importing the CSV file
tickets = [] #list appending the tickets
with open("mobile_products.csv", encoding = "utf-8") as file:
    reader = csv.DictReader(file) #allow each row to become a dictionary automaticly
    for row in reader:
        tickets.append(row)

categores = {}
for row in tickets:
    categoreis = row["category_title"]

    if categoreis not in categores:
        categores[categoreis] = caterogies(categoreis) # categories dictonery groups all the categories making eaier to display though code
    categores[categoreis].tickets.append(row)




def save_csv(): #can re-use the function again though out the code if needed 
    try:
        with open("mobile_products.csv", "w", encoding="utf-8", newline="") as file:
            fieldname = tickets[0].keys()
            writer = csv.DictWriter(file, fieldnames = fieldname)
            writer.writeheader() #allow the document to be saved making sure admin modify data is correct
            writer.writerows(tickets)

        print("the csv file has been saved")
    except Exception as e:
        print(f"csv did not save due to error: {e}")
        



def customer():
    clear() #this is the customer menu option
    print("===Customer===")
    print("1. purchase ticket")
    print("2. Purchase History")
    print("3. Main Menu")
    
    customer_option = input("Select the following option: ")

    if customer_option == ("1"):
        ticket_purchese()
    elif customer_option == ("2"):
        purchse_history()
    elif customer_option == ("3"):
        return

def ticket_purchese():
    clear()
    categoreis_list = list(categores.keys())
    #below code for the caegorys for the user 
    print("==pick a category==")
    for i, categoreis in enumerate(categoreis_list): #reusing the code again to show the categoreies off
        print(i, categoreis)
    while True:
        catego_choice = input("pick the category: ")
        if catego_choice.isdigit():
            catego_choice = int(catego_choice)
            break
        else:
            print("enter in a valid number: ")
    selected_choice = categoreis_list[catego_choice] #re used code from admin and customer table to show off categories 
    ticket_cat = categores[selected_choice].tickets
    df = pandas.DataFrame(ticket_cat)
    print(df)

    
    print("==Purchese Tickets==")
    for i, row in enumerate(ticket_cat):
        title = row["topup_title"] #reusing the code from the admin menus
        price = int(row["topup_price_in_pence"]) / 100 #change the price into pounds 
        print(f"{i}. {title:<25} £{price:.2f}")
    while True:
        ticket_num = input("pick the ticket: ")
        if ticket_num.isdigit():
            ticket_num = int(ticket_num)
            break
        else:
            print("enter in a valid number: ")
    num_selected = ticket_cat[ticket_num]#code reused from the admin just dose the same 
    ticket_duration = num_selected["topup_entitlement_value"]
    ticket_unit = num_selected["topup_entitlement_unit"]
    if ticket_duration == "":
        start = num_selected["topup_entitlement_start_date"]
        end = num_selected["topup_entitlement_end_date"]
        print(f"the ticket is only valid till {start} till the {end}")
    else:
        print(f"the ticket is valid untill {ticket_duration} {ticket_unit}")

    

    ticket_quantity = num_selected["topup_entitlement_quantity"]
    print(f"u have this meny ticket: {ticket_quantity}") #show the quantity of the ticket resued the code form the duration

    numer_people_per_ticket = num_selected["topup_passenger_class_quantity"] #this is the code to see number people per ticket 
    print(f"number people per ticket: {numer_people_per_ticket}")

    price_ticket = int(num_selected["topup_price_in_pence"]) /100 #change the price into pounds 
    ticket_time = datetime.now().strftime("%Y-%M-%D %H:%M:%S") #the date and time and show the correct formate with in the csv file

    new_ticket_bought = purchases(title, price_ticket,ticket_time ) #links the the class which i made above
    #save purchses to the csv code below:
    with open(purches_ticket, "a" , encoding="utf-8", newline="") as file:
        writer = csv.writer(file) #link to the code make a extra csv showing the ticket bought and the date and time
        if file.tell() == 0:
            writer.writerow(["time","title","price"])
        
        writer.writerow(new_ticket_bought.to_list())
    print("the ticket has been bought/purchsed")
    time.sleep(3)
    customer()


def purchse_history():
    print("==Purhase History==")
    print(pandas.read_csv(purches_ticket))
    time.sleep(3)
    customer()
    
    


    
    

def admin():
    clear() #this is the admin menu option
    print("===Admin===")
    print("1. Modify CSV")
    print("2. Save CSV File")
    print("3. view csv")
    print("4. main menu")
    admin_option = input("Select the following option: ")

    if admin_option == ("1"):
        modify_csv()
    elif admin_option == ("2"):
        save_csv()
    elif admin_option == ("3"):
        view_csv()
    elif admin_option == ("4"):
        return
    
    

def modify_csv():
    
        print("==modify csv==")
        for i, row in enumerate(tickets): 
            title = row["topup_title"]
            price = int(row["topup_price_in_pence"]) / 100 #show the ticket prices in pounds allow the prices to be changed by the admin
            print(f"{i}. {title:<25} £{price:.2f}")

        while True:
            row_choice = input("choose ticket u like to change")
            if row_choice.isdigit():
                row_choice = int(row_choice)
                break
            else:
                print("re-enter a valid number")

        row_selected = tickets[row_choice] #Hole function allow the price to be picked and sorted and changed

        

        while True:
            modify_price = input("type the new price in (£): ")
            if modify_price.isdigit():
                modify_price = int(modify_price)
                break
            else:
                print("re-enter a write value: ")

        row_selected["topup_price_in_pence"] = str(int(modify_price * 100)) #turn price pennies into pounds

        print(f"price has been changed to £{modify_price}") #show the prices have been changed

        #saving the new data on the csv file on top of the code:
        save_csv()#importing the csv file into the function from another function
        admin() 


def view_csv():
    print("==view csv==")
    print("==Purhase History==")
    df = pandas.read_csv("mobile_products.csv")
    print(df[["topup_title", "category_title","topup_price_in_pence"]])
    input("press enter to return to admin: ")
    admin()


def menu(): #this is the main menu option
    while True:
        clear()
        print("===Main Menu===")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        userchoice = input("Select the following option: ")
        #making the password so if user get it wrong it loop otherwise they can type ("main menu") to go back
        if userchoice == ("1"):
            customer()
        elif userchoice == ("2"):
            while True:
                admin_pass = getpass("enter in password: ") #getpass make the password enypted so no-one can see it
                if admin_pass == "123admin":
                    admin()
                    break
                elif admin_pass == "main menu":
                    print("returning to the main menu........")
                    break
                else:
                    print("passcode is invalid")
            

        elif userchoice == ("3"):
            print("closing application")
            break
menu()
#end of project