#staff.py

class Staff():
    def __init__(self, staff_id, name, salary):
        self.__staff_id = staff_id
        self.__name = name
        self.__salary = salary

    def get_staff_id(self):
        return self.__staff_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary
    
    def display(self):
        print("Staff ID: ", self.__staff_id)
        print("Name: ", self.__name)
        print("Salary: ", self.__salary)

class FulltimeStaff(Staff):
    def __init__(self, staff_id, name, salary):
        super().__init__(staff_id, name, salary)
        self.__bonus = 0

    def add_bonus(self, month):
        if month == 'June':
            self.__bonus = self.get_salary() * 1.5
            self.set_salary(self.__bonus)
        if month == 'December':
            self.__bonus = self.get_salary() * 2
            self.set_salary(self.__bonus)

    def gen_payroll(self):
        self.display()

class ParttimeStaff(Staff):
    def __init__(self, staff_id, name, daily_rate, work_days):
        super().__init__(staff_id, name, daily_rate*work_days)
        self.__daily_rate = daily_rate
        self.__work_days = work_days

    def calc_salary(self):
        return self.__daily_rate * self.__work_days

    def gen_payroll(self):
        self.display()
        print("Daily Rate: ", self.__daily_rate)
        print("Work Days: ", self.__work_days)

staff = []
FulltimeStaff1 = FulltimeStaff('S01', 'Bryan', 1000)
staff.append(FulltimeStaff1)
ParttimeStaff1 = ParttimeStaff('S02', 'Ryan', 20, 20)
staff.append(ParttimeStaff1)
FulltimeStaff2 = FulltimeStaff('S03', 'Yan', 1000)
staff.append(FulltimeStaff2)
FulltimeStaff1.add_bonus('June')
for i in staff:
    i.gen_payroll()
    print()
