
class Person() :
    def __init__(self,name,age,gender,money) :
        self.name = name
        self.age = age
        self.gender = gender
        self.money = money
 

class Flight() :
    def __init__(self,capacity,route,price) :
        self.capacity = capacity
        self.passangers = []
        self.route = route
        self.price = price

    def open_seats(self) :
        return self.capacity - len(self.passangers)      

    def add_passanger(self,person) :
        if(self.open_seats() > 0 and person.money >= self.price):
            self.passangers.append(person) 
            print(f"passanger {person.name} is added succesfully!")
        else:
            if(self.open_seats() <= 0) :
                       print(f"flight capacity is full so {person.name} is could not added. ")
            
            elif(person.money < self.price):
                    print(f"passanger {person.name} does not have enough money to buy ticket (ticekt price is : {self.price}, passanger's money is {person.money})")

    def summary_of_person(self,person):
        if(person in self.passangers):
            print (f"name of the person is {person.name}, age is {person.age} and gender is {person.gender}")
        else :
            print (f"{person.name} is not in this flight list.")   

    def showPassangers(self) :
        for i in range(len(self.passangers)):
            passList = []
            print(self.passangers[i].name)

    def flightInfo(self) :
         print(f"flight infos : plane capacity is {self.capacity}, route is from { self.route.split('-')[0] } to { self.route.split('-')[1] } and ticket price is {self.price}")        


      
        
flight1 = Flight(3,"Ankara-İstanbul",500)



emre = Person("Emre", 24, "male",400)
hakan = Person("Hakan", 21, "male",800)
cansu = Person("Cansu", 35, "female",900)
eren = Person("Eren", 21, "male",1000)
buse = Person("Buse", 17, "female",200)

people = [emre,hakan,cansu,eren,buse]

for person in people:
    flight1.add_passanger(person)


flight1.showPassangers()    

flight1.flightInfo()




flight1.summary_of_person(emre)
flight1.summary_of_person(eren)





