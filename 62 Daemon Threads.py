import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.daemon = True
print(x.isDaemon())

x.start()

answer = input("Do you wish to exit? ")

if answer.lower().strip() == "yes":
    exit()
else:
    print("Thank you for staying logged in!")
