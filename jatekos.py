# This file belongs to the LevBank project
# For further informations please see the main.py file

# This file contains the player class


class jatekos:
    def __init__(self, penz, nev) -> None:
        self.penz = penz
        self.nev = nev

    def __str__(self) -> str:
        return "Not impleted yet."

    def hozzaadas(self, osszeg) -> str:
        self.penz += osszeg
        return "Sikeres tranzakció"

    def levonas(self, osszeg) -> str:
        if self.penz >= osszeg:
            self.penz -= osszeg
            return "Sikeres tranzakció"
        else:
            return "A tranzakció sikertelen. Nem áll rendelkezésre elegendő egyenleg."

    def startmezo(self) -> str:
        self.penz += 2_000_000
        return "Sikeres tranzakció"