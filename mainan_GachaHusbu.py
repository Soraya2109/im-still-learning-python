# 11. GACHA HUSBU

import random

husbu = []
number = 1

while True :
    user = input(f"Masukkan husbu ke-{number} : ").upper()
    if user == "Q" or user == " " :
        break
    else :
        husbu.append(user)
    
    number += 1

print("-----Sedang Memilih...-----")
for husbus in husbu :
    print(husbus)

terpilih = random.choice(husbu)
print("--------------------")
print(f"Menikahlah dengan {terpilih} ! ^ w ^")

