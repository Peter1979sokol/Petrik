import random


class Bojovnik:
    def __init__(self, meno, zdravie, rozsah_utoku):
        self.meno = meno
        self.zdravie = zdravie
        self.rozsah_utoku = rozsah_utoku

    def zautoc(self, druhy):
        poskodenie = random.randint(self.rozsah_utoku[0], self.rozsah_utoku[1])
        druhy.zdravie -= poskodenie
        print(f"{self.meno} utoci na  {druhy.meno} sposobuje {poskodenie} stratu zivota.")
        if druhy.zdravie <= 0:
            print(f"{druhy.meno} bol porazeny!")
            druhy.zdravie = 0


class Pesiak(Bojovnik):
    def __init__(self, meno):
        super().__init__(meno, 120, (15, 30))


class Lukostrelec(Bojovnik):
    def __init__(self, meno):
        super().__init__(meno, 80, (10, 40))


class Mag(Bojovnik):
    def __init__(self, meno):
        super().__init__(meno, 70, (20, 50))


class Arena:
    def __init__(self):
        self.bojovnici = []

    def pridaj_bojovnika(self, warrior):
        self.bojovnici.append(warrior)

    def bojuj(self):
        if len(self.bojovnici) != 2:
            print("V boji musia byt presne dvaja bojovnici.")
            return

        bojovnik1, bojovnik2 = self.bojovnici
        print(f"Boj zacina medzi {bojovnik1.meno} a {bojovnik2.meno}!")

        while bojovnik1.zdravie > 0 and bojovnik2.zdravie > 0:
            bojovnik1.zautoc(bojovnik2)
            if bojovnik2.zdravie > 0:
                bojovnik2.zautoc(bojovnik1)

            print(f"{bojovnik1.meno} zdravie: {bojovnik1.zdravie}")
            print(f"{bojovnik2.meno} zdravie: {bojovnik2.zdravie}")
            print("")

        print("Boj skoncil!")
        if bojovnik1.zdravie > 0:
            print(f"{bojovnik1.meno} je vitaz!")
        else:
            print(f"{bojovnik2.meno} je vitaz!")


def vyber_typ_bojovnika(meno):
    print("Vyber typ bojovnika", meno)
    print("1. Pesiak")
    print("2. Lukostrelec")
    print("3. Mag")
    vyber = input("zadaj cislo tvojho vyberu: ")
    if vyber == "1":
        return Pesiak(meno)
    elif vyber == "2":
        return Lukostrelec(meno)
    elif vyber == "3":
        return Mag(meno)
    else:
        print("Nespravny vyber, default je pesiak.")
        return Pesiak(meno)


# Výber bojovníkov používateľom
warrior1_name = input("Zadaj meno prveho bojovnika: ")
warrior1 = vyber_typ_bojovnika(warrior1_name)

warrior2_name = input("Zadaj meno druheho bojovnika: ")
warrior2 = vyber_typ_bojovnika(warrior2_name)

# Vytvorenie arény
arena = Arena()

# Pridanie bojovníkov do arény
arena.pridaj_bojovnika(warrior1)
arena.pridaj_bojovnika(warrior2)

# Začatie boja v aréne
arena.bojuj()