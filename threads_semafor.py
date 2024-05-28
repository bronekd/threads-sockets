# semafor určím poček kolik jich může přistoupit k těm vláknům a kolik procesor pustí procesů

import threading
import time

# Vytvorenie semaforu s počiatočnou hodnotou 3
semaphore = threading.Semaphore(3)


def access_shared_resource(thread_id):
    print(f"Vlákno {thread_id} čaká na prístup.")

    # Pokus o získanie povolenia od semaforu
    with semaphore:
        print(f"Vlákno {thread_id} získalo prístup.")
        time.sleep(2)
        print(f"Vlákno {thread_id} uvoľnilo prístup.")


threads = []
for i in range(1, 5):
    thread = threading.Thread(target=access_shared_resource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Všetky vlákna ukončené.")
