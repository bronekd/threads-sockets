#The user types in value in a list. After that, two threads start. The first thread finds the largest value in the list.
#The second thread finds the smallest value un the list.
# The results are displayed on the screan.

# moje řešení:
import threading
import time

# Funkce, kterou budeme volat v každém vlákně

a = [1,2,3,4,5,6,7,8,9,10]
def num_min(a):
    print(min(a))
def num_max(a):
    print(max(a))


# Vytvoření dvou vláken
thread1 = threading.Thread(target=num_min(a), args="Vlákno 1")
thread2 = threading.Thread(target=num_max(a), name="Vlákno 2")

# Spuštění vláken
thread1.start()
thread2.start()

# Čekání na dokončení obou vláken
thread1.join()
thread2.join()

print("Hlavní vlákno skončilo.")



# řešení od učitele:
