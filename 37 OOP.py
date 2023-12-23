class Car:
    make = None
    model = None
    year = None

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("You drive the " + self.make + " " + self.model + " " + str(self.year))


ford = Car(make="Ford", model="Mustang", year=1969)
ford.drive()
