# 18. PERTAMBAHAN DERET ANGKA

def pertambahan(*add) :                         # fungsi untuk menambahkan semua angka
    total =0
    for ad in add :
        total += ad
    return total
    
number = []                                     # list angka dari input
ditambah = True

while ditambah :
    angka = input("Masukkan angka : ")
    
    if angka == "q" :
        ditambah = False
    else :
        menambah = int(angka)
        number.append(menambah)


hasil = pertambahan(*number)                    # * sebelum variabel, artinya memecah list menjadi satuan gitu
print("------------------------------")
print(f"angka yang dijumlahkan : {number}")
print(f" hasil pertambahan = {hasil}")