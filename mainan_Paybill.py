# PAYBILL 

menu = { 
    "tea"       : 10000,
    "coffee"    : 25000,
    "matcha"    : 25000,
    "milk"      : 15000, 
    "lemon tea" : 8000,
    "chocolate" : 15000,
    "lychee"    : 10000
    }

for key, value in menu.items() :    
    print(f"{key:10} : Rp{value}")                              # {key:10}, ngasi spasi 10 gitu biar rapi

print("___________________________________")

drinks = []
paybill = 0

while True :
    drink = input("Can i have (type q if u done) : ").lower()
    if drink == "q" :                                           # break while
        break
    elif drink in menu :
        drinks.append(drink)                                    # memasukkan input ke drinks list
        paybill = paybill + menu[drink]                         # menghitung harga sesuai dictionary menu
    else :
        print(f"Sorry, we dont have {drink}.")

for cart in drinks :
    print(f"{cart} x1 {menu[cart]}")                            # menampilan drinks satu satu beserta harga sesuai {cart}

print("___________________________________")
print(f"Your total is Rp{paybill}!")

