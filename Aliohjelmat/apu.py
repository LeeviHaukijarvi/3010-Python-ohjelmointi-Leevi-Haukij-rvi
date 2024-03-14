def lue_desimaaliluku(kehote, pienin, suurin):

    tulos = 0
    ok = False
    while not ok:
        teksti = input(kehote)
        tulos = float(teksti)


        if tulos >= pienin and tulos <= suurin:
            ok = True
        else:
            print(f'Luvun pitää olla välillä {pienin}-{suurin}. Yritä uudelleen!')
        return tulos