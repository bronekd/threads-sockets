#když se zaseknu v programu

# tento program se zacyklí
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

# Funkcia, ktorá spôsobí deadlock
def deadlock_function1():
    lock1.acquire()
    print("Thread 1 získalo lock1")

    time.sleep(1)

    lock2.acquire()
    print("Thread 1 získalo lock2")

    lock1.release()
    lock2.release()

# Funkcia, ktorá spôsobí deadlock
def deadlock_function2():
    lock2.acquire()
    print("Thread 2 získalo lock2")

    time.sleep(1)

    lock1.acquire()
    print("Thread 2 získalo lock1")


    lock2.release()
    lock1.release()

thread1 = threading.Thread(target=deadlock_function1)
thread2 = threading.Thread(target=deadlock_function2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


