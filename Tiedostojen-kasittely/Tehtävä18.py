kysymysten_määrä = 0

def lue_kysymys(file):
    kysymys = file.readline().strip()
    if not kysymys:
        return None
    vastaukset = [file.readline().strip() for _ in range(3)]
    oikea_vastaus = file.readline().strip().upper()
    return {'k': kysymys, 'v': vastaukset, 'o': oikea_vastaus}

def esita_kysymys(kysymys_dict, numero):
    global kysymysten_määrä
    kysymysten_määrä = kysymysten_määrä + 1
    print(f"{numero}. {kysymys_dict['k']}")
    for indeksi, kirjain in enumerate('ABC'):
        print(f"{kirjain}) {kysymys_dict['v'][indeksi]}")

def tietovisailu(file):
    oikein_vastatut = 0
    while True:
        kysymys_dict = lue_kysymys(file)
        if kysymys_dict is None:
            break
        esita_kysymys(kysymys_dict, oikein_vastatut + 1)
        vastaus_kirjain = input("Vastauksesi: ").strip().upper()
        if vastaus_kirjain == kysymys_dict['o']:
            print("Oikein!")
            oikein_vastatut += 1
        else:
            print(f"Väärin, oikea vastaus on {kysymys_dict['o']}.")

    print(f"Tuloksesi: {oikein_vastatut} / {kysymysten_määrä}")

with open('tietovisa.txt', 'r') as file:
    print("Nyt seuraa pieni tietokilpailu.")
    tietovisailu(file)
