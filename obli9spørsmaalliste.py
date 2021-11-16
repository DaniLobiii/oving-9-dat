# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:01:20 2021

@author: lobit
"""

class Sporsmal:
    def __init__(self, sporsmaltekst, svaralternativer, riktigsvar):
        self.sporsmaltekst = sporsmaltekst
        self.svaralternativer = svaralternativer
        self.riktigsvar = int(riktigsvar)

    def __str__(self):
        svarliste = ""
        for i in range(len(self.svaralternativer)):
            svarliste += f"\n\t{self.svaralternativer[i]}"
        resultat = f"{self.sporsmaltekst}{svarliste}"
        return resultat

        pass

    def sjekk_svar(self, svar: int):
        if self.riktigsvar == svar:
            return 1

    def korrekt_svar_tekst(self):
        korrekt_svar = self.svaralternativer[self.riktigsvar]
        return korrekt_svar

if __name__ == "__main__":
    score_player1 = 0
    score_player2 = 0


    sporsmalliste = list()
    with open("C:/Users/lobit/Desktop/9m/sporsmaalsfil.txt", "r", encoding="UTF8") as file:
        for sporsmal in file:
            sporsmal.strip()

            sporsmalslutt = int(sporsmal.find(":"))
            sporsmaltekst = sporsmal[0:sporsmalslutt]
            sporsmalriktig = sporsmal[sporsmalslutt+2:sporsmalslutt+3]

            svaralternativer = list(
                sporsmal[int(sporsmal.find("[")+1):int(sporsmal.find("]"))].split(", "))

            sporsmalliste.append(Sporsmal(sporsmaltekst, svaralternativer, sporsmalriktig))

        for i in range(len(sporsmalliste)):
            sporsmal = sporsmalliste[i]
            svaralternativer = sporsmal.svaralternativer
            korrekt_svar = sporsmal.korrekt_svar_tekst()

            print(sporsmal.sporsmaltekst)

            for j in range(len(svaralternativer)):
                print(str(j) + ": " + str(svaralternativer[j]))
            svar1 = int(input("Velg et svaralternativ for spiller 1: "))
            svar2 = int(input("Velg et svaralternativ for spiller 2: "))

            if sporsmal.sjekk_svar(svar1) == 1:
                print('Riktig! Korrekt svar er: ' + korrekt_svar)
                score_player1 += 1
            else:
                print('Feil! Korrekt svar er: ' + korrekt_svar)
            if sporsmal.sjekk_svar(svar2) == 1:
                print('Riktig! Korrekt svar er: ' + korrekt_svar)
                score_player2 += 1
            else:
                print('Feil! Korrekt svar er: ' + korrekt_svar)

    print("Spiller 1: " + str(score_player1))
    print("Spiller 2: " + str(score_player2))
