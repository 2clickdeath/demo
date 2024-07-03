import os
import threading

file_prefix = "file"

def create_file(name):
    with open(name, "w") as f:
        while True:
            f.write("A" * 10**6) 

def use_ram():
    array = []
    try:
        while True:
            array.append('A' * 10**6)  
    except MemoryError:
        print("100% Reached!")

file_threads = []
for i in range(5):
    file_name = f"{file_prefix}{i}.txt"
    thread = threading.Thread(target=create_file, args=(file_name,))
    file_threads.append(thread)
    thread.start()

ram_threads = []
for _ in range(5):
    thread = threading.Thread(target=use_ram)
    ram_threads.append(thread)
    thread.start()

for thread in file_threads:
    thread.join()

for thread in ram_threads:
    thread.join()
