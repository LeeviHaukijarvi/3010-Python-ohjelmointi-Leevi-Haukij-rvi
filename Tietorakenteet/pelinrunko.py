esineet = ['kivi', 'tikku', 'kukka']

def tulosta_inventaario(esineet):
    if esineet == None:
        print ('Sinulla ei ole mukana mitään.')
    else :
        print('Sinulla on mukana:')
        for i in esineet:
            print('- ' + i.capitalize())

def alkutekstit():
    """
    Tulostetaan pelaajalle ohjeita tai
    rakennetaan tunnelmaa.
    """
    print('\nOlet synkän metsän laidalla.')
    print('Edessäsi on polku, joka vie syvemmälle metsään.')
    print('Mitä haluat tehdä?\n')

def lopputekstit():
    """Tulostetaan nämä rivit pelin loppuessa."""
    print('Kiitos pelistä! Nähdään taas!\n')

def lue_komento():
    """
    Luetaan pelaajalta komento, muunnetaan pieniksi
    kirjaimiksi ja palautetaan osat pilkottuna
    välilyöntien kohdilta.
    """
    k = input('> ').lower().strip()
    return k.split()

def onko_lopetus(komento):
    """
    Palautetaan True jos komento oli yksiosainen
    ja ainoa osa oli 'lopeta', muutoin False.
    """
    if len(komento) == 1 and komento[0] == 'lopeta':
        return True
    else:
        return False

def peli():
    """
    Pelin pääsilmukka. Toistetaan kunnes pelaaja
    haluaa lopettaa pelin.
    """
    while True:
        komento = lue_komento()
        if onko_lopetus(komento):
            break
        pituus = len(komento)
        if pituus == 0:
            continue
        elif pituus == 1:
            verbi = komento[0]
            print(f'Yksiosainen komento: "{verbi}"')
            if verbi == 'katsele':
                print('OK, katsellaan ympäriinsä')
            elif verbi == 'mukana':
                tulosta_inventaario(esineet)

            else:
                print(f'En tunnista komentoa: {verbi}')
        elif pituus == 2:
            verbi = komento[0]
            objekti = komento[1]
            print(f'Kaksiosainen komento: "{verbi} {objekti}"')
        else:
            print(f'Komento, jossa on {pituus} osaa:')
            for osa in komento:
                print(osa)

if __name__ == '__main__':
    alkutekstit()
    peli()
    lopputekstit()
