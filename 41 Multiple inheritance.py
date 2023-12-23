class Prey:
    def flee(self):
        print("This animal flees")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    def run(self):
        print("This rabbit is running")


class hawk(Predator):
    def fly(self):
        print("This hawk is flying")


class fish(Prey, Predator):
    def swim(self):
        print("This fish is swimming")
