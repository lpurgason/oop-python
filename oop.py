# Python Object-Oriented Programming

import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}.@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name Deleted!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)


# # see number of employees before creation
# print(Employee.num_of_emps)
#
# # create new employees
# emp_1 = Employee("Leslie", "Purgason", 70000)
# emp_2 = Employee("Test", "User", 60000)
#
# # see number of employees after creation
# print(Employee.num_of_emps)
#
# # print Employee.fullname method output
# print(emp_1.fullname)
#
# # apply raise to individual employee
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#
# # change raise amount for all employees
# Employee.raise_amount = 1.05
#
# # change raise amount for one employee
# emp_1.raise_amount = 1.06
#
# # set raise to all employees amount using class method
# Employee.set_raise_amt(1.05)
#
# # use class method as alternative constructor to parse string
# emp_str_1 = "John-Doe-70000"
# new_emp_1 = Employee.from_string(emp_str_1)
#
# # use static method to check if given date is a work day
# my_date = datetime.date(2020, 1, 12)
# print(Employee.is_workday(my_date))
#
# # see changes in raise amounts
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# # see attributes from instance and class
# print(emp_1.__dict__)
# print(Employee.__dict__)
#
# # create new developer employees (inherited from Employee class)
# dev_1 = Developer("Chris", "Johnson", 70000, "Python")
# dev_2 = Developer("Dev_Test", "Dev_User", 60000, "Java")
#
# print(dev_1.email)
# print(dev_1.prog_lang)
#
# # create new manager employees (inherited from Employee class)
# mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
#
# # see Manager class in action
# print(mgr_1.email)
#
# mgr_1.print_emps()
# print('\n')
#
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# print('\n')
#
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()
#
# # see representation and string
# print(repr(emp_1))
# print(str(emp_1))
#
# # see result from __add__ special method
# print(emp_1 + emp_2)
#
# # see result from __len__ special method
# print(len(emp_1))
#
# # use fullname setter to change first and last name
# emp_1.fullname = 'Jane Smith'
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
#
# # use fullname deleter to delete employee
# del emp_1.fullname
#
# # check if an object is an instance of a class
# print(isinstance(mgr_1, Manager))  # --True
# print(isinstance(mgr_1, Employee))  # --True
# print(isinstance(mgr_1, Developer))  # --False
#
# # check if class is a subclass of another class
# print(issubclass(Developer, Employee))  # --True
# print(issubclass(Manager, Employee))  # --True
# print(issubclass(Manager, Developer))  # --False
#
#
# # see help for classes
# print(help(Developer))

