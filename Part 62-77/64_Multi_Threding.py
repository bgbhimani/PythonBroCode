# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  for I/O bound tasks like reading files or fetching data from APIs
#                  threading. Thread (target=my_function)

import threading
import time

def walk_dog(first,last):
    time.sleep(5)
    print(f"You finished Walking Dog {first} {last}")
    
def take_out_trash():
    time.sleep(2)
    print("You take out the trash")
    
def get_mail():
    time.sleep(3)
    print("You get the mail")


print("Hii This is Morning")

chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))  #  "," for tuple
chore1.start()
chore2 = threading.Thread(target=get_mail)
chore2.start()
chore3 = threading.Thread(target=take_out_trash)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All the Work Completed")
