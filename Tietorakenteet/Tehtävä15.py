def pelaajan_päivitys(nimi, pistemäärä, esineet): # Funktio, joka päivittää pelaajan tiedot
    pelaaja = {
        "nimi": nimi,
        "pistemäärä": pistemäärä,
        "esineet": esineet
    }
    return pelaaja

nimi = ""
while nimi == "":
    nimi = input("Mikä on nimesi?: ")
    if nimi != "":
        break

nimi = nimi.strip() # Poistaa ylimääräiset välilyönnit
pelaaja = pelaajan_päivitys(nimi, 0, []) # Pelaaja aloittaa pelin 0 pisteellä ja ilman esineitä

print(f'Tervetuloa pelaamaan, {pelaaja["nimi"]}!')


pelaaja = pelaajan_päivitys(nimi, input("Kuinka monta pistettä haluat lisätä?: "), [])

print(f'Kiitos pelistä {pelaaja["nimi"]} {pelaaja["pistemäärä"]}')
