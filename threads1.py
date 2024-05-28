import threading
import time

# Funkce, kterou budeme volat v každém vlákně
def print_numbers():
    for i in range(5):
        time.sleep(2)  # Simulace časově náročné operace
        print(f"Vlákno {threading.current_thread().name}: {i}")

# Vytvoření dvou vláken
thread1 = threading.Thread(target=print_numbers, name="Vlákno 1")
thread2 = threading.Thread(target=print_numbers, name="Vlákno 2")
#thread2 = threading.Thread(target=print_numbers, daemon=True, name="Vlákno 2") # ukáza deamon který je ve výchozí hodnotě false. Ukončuje vlákno s koncem programu. 

# Spuštění vláken
thread1.start()
thread2.start()

# Čekání na dokončení obou vláken
thread1.join()
thread2.join()

print("Hlavní vlákno skončilo.")