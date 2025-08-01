# 16. PENILAIAN PESERTA DUTA WIBU (wkwkwk)

def penilaian(total_nonton, tahun, bhs_jepang) :
    nilai = ((total_nonton * 0.3) + (tahun * 0.2) + (bhs_jepang * 0.5)) 
    return nilai

# jumlah anime yang ditonton 30%
# berapa lama ngewibu 20%
# skor basjep 50%

def kewibuan(nilai) :
    if nilai >= 85 :
        return "A"
    elif nilai >= 70 :
        return "B"
    elif nilai >= 40 :
        return "C"
    else :
        return "D"
    
name = input("Nama : ")
total_nonton = int(input("Berapa banyak anime yang ditonton : "))
tahun = int(input("Sudah berapa tahun kamu nonton anime? : "))
bhs_jepang = int(input("Skor tes bahasa Jepang : "))

hasil = penilaian(total_nonton, tahun, bhs_jepang)
grade = kewibuan(hasil)

print("---------sewibu apa loe-----------")
print(name)
print(f"Nilai akhir : {hasil}")
print(f"Kelompok : {grade}")
print("---------------------------")