class Employee():
    hike=1.06
    def __init__(self,fname,lname,pay):    #Constructor
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@gamil.com'

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def appraisal(self):
        #self.hike=hike
        self.salary=self.salary*self.hike

    @classmethod
    def create_object(cls,input_str):
        fn,ln,sal=input_str.split('-')
        return cls(fn,ln,int(sal))

    @staticmethod
    def is_workingday(d):
        if d.weekday()==5 or d.weekday()==6:
            return "HOLIDAY!"
        else:
            return "Workingday!"
    def __repr__(self):
        return "This is the Employee class object"

    def __str__(self):
        return "EMPLOYEE class object!"

    def __add__(self,other):
        return self.salary+other.salary

    def __len__(self):
        return len(self.fullname())
    #DUNDER METHOD


class Developer(Employee):
    def __init__(self,fname,lname,pay,tech):
        self.tech=tech
        super().__init__(fname,lname,pay)

dev_1=Developer('Ramya','Rajesh',10000,'Java')
dev_2=Developer('Siva','Murugan',20000,'CPP')

print(dev_1.email, dev_1.tech)
print(dev_2.email, dev_2.tech)
# str1='Levin-Lenus-100000'
# str2='Dinesh-Kumar-200000'
#
# emp_1=Employee.create_object(str1)    #Employee('Levin','Lenus',100000)
# emp_2=Employee.create_object(str2)    #Employee('Dinesh','Kumar',200000)

#print(emp_1+emp_2)
# print(len(emp_1))
# print(len(emp_2))
# print(emp_1)
# print(emp_2)
# print(emp_1.fullname())
# print(emp_2.fullname())

# import datetime
# dt=datetime.date(2022,8,30)
# print(Employee.is_workingday(dt))
# fn,ln,sal=str1.split('-')
# emp_1=Employee(fn,ln,int(sal))
#
# fn,ln,sal=str2.split('-')
# emp_2=Employee(fn,ln.int(sal))


# emp_1=Employee('Raghul','Ramesh',50000)
# emp_2=Employee('Bala','Murugan',60000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())
# emp_1.hike=1.1
# print(emp_1.salary)
# emp_1.appraisal()
# print(emp_1.salary)
# print("=========")
# print(emp_2.salary)
# emp_2.appraisal()
# print(emp_2.salary)

#Types of the methods
# object / instance method
# class method
# static method

#OOPS Features
# Absraction
# Inheritance
# Polymorphism
# Encapsulation