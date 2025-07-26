# COUNTDOWN 

import time

count = int(input("Type time to countdown (sec) : "))

for x in range(count,-1, -1) :                       # menghitung mulai dari {count}, sampai 0, reversed.
    seconds = x % 60                                 # supaya ga lebih dari 60
    mins = int(x / 60) % 60
    hs = int(x / 3600) % 24
    days = int(x / 24) 
    print(f"{hs:02} h {mins:02} min {seconds:02} s")
    time.sleep(1)

print("HBD CHERRY!")

