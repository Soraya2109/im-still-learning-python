# PYTHON QUIZ GAME

print("Rule : Type T for True and F for False")

quiz = ("Altocumulus is middle clouds.",
        "Mimosa is a star within Centaury Constellation.",
        "Kerak samudera lebih tebal dari kerak benua.",
        "Nekton adalah jenis hewan yang bergerak bebas di dalam laut.",
        "Intan adalah mineral dengan skala mohs 1.")


answers = (("True", "False"),
          ("True", "False"),
          ("True", "False"),
          ("True", "False"),
          ("True", "False"))

correct = ("T", "T", "F", "T", "F").upper()

number = 0
score = 0

for quest in quiz :
    print(" ")
    print(quest)                                    # menampilkan quiz satu persatu
    for answer in answers[number] :                 # menampilkan jawaban sesuai index
        print(answer)

    what = input("T/F : ")

    if what == correct[number] :
        print("Correct!")
        score += 20

    else :
        print("Incorrect.")
        score += 0

    number += 1                                     # index otomatis nambah setiap iterasi (menampilkan jawaban nomor berikutnya)

print(f"Finally! Your score is {score}")