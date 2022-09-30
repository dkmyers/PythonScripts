#simple class
class Car:
    color = 'Undefined'
    def __init__(self):
        self.color = 'gray'
    def setColor(self, givenColor):
        self.color = givenColor
    def describeSelf(self):
        print("A", self.color, "car.")
    def describeCar(self):
        print("A", Car.color, "car.")

#simple inheritance of simple class
class Truck(Car):
    color = 'Truck'

    def __init__(self):
        self.color = 'gray truck'

    #simple polymorphism by overloading function
    def describeSelf(self):
        print("A", self.color, "but actually is a truck yes.")

    #simple polymorphism by adding a function
    #(I think that still counts as polymorphism,
        #but it might just be inheritance again)
    def describeTruck(self):
        print("A", Truck.color, "truck.")

test = Car()
test.describeSelf()
test.describeCar()
test.setColor("Blue")
test.describeSelf()
test.size = 'small'
print(test.size)

testerson = Truck()
testerson.describeSelf()
testerson.describeCar()
testerson.describeTruck()
