class Account:
    def __init__(self, account_no, name, address, tel, balance):
        self.__account_no = account_no
        self.__name = name
        self.__address = address
        self.__tel = tel
        self.__balance = balance

    def get_account_no(self):
        return self.__account_no

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tel(self):
        return self.__tel
    
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def display(self):
        print("Account No:", self.__account_no)
        print("Name:", self.__name)
        print("Balance:", self.__balance)
