# MENGHITUNG V/LP BANGUN RUANG KUBUS DAN BALOK

print("welcome! menyediakan kalkulator untuk rumus volume dan luas permukaan bangun ruang")

rumus = input("Mau hitung apa? (volume atau luas permukaan) : ")


if rumus == "volume" :
    bangun = input("Bangun ruang apa? (lowercase) : ")
    if bangun == "kubus" :
        rusuk = float(input("rusuk :"))
        result = pow(rusuk, 3)
        print(f" Volume kubusnya adalah {result}cm")

    elif bangun == "balok" :
        pa = float(input("Panjang = "))
        le = float(input("Lebar = "))
        ti = float(input("Tinggi = "))
        result = pa * le * ti
        print(f" Volume baloknya adalah {result}cm")

    else :
        print("lu mau hitung bangun apa kocak??")


elif rumus == "luas permukaan" :
    bangun = input("Bangun ruang apa? (lowercase) : ")
    if bangun == "kubus" :
        rusuk = float(input("rusuk :"))
        result = 6 * pow(rusuk, 2)
        print(f"Luas permukaan kubusnya adalah {result}cm")

    elif bangun == "balok" :
        pa = float(input("Panjang = "))
        le = float(input("Lebar = "))
        ti = float(input("Tinggi = "))
        result = 2 * ((pa * le) + (pa * ti) + (le * ti))
        print(f"Luas permukaan baloknya adalah {result}cm")

    else :
        print("lu mau hitung bangun apa kocak??")



while rumus != "volume" and rumus != "luas permukaan":
    print("watdehek??")
    break






