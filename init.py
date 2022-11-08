# This file belongs to the LevBank project
# For further informations please see the main.py file

# This file contains the initialization of the program

import jatekos
from cls import cls
from os import scandir

STATUS = "DEV"
VERSION = "0.0.2"
BANNER = "---------------------------------------\nLevBank Financial Software for Monopoly\n"

# Prints the welcome message
cls()
print(BANNER, STATUS, VERSION, "\n")


# Mentési fájlok beolvasása
fajlok = scandir("./saves")
mentesek = [mentes.name for mentes in fajlok if mentes.is_file() and mentes.name.endswith(".levdb")]


print("0 - Új mentés létrehozása")
for i in range(len(mentesek)):
    print(i+1, mentesek[i])

userChoice = int(input("Válasz: ")) - 1

print()
if userChoice == -1:
    with open("kezdotoke.levdb", "r", encoding="utf-8") as f: kezdotokek = [sor.strip().split("||") for sor in f]

    for i in range(len(kezdotokek)):
        print(i+1, kezdotokek[i][0], kezdotokek[i][1])

    userChoice = int(input("Válasz: ")) - 1
    kezdotoke = kezdotokek[userChoice][1]