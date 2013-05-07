import accounts.py

def menu():
    print("[1] Search")
    print("[2] Create")
    print("[3] Update")
    print("[4] Delete")
    print("[0] Quit")

def search():
    try:
        with open('ACCOUNTS.DAT','r') as f:
            account_no = input("Enter account number: ")
            account_no = account_no.upper()
            
    except IOError:
        print('Cannot read input file')

def create():
    try:
        with open('ACCOUNTS.DAT','a') as f:
            pass
    except IOError:
        print('Cannot append to output file')

def update():


def delete():

    
#main
option = "1"

while option != '0':
    menu()
    option = input("Enter option: ")
    if option == '1':
        search()
    elif option == '2':
        create()
    elif option == '3':
        update()
    elif option == '4':
        delete()
