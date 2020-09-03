class Employee:
    rasie_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.rasie_amt)

class Developr(Employee):
    rasie_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees =None):
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
            print('-->', emp.fullname())


#dev_1 = Employee('Sabbir', 'Ahamed', 1900)
#dev_2 = Employee('Michael', 'Horton', 1700)

dev_1 = Developr('Sabbir', 'Ahamed', 1900, 'Python')
dev_2 = Developr('Michael', 'Horton', 1700, 'Java')

mgr_it = Manager('John', 'Dao', '3500', [dev_1])

print(mgr_it.email)
mgr_it.add_emp(dev_2)
mgr_it.remove_emp(dev_1)

mgr_it.print_emps()

print(isinstance(mgr_it, Developr))
print(isinstance(mgr_it, Employee))
print(isinstance(mgr_it, Manager))

print(issubclass(Developr,Developr))
print(issubclass(Developr, Employee))
print(issubclass(Employee,Employee))
print(issubclass(Manager, Developr))



print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.rasie_amt)
dev_1.apply_raise()
print(dev_1.rasie_amt)

print(dev_1.email)
print(dev_2.email)

print(dev_1.prog_lang)
print(dev_2.prog_lang)

print(help((Developr)))