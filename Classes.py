#1
class Address:
    def __init__(self, houseNumber, street, city, state, postalCode, aptNumber=""):
        self.houseNumber = houseNumber
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.aptNumber = aptNumber

    def print(self):
        print('Street: ' + self.street)
        print('City: ' + self.city + ', State: ' + self.state + ', Postal code: ' + self.postalCode)

    def comesBefore(self, other):
        return self.postalCode < other.postalCode

a = Address("1234", "Gerdin", "Ames", "IA", "50399", "Apt# 5678")
b = Address("123", "Elm Street", "Ankeny", "IA", "50023")
a.print()
b.print()

#3
class CashRegister:
    def __init__(self):
        self.items = []
        self.prices = {}
        self.total = 0
        self.count = 0
    def addItem(self,item,price):
        self.items.append(item)
        self.prices[item] = price
    def getTotal(self):
        for i in self.items:
            self.total += self.prices[i]
        return self.total
    def getCount(self):
        for i in self.items:
            self.count += 1
        return self.count
    def displayAll(self):
        for i in self.items:
            print(i,":",self.prices[i])
    def clear(self):
        self.items = []
        self.prices = {}
        self.total = 0
        self.count = 0

c = CashRegister()
c.addItem(0,.99)
c.addItem(0,2.99)
c.addItem(0,2.99)
print(c.getTotal())
print(c.getCount())
c.displayAll()

#4
class Student:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    def print(self):
        print(self.name, "is from", self.hometown)

name_list = ["Tod", "Joe", "Sarah"]
hometown_list = ["Palatine", "Ames", "Carol Stream"]
obj = []

for i in range(0, 3):
    obj.append(Student(name_list[i], hometown_list[
        i]))
    obj[i].print()

#5
class olym:
    def __init__(self, year1, year):
        self.year1 = year1
        self.year = year

    def print(self):
        print(self.year1, self.year)
print("Summer Olympics with no Winter Olympics:")
year1_list = ["1896", '1900', '1904', '1908', '1912']
year_list = ['2000', '2004', '2008', '2012', '2016',]
obj = []

print("Winter Olympics with no Summer Olympics:")
year1_list = ['1994', '1998', '2002', '2006', '2010']
obj = []

print("Summer AND Winter Olympics in same year:")
year1_list = ['1924', '1928', '1932', '1936', '1948']
year_list = ['1952', '1956', '1960', '1964', '1968']
obj = []

for i in range(0, 7):
    obj.append(olym(year1_list[i], year_list[
        i]))
    obj[i].print()
