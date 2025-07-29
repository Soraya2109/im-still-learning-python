# 13. NUMBER GUESSING GAME

import random 

terendah = 1
tertinggi = 5
jawab = random.randint(terendah, tertinggi)
kali_tebak = 0
works = True

while works :
    guess = input(f"Tebak angka antara {terendah} sampai {tertinggi}: ")
    if guess.isdigit() : 
        guess = int(guess)
        kali_tebak += 1

        if guess < terendah or guess > tertinggi :
            print("Angka diluar batas!")
        elif guess < jawab :
            print("Terlalu rendah!")
        elif guess > jawab :
            print("Terlalu tinggi!")
        else :
            print("BENARR! ANDA MENDAPATKAN 1 MILIAR")
            print(f"Kali menebak = {kali_tebak}")
            works = False

    else :
        print("Tolong masukkan angka!!")

