from navigointi import *
suunta = ''
sijainti = 'koti'
esineet = []
paikan_esineet = []
pisteet = 0



def koti(tarina):
    global paikan_esineet
    paikan_esineet = ['läppäri', 'kynttilä', 'koira', 'haalarimerkki',
                    'aurinkolasit', 'takki', 'pipo', 'puhelin']
    if tarina == True:
        print('Kodikas ja turvallinen paikka, Koti voi sisältää erilaisia huoneita, kuten olohuoneen, keittiön ja makuuhuoneen.')

def hiekkatie(tarina):
    global paikan_esineet
    paikan_esineet = ['rengas', 'tölkki', 'hiekkaa', 'jäkälää', 'kolikko',
                    'nuuskakiekko', 'roska', 'peura']
    if tarina == True:
        print('paskanaama')



def sijainti_päivitys(tarina):
    if sijainti == 'koti':
        return koti(tarina)
    elif sijainti == 'hiekkatie':
        return hiekkatie(tarina)
    elif sijainti == 'mummola':
        return mummola(tarina)
    elif sijainti == 'valintatalo':
        return valintatalo(tarina)
    elif sijainti == 'täti':
        return täti(tarina)
    elif sijainti == 'kirjasto':
        return kirjasto(tarina)
    elif sijainti == 'kebab_ravintola':
        return kebab_ravintola(tarina)
    elif sijainti == 'parturi':
        return parturi(tarina)
    elif sijainti == 'ylöjärven_keskusta':
        return ylöjärven_keskusta(tarina)
    elif sijainti == 'tampereen_keskustori':
        return tampereen_keskustori(tarina)
    elif sijainti == 'moottoritie':
        return moottoritie(tarina)
    elif sijainti == 'armeija_alue':
        return armeija_alue(tarina)
    elif sijainti == 'sotilaskoti':
        return sotilaskoti(tarina)
    elif sijainti == 'maantie':
        return maantie(tarina)
    elif sijainti == 'kaatopaikka':
        return kaatopaikka(tarina)
    elif sijainti == 'kyläpubi':
        return kyläpubi(tarina)
    elif sijainti == 'kela':
        return kela(tarina)
    elif sijainti == 'ratikka':
        return ratikka(tarina)
    elif sijainti == 'takamaa':
        return takamaa(tarina)


def voiko_liikkua(suunta):
    if sijainti == 'koti' and suunta == 'itä':
        return 'hiekkatie'
    elif sijainti == 'hiekkatie' and suunta == 'itä':
        return 'mummola'
    elif sijainti == 'hiekkatie' and suunta == 'etelä':
        return 'maantie'
    elif sijainti == 'hiekkatie' and suunta == 'länsi':
        return 'koti'

    elif sijainti == 'maantie' and suunta == 'länsi':
        return 'kaatopaikka'
    elif sijainti == 'maantie' and suunta == 'itä':
        return 'kyläpubi'
    elif sijainti == 'maantie' and suunta == 'pohjoinen':
        return 'hiekkatie'
    elif sijainti == 'maantie' and suunta == 'etelä':
        return 'moottoritie'


    elif sijainti == 'moottoritie' and suunta == 'pohjoinen':
        return 'maantie'
    elif sijainti == 'moottoritie' and suunta == 'itä':
        return 'armeija_alue'
    elif sijainti == 'moottoritie' and suunta == 'etelä':
        return 'tampereen_keskustori'


    elif sijainti == 'armeija_alue' and suunta == 'länsi':
        return 'sotilaskoti'
    elif sijainti == 'armeija_alue' and suunta == 'itä':
        return 'moottoritie'

    elif sijainti == 'sotilaskoti' and suunta == 'länsi':
        return 'armeija_alue'

    elif sijainti == 'tampereen_keskustori' and suunta == 'pohjoinen':
        return 'moottoritie'
    elif sijainti == 'tampereen_keskustori' and suunta == 'länsi':
        return 'ratikka'
    elif sijainti == 'tampereen_keskustori' and suunta == 'itä':
        return 'ylöjärven_keskusta'

    elif sijainti == 'ratikka' and suunta == 'itä':
        return 'tampereen_keskustori'
    elif sijainti == 'ratikka' and suunta == 'pohjoinen':
        return 'kela'

    elif sijainti == 'kela' and suunta == 'etelä':
        return 'ratikka'

    elif sijainti == 'ylöjärven_keskusta' and suunta == 'länsi':
        return 'tampereen_keskustori'
    elif sijainti == 'ylöjärven_keskusta' and suunta == 'itä':
        return 'kebab_ravintola'
    elif sijainti == 'ylöjärven_keskusta' and suunta == 'pohjoinen':
        return 'takamaa'

    elif sijainti == 'takamaa' and suunta == 'etelä':
        return 'ylöjärven_keskusta'
    elif sijainti == 'takamaa' and suunta == 'pohjoinen':
        return 'jarppa_setä'

    elif sijainti == 'jarppa_setä' and suunta == 'etelä':
        return 'takamaa'

    elif sijainti == 'kebab_ravintola' and suunta == 'länsi':
        return 'ylöjärven_keskusta'
    elif sijainti == 'kebab_ravintola' and suunta == 'itä':
        return 'parturi'
    elif sijainti == 'kebab_ravintola' and suunta == 'pohjoinen':
        return 'kirjasto'

    elif sijainti == 'parturi' and suunta == 'länsi':
        return 'kebab_ravintola'

    elif sijainti == 'kirjasto' and suunta == 'etelä':
        return 'kebab_ravintola'
    elif sijainti == 'kirjasto' and suunta == 'pohjoinen':
        return 'täti'

    elif sijainti == 'täti' and suunta == 'etelä':
        return 'kirjasto'
    elif sijainti == 'täti' and suunta == 'pohjoinen':
        return 'valintatalo'

    elif sijainti == 'valintatalo' and suunta == 'etelä':
        return 'täti'
    elif sijainti == 'valintatalo' and suunta == 'länsi':
        return 'mummola'

    elif sijainti == 'mummola' and suunta == 'länsi':
        return 'hiekkatie'
    elif sijainti == 'mummola' and suunta == 'itä':
        return 'valintatalo'

    else:
        print ('Täällä ei voi liikkua tuohon suuntaan.')

def uusi_sijainti(suunta):
    global sijainti
    sijainti = voiko_liikkua(suunta)


def missa_pelaaja():
    print(f'Olet nyt {sijainti}.')


def ota_esine(esine):
    if esine in paikan_esineet:
        global pisteet
        esineet.append(esine)
        paikan_esineet.remove(esine)
        print(f'Otit esineen: {esine.capitalize()}')
        if esine in ['ohjausvaijeri', 'sähköjärjestelmä', 'moottorin suodatin', 'kaasutin',
                    'ilmansuodatin', 'akku', 'jousitus', 'vaihteisto',
                    'pakoputki', 'istuimet', 'renkaat', 'moottoriöljy', 'ohjauspyörä', 'puskurit']:
            pisteet += 1
            print(f'Keräsit osan autosta: {esine.capitalize()}')
        else:
            pisteet -= 1
    else:
        print(f'Esine {esine.capitalize()} ei ole täällä.')

def pudota_esine(esine):
    if esine in esineet:
        esineet.remove(esine)
        paikan_esineet.append(esine)
        print(f'Pudotit esineen: {esine.capitalize()}')
    else:
        print(f'Sinulla ei ole mukana esinettä: {esine.capitalize()}')

def tulosta_inventaario(esineet):
    if not esineet:
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
                sijainti_päivitys(True)
            elif verbi == 'mukana':
                tulosta_inventaario(esineet)
            elif verbi == 'missä':
                missa_pelaaja()
            elif verbi == 'esineet':
                print(paikan_esineet)
            elif verbi == 'pisteet':
                print(pisteet)
            else:
                print(f'En tunnista komentoa: {verbi}')
        elif pituus == 2:
            verbi = komento[0]
            objekti = komento[1]
            print(f'Kaksiosainen komento: "{verbi} {objekti}"')
            if verbi == 'ota':
                ota_esine(objekti)
            elif verbi == 'pudota':
                pudota_esine(objekti)
            elif verbi == 'mene':
                uusi_sijainti(objekti)
                sijainti_päivitys(False)
            else:
                print(f'En tunnista komentoa: {verbi}')
        else:
            print(f'Komento, jossa on {pituus} osaa:')
            for osa in komento:
                print(osa)

if __name__ == '__main__':
    alkutekstit()
    peli()
    lopputekstit()
