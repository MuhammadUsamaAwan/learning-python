import time

current_time = time.localtime()
print("Current time:", time.strftime("%H:%M:%S", current_time))
print("Current date and time:", time.strftime("%Y-%m-%d %H:%M:%S", current_time))

time_string = "17 February, 2021"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)
