class Person() :
    def __init__(self,name,age,gender) :
        self.name = name
        self.age = age
        self.gender = gender
 

class Flight() :
    def __init__(self,capacity) :
        self.capacity = capacity
        self.passangers = []

    def open_seats(self) :
        return self.capacity - len(self.passangers)      

    def add_passanger(self,person) :
        if(self.open_seats() > 0):
            self.passangers.append(person) 
            print(f"passanger {person.name} is added succesfully!")
        else : print(f"flight capacity is full so {person.name} is could not added. ")

    def summary_of_person(self,person):
        if(person in self.passangers):
            print (f"name of the person is {person.name}, age is {person.age} and gender is {person.gender}")
        else :
            print (f"{person.name} is not in this flight list.")       

      
        
flight1 = Flight(3)


emre = Person("Emre", 24, "male")
hakan = Person("Hakan", 21, "male")
cansu = Person("Cansu", 35, "female")
eren = Person("Eren", 21, "male")
buse = Person("Buse", 17, "female")

people = [emre,hakan,cansu,eren,buse]

for person in people:
    flight1.add_passanger(person)


flight1.summary_of_person(emre)

flight1.summary_of_person(eren)