class Duck:
    def talk(self):
        print("Quack Quack")

    def walk(self):
        print("Walks like a duck")


class Chicken:
    def talk(self):
        print("Cluck Cluck")

    def walk(self):
        print("Walks like a chicken")


class Person:
    def catch(self, duck):
        duck.talk()
        duck.walk()
        print("You caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)
person.catch(chicken)
