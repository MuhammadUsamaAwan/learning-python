class Car:
    color = None


class Truck:
    color = None


def change_color(vehicle, color):
    vehicle.color = color


car1 = Car()
car2 = Car()
truck1 = Truck()
change_color(car1, "red")
change_color(car2, "blue")
change_color(truck1, "green")
print(car1.color)
print(car2.color)
print(truck1.color)
