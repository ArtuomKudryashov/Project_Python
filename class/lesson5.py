class Person:

    country = "USA"


    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.__salary = salary

    def hello(self):
        return f'{self.fname}{self.lname} says hello'

    def get_salary(self):
        return  self.__salary
    def set_salary(self, new_salary):
        self.__salary = new_salary


person_1 = Person('Alex', " Baker",30000)

print(person_1.lname)
print(person_1.fname)

print(person_1.__dict__)
print(person_1.hello())
print(person_1.country)

person_2 = Person('Kevin', ' Smith',15000)
print(person_2.lname)
print(person_2.fname)
print(person_2.__dict__)

print(person_2.hello())
person_2.country

print(person_1._Person__salary)


#
class Developer(Person):
    def __init__(self, fname, lname, salary, language, job_title):
        super().__init__(fname, lname,salary)
        self.language = language
        self.job_title = job_title


    def coding(self):
        return f'I\'m coding with {self.language}'





coder_1 = Developer('Alejandro', 'Villiarrel', 10000,'Python', 'Senior developer' )
print(coder_1.fname)
print(coder_1.lname)
print(coder_1.language)
print(coder_1.job_title)
print(coder_1.country)
print(coder_1.get_salary())
coder_1.set_salary(25000)
print(coder_1.get_salary())

print(coder_1._Devaloper__salary)






class Tester(Person):
    def __init__(self, fname, lname, salary, framework, job_title):
        super().__init__(fname, lname, salary)
        self.framework = framework
        self.job_title = job_title


    def testing(self):
        return f'I\'m testing with {self.framework}'


tester_1 = Tester('Yroslav', 'Popov', 20500, 'Pytest','SDET')
print(tester_1.fname)
print(tester_1.lname)
print(tester_1.framework)
print(tester_1.job_title)
print(tester_1.country)

