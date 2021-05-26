class Employee:
    raise_amt=1.05
    num_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'123@gmail.com'
        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

    @staticmethod
    def is_workday(day):
        if day.weekday==5 or day.weekday==6:
            return False
        return True

emp_1=Employee('corey','schafer',50000)
emp_2=Employee('Pratik','Kagale',50000)

emp_str_1='John-Deo-70000'
emp_str_2='Steve-smith-80000'

first,last,pay=emp_str_1.split('-')
new_emp_1=Employee(first,last,pay)

print(new_emp_1.email)
print(new_emp_1.fullname())



import datetime
my_date=datetime.date(2021,5,25)
print(Employee.is_workday(my_date))