store = [("shirt", 20.00), ("pants", 25.00), ("jacket", 50.00), ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.8)

store_euros = list(map(to_euros, store))

print(store_euros)
