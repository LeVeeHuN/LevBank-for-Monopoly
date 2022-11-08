
import jatekos
import tranzakciok as tr

class savegame:
    def __init__(self, src) -> None:
        # src -> megnyitott mentési fájl
        self._src = src
        
        self._mentesiUtvonal = self._src.name
        self.mentesNeve = self._mentesiUtvonal.strip().split("/")
        for i in range(len(self.mentesNeve) - 1): self.mentesNeve.pop(0)
        self.mentesNeve = str(self.mentesNeve[0]).removesuffix(".levdb").upper()

        # a mentési fájl sorainak beolvasása
        self._adathalmaz = self._src.readlines()

        # az adathalmazban a sorok végén lévő újsor karakter törlése
        for i in range(len(self._adathalmaz)):
            self._adathalmaz[i] = self._adathalmaz[i].strip()

        # játékosok számának beolvasása majd törlése az adathalmazból
        self.numberOfPlayers = int(self._adathalmaz[0])
        self._adathalmaz.pop(0)

        # játékosok lista létrehozása
        self.jatekosok = list()
        # az adathalmazból a játékosok kiválogatása
        # majd játékos objectként eltárolás a játékosok listában
        for _ in range(self.numberOfPlayers):
            self._jatekosAdatai = self._adathalmaz[0].split("||")
            self._jatekosNeve = self._jatekosAdatai[0]
            self._jatekosPenze = int(self._jatekosAdatai[1])

            self.jatekosok.append(jatekos.jatekos(self._jatekosNeve, self._jatekosPenze))
            self._adathalmaz.pop(0)
        
        # tranzakciók feldolgozása
        self.tranzakciok = list()
        for _ in range(len(self._adathalmaz)):
            self._tranzakcioAdatai = self._adathalmaz[0].split("||")
            self._tranzakcioMod = self._tranzakcioAdatai[0]
            self._kitol = self._tranzakcioAdatai[1]
            self._kinek = self._tranzakcioAdatai[2]
            self._osszeg = int(self._tranzakcioAdatai[3])

            self.tranzakciok.append(tr.transaction(self._tranzakcioMod, self._kitol, self._kinek, self._osszeg))
            self._adathalmaz.pop(0)
    

    def printAllTransaction(self) -> None:
        self._str = ""
        for transaction in self.tranzakciok:
            if transaction.mode == "u":
                self._str += f"{transaction.kitol} -> {transaction.osszeg:,} -> {transaction.kinek}\n"
            elif transaction.mode == "h":
                self._str += f"{transaction.kinek} <- + {transaction.osszeg:,}\n"
            elif transaction.mode == "e":
                self._str += f"{transaction.kitol} -> - {transaction.osszeg:,}\n"
        print(self._str)


    def getAllTransaction(self) -> list:
        pass


    def save(self):
        with open(self._mentesiUtvonal) as mentes:
            pass