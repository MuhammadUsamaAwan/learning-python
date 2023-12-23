import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You have finished eating breakfast.")


def drink_coffee():
    time.sleep(4)
    print("You have finished drinking coffee.")


def study():
    time.sleep(5)
    print("You have finished studying.")


# eat_breakfast()
# drink_coffee()
# study()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print("Finished doing all tasks!")
