import multiprocessing
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(multiprocessing.cpu_count())
    a = multiprocessing.Process(target=counter, args=(250000000,))
    b = multiprocessing.Process(target=counter, args=(250000000,))
    c = multiprocessing.Process(target=counter, args=(250000000,))
    d = multiprocessing.Process(target=counter, args=(250000000,))
    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("Finished in: ", time.perf_counter(), "seconds")


if __name__ == "__main__":
    main()
