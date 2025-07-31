# HITUNG KELILING DAN LUAS BANGUN DATAR

# tapi cuma persegi, persegi panjang, lingkaran hehe

print("Welcome! tools ini ngitung keliling dan luas suatu bangun datar!")

def persegi() :
    sisi = int(input("Sisi persegi : "))
    keliling = 4 * sisi
    luas = pow(sisi, 2)
    print(f"Keliling persegi = {keliling}")
    print(f"Luas persegi = {luas}")

def per_panjang() :
    panjang = int(input("Panjang : "))
    lebar = int(input("Lebar : "))
    keliling = (2 * panjang) + (2 * lebar)
    luas = panjang * lebar
    print(f"Keliling persegi panjang = {keliling}")
    print(f"Luas persegi panjang = {luas}")

def lingkaran() :
    radius = int(input("Jari-jari = "))
    keliling = 2 * 3.14 * radius
    luas = 3.14 * pow(radius, 2)
    print(f"Keliling lingkaran = {keliling} ~ {keliling:.2f} ")
    print(f"Luas lingkaran = {luas} ~ {luas:.2f}")

user = input("Bangun datar : ").lower()
if user == "persegi" :
    persegi()
elif user == "persegi panjang" :
    per_panjang()
elif user == "lingkaran" :
    lingkaran()
else :
    print("Apaansih?!")
    