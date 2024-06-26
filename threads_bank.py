# transakce na databazi se nazývá bank

#vzor od učitele mění se hodnota odečítá se vždy od jednoho čísla.
import threading
import time
# Globální proměnná sdílená mezi vlákny
balance = 1000

# Funkce reprezentující transakci
def make_transaction(amount):
    global balance
    current_balance = balance
    # Simulace nějakého výpočtu nebo operace
    # Mezitím může jiné vlákno změnit hodnotu balance
    # a tím způsobit race condition
    time.sleep(0.2)
    balance = current_balance - amount

# Vytvoření dvou vláken pro provedení transakcí
thread1 = threading.Thread(target=make_transaction, args=(200,))
thread2 = threading.Thread(target=make_transaction, args=(300,))


thread1.start()
time.sleep(0.2)
thread2.start()


thread1.join()
thread2.join()

# Očekávaný výsledek je 500, ale může být odlišný kvůli race condition
print("Zůstatek na účtu po transakcích:", balance)



#další řešení
# Globální proměnná sdílená mezi vlákny
balance = 1000

# Vytvoření Threading Lock
lock = threading.Lock()

# Funkce reprezentující transakci
def make_transaction(amount):
    lock.acquire()
    try:
        global balance
        current_balance = balance
        # Simulace nějakého výpočtu nebo operace
        # Mezitím může jiné vlákno změnit hodnotu balance
        # a tím způsobit race condition
        time.sleep(0.2)

        balance = current_balance - amount
    finally:
        # Uvolnění zámku
        lock.release()

# Vytvoření dvou vláken pro provedení transakcí
thread1 = threading.Thread(target=make_transaction, args=(200,))
thread2 = threading.Thread(target=make_transaction, args=(300,))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

# Očekávaný výsledek je 500, ale může být odlišný kvůli race condition
print("Zůstatek na účtu po transakcích 2:", balance)



# řešení od učitele pomocí with lock:

import threading
import time


balance = 1000
lock = threading.Lock()

def make_transaction(amount):
    global balance

    with lock:
        current_balance = balance

        time.sleep(0.1)
        balance = current_balance - amount


thread1 = threading.Thread(target=make_transaction, args=(200,))
thread2 = threading.Thread(target=make_transaction, args=(300,))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

# Očekávaný výsledek je 500, ale může být odlišný kvůli race condition
print("Zůstatek na účtu po transakcích:", balance)



