import random


suunta = ''
sijainti = 'koti'
esineet = []
paikan_esineet = []

auton_osat = ['ohjausvaijeri', 'sähköjärjestelmä', 'moottorinsuodatin', 'kaasutin',
                    'ilmansuodatin', 'akku', 'jousitus', 'vaihteisto',
                    'pakoputki', 'istuimet', 'renkaat', 'moottoriöljy', 'ohjauspyörä', 'puskurit', 'jarrut']

paikat = {
    "koti": {
        "esineet": ['läppäri', 'kynttilä', 'koira', 'haalarimerkki','aurinkolasit', 'takki', 'pipo', 'puhelin'],
        "tarina": 'Kotona on etupihalla rikkinäinen auto, josta puuttuu osia.'
    },
    "auto": {
        "esineet": [],
        "tarina": 'Rikkinäinen auto odottaa korjausta. Etsi osat ja korjaa auto.'
    },
    "mummola": {
        "esineet": ['kahvi', 'keksi', 'pulla', 'vesi', 'tippaleipä', 'sudoku', 'hevonen', 'faksi'],
        "tarina": 'Mummolassa voit nauttia herkullisista leivonnaisista ja viettää aikaa rakkaiden muistojen parissa.'
    },
    "valintatalo": {
        "esineet": ['mallu', 'lager', 'lonkero', 'irtokarkkeja', 'saludo', 'jauhelihapaketti', 'maito', 'ketsuppi'],
        "tarina": 'Valintatalossa voit tehdä ostoksia ja löytää tarvitsemiasi tuotteita matkasi varrelle.'
    },
    "täti": {
        "esineet": ['vanhoja valokuvia', 'korurasia', 'lusikkakokoelma', 'ohjauspyörä', 'suklaarasia', 'silmälasikotelo', 'kirjekuori', 'villapaita'],
        "tarina": 'Tädin luona voit tutustua menneisyyden esineisiin ja kuulla jännittäviä tarinoita.'
    },
    "kirjasto": {
        "esineet": ['kirja', 'tietosanakirja', 'kynä ja muistivihko', 'kirjaston kortti', 'moottoriöljy', 'kahvimuki', 'kuulokkeet', 'kirjastonhoitaja'],
        "tarina": 'Kirjastossa voit uppoutua kirjojen maailmaan ja löytää mielenkiintoista luettavaa.'
    },
    "kebab_ravintola": {
        "esineet": ['kebab-ateria', 'renkaat', 'salaattikulho', 'ranskalainen', 'kebabveitsi', 'limupullo', 'kassakone', 'kastikepullo'],
        "tarina": 'Kebab-ravintolassa voit nauttia herkullisista välimerellisistä ruoista ja rentoutua.'
    },
    "parturi": {
        "esineet": ['hiusharja', 'partasuti', 'shampoopullo', 'partakone', 'hiustenleikkauskone', 'peili', 'pyyhe', 'hiustenkuivaaja', 'istuimet'],
        "tarina": 'Parturissa voit hemmotella itseäsi ja saada tyylikkään hiustyylin tai parran.'
    },
    "ylöjärven_keskusta": {
        "esineet": ['kauppakeskuslahjakortti', 'jarrut', 'kaupunkikartta', 'kävelykengät', 'istuimet', 'avainnauha', 'aurinkovarjo', 'katuliittymäkartta'],
        "tarina": 'Ylöjärven keskustassa voit tutustua erilaisiin liikkeisiin ja nauttia vilkkaasta tunnelmasta.'
    },
    "tampereen_keskustori": {
        "esineet": ['tampere-muki', 'torikukkakimppu', 'mansikkalaatikko', 'kangaskassi', 'reseptivihko', 'musiikkiesityslippu', 'vanhoja postikortteja', 'piirros', 'pakoputki'],
        "tarina": 'Tampereen keskustorilla voit tutustua erilaisiin kojuhin ja nauttia historiallisesta tunnelmasta.'
    },
    "moottoritie": {
        "esineet": ['muovipussi', 'kuluneet ajovalot', 'rikkinäinen jousi', 'pysäköintimaksu lippu', 'vaihteisto', 'kahvimainos', 'talonavain', 'kuponki'],
        "tarina": 'Moottoritiellä voit nauttia kauniista maisemista ja pysähtyä levähdysalueilla.'
    },
    "armeija_alue": {
        "esineet": ['huivi', 'kypärä', 'käsiheittopommi', 'sotilaspassi', 'kompassi', 'maastopuku', 'ruokarasia', 'jousitus'],
        "tarina": 'Armeija-alueella voit tutustua sotilaallisiin toimintoihin ja nähdä erilaisia rakennuksia ja varusteita.'
    },
    "sotilaskoti": {
        "esineet": ['sotilaskoulutuksen käsikirja', 'sotilaslehti', 'sotilasnauha', 'sotilasnimikortti', 'patjoja', 'ruoanlaittovälineitä', 'akku', 'leivänpaahdin'],
        "tarina": 'Sotilaskodissa voit levätä ja viettää aikaa yhdessä muiden sotilaiden kanssa.'
    },
    "maantie": {
        "esineet": ['renkaanpumppu', 'maantienkartta', 'kännykänlaturi', 'aurinkolasit', 'ilmansuodatin', 'jalkapallo', 'kukkaseppele', 'piknikpeite'],
        "tarina": 'Maantiellä voit nauttia kauniista maisemista ja tutkia erilaisia pysähdyspaikkoja.'
    },
    "kaatopaikka": {
        "esineet": ['romuraudanpala', 'vanha kännykkä', 'rikkinäinenleluauto', 'tyhjä spraymaalisäiliö', 'jäähdytin', 'rotta', 'kulunut matkalaukku', 'kierrätyspussi'],
        "tarina": 'Kaatopaikalla voit tutkia erilaisia jäteläjiä ja kasoja, mutta varo hajuja!'
    },
    "kyläpubi": {
        "esineet": ['kaasutin', 'dartsi-peli', 'pubilasku', 'karamellipussi', 'pokerikortit', 'ravintola-annoskuponki', 'karaoke mikki', 'tuoppi'],
        "tarina": 'Kyläpubissa voit nauttia kodikkaasta tunnelmasta ja hyvästä seurasta.'
    },
    "kela": {
        "esineet": ['asiakaspalautekysely', 'kelakortti', 'puhelinnumero-opas', 'kalenteri', 'postikortti', 'moottorinsuodatin', 'leimasin', 'muki'],
        "tarina": 'Kelassa voit hoitaa viranomaisasioita ja saada tarvitsemaasi tukea ja apua.'
    },
    "ratikka": {
        "esineet": ['sähköjärjestelmä', 'aikataulut', 'ratikkakartta', 'istuin', 'hanskat', 'mukiteline', 'infotaulu', 'lippu'],
        "tarina": 'Ratikassa voit matkustaa kätevästi kaupungin sisällä ja nauttia maisemista.'
    },
    "takamaa": {
        "esineet": ['veitsi', 'lamppu', 'kartta', 'teltta', 'ohjausvaijeri', 'kirves', 'kompassi', 'ruokapaketti'],
        "tarina": 'Takamaalla voit kokea rauhaa ja hiljaisuutta sekä tutkia luonnon kauneutta.'
    },
    "jarppa_setä": {
        "esineet": ['valokuva-albumi', 'puutarhakirves', 'päiväkirja', 'nahkatakki', 'puskurit', 'kalastusreppu', 'kiikarit', 'metsästyskivääri'],
        "tarina": 'Jarppa-setä on karismaattinen hahmo, joka asuu yksinäisellä maatilalla ja jakaa viisauksiaan.'
    }
}

def sijainti_päivitys():
    if sijainti == 'jarppa_setä':
        print('\nJarppa-setä: "Hei, jotta voit korjata autosi sinun pitää löytää ainakin 5 osaa autosta.\n'
            'kun sinulla on osat palaa autollesi ja pudota ne!\nVihje: komento "korjaa auto" on hyödyksi\n ')

    return paikat[sijainti]

def voiko_liikkua(suunta):
    if sijainti == 'koti' and suunta == 'itä':
        return 'auto'
    elif sijainti == 'auto' and suunta == 'itä':
        return 'mummola'
    elif sijainti == 'auto' and suunta == 'etelä':
        return 'maantie'
    elif sijainti == 'auto' and suunta == 'länsi':
        return 'koti'

    elif sijainti == 'maantie' and suunta == 'länsi':
        return 'kaatopaikka'
    elif sijainti == 'maantie' and suunta == 'itä':
        return 'kyläpubi'
    elif sijainti == 'kyläpubi' and suunta == 'länsi':
        return 'maantie'
    elif sijainti == 'maantie' and suunta == 'pohjoinen':
        return 'auto'
    elif sijainti == 'maantie' and suunta == 'etelä':
        return 'moottoritie'


    elif sijainti == 'moottoritie' and suunta == 'pohjoinen':
        return 'maantie'
    elif sijainti == 'moottoritie' and suunta == 'itä':
        return 'armeija_alue'
    elif sijainti == 'moottoritie' and suunta == 'etelä':
        return 'tampereen_keskustori'
    elif sijainti == 'moottoritie' and suunta == 'länsi':
        return 'armeija_alue'


    elif sijainti == 'armeija_alue' and suunta == 'länsi':
        return 'sotilaskoti'
    elif sijainti == 'armeija_alue' and suunta == 'itä':
        return 'moottoritie'

    elif sijainti == 'sotilaskoti' and suunta == 'itä':
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
        return 'auto'
    elif sijainti == 'mummola' and suunta == 'itä':
        return 'valintatalo'

    else:
        print ('Täällä ei voi liikkua tuohon suuntaan.')
        return sijainti

def uusi_sijainti(suunta):
    global sijainti
    sijainti = voiko_liikkua(suunta)

def erikoiskomennot(verbi, objekti):
    global sijainti
    if verbi == "polta" and objekti == "mallu" and 'mallu' in esineet:
            print('Aloitat mallun polttamisen, tämä on eka kertasi ja saat yskänkohtauksen.\nSaat nikotiinimyrkytyksen ja kuolet. Peli päättyy.')
            exit()
    elif verbi == "polta" and objekti == "mallu" and 'mallu' not in esineet:
                print('Sinulla ei ole mukana mallua.')

    if verbi == "silitä" and objekti == "koira" and'koira' in esineet:
        print('Silität koiraa ja se nuolee sinua kiitokseksi.')
    elif verbi == "silitä" and objekti == "koira" and 'koira' not in esineet:
            print('Sinulla ei ole mukana koiraa.')

    if verbi == "juo" and objekti == "lager" and 'lager' in esineet:
        print('Juot oluen, etkä voi enää hallita itseäsi, juot itsesi humalaan.')
        for i in range(5):
            input('> ')
            print(random.choice(['Nyt on hauskaa!', 'Oletko nähnyt mun olutta?', 'Missä mä olen?', 'Mikä on sun nimi?', 'MOROO!']))
        sijainti  = 'kyläpubi'
        print('Heräät kyläpubin vessasta ja huomaat olevasi pahassa krapulassa.')
    elif verbi == "juo" and objekti == "lager" and 'lager' not in esineet:
            print('Sinulla ei ole mukana lageria')

    if verbi == "korjaa" and objekti == "auto" and sijainti == 'auto':
        if len([osa for osa in auton_osat if osa in paikat['auto']['esineet']]) >= 8:
            print('\nSait autosi rekisteröityä ja se on nyt valmis liikenteeseen.')
            lopputekstit()
        elif len([osa for osa in auton_osat if osa in paikat['auto']['esineet']]) == 5:
            print('\nKorjasit auton, mutta sitä ei voi vielä rekisteröidä liikenteeseen.')
            print('Etsi vielä ainakin kolme osaa niin saat autosi rekisteröityä.')
        else:
            print('Sinulla ei ole tarpeeksi osia autossa.')

    if verbi == "harjaa" and objekti == "hiukset" and esineet == 'hiusharja':
        print('Harjaat hiuksesi ja ne näyttävät nyt siistimmiltä.')
    elif verbi == "harjaa" and objekti == "hiukset" and esineet != 'hiusharja':
        print('Sinulla ei ole harjaa.')

    if verbi == "täytä" and objekti == "lomake" and esineet == 'asiakaspalautekysely':
        print('Täytät lomakkeen ja annat palautetta Kelan toiminnasta.')
    elif verbi == "täytä" and objekti == "lomake" and esineet !='asiakaspalautekysely':
        print('Sinulla ei ole lomaketta.')

def missa_pelaaja():
    print(f'Olet paikassa: {sijainti.capitalize()}')

def ota_esine(esine):
    if esine in esineet:
        print(f'Sinulla on jo mukana esine: {esine.capitalize()}')
        return
    if esine in paikat[sijainti]['esineet']:
        global pisteet
        if len(esineet) >= 5:
            print('Sinulla on jo liikaa esineitä mukana.')
            return
        esineet.append(esine)
        paikat[sijainti]['esineet'].remove(esine)
        print(f'Otit esineen: {esine.capitalize()}')
    else:
        print(f'Esine {esine.capitalize()} ei ole täällä.')

def pudota_esine(esine):
    if esine in esineet:
        esineet.remove(esine)
        paikat[sijainti]['esineet'].append(esine)
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
    print('\nOlet kotonasi, joku soittaa\n')
    print('Vastaat\n')
    print('Se on Jarppa-setä, hän oli kuullut että olit aikeissa korjata pihalla olevan autonne.\n')
    print('Jarppa-setä: "Hei, kuulehan, olen kuullut että olet korjaamassa autoasi. Tule käymään niin neuvon kuinka se tehdään"\n')
    print('Matkasi alkaa, lähde Jarppa-sedän luo ja saat lisäohjeita.\n')
    print('Jos tarvitset apua koita komentoja: "vihje, komennot"\n')

def lopputekstit():
    print('\nLähdet iloisena ajelemaan auringonlaskuun!\nKiitos pelaamisesta!')
    exit()

def lue_komento():
    """
    Luetaan pelaajalta komento, muunnetaan pieniksi
    kirjaimiksi ja palautetaan osat pilkottuna
    välilyöntien kohdilta.
    """
    k = input('> ').lower().strip()
    k = k.split(' ', 1)
    return k

def onko_lopetus(komento):
    if len(komento) == 1 and komento[0] == 'lopeta':
        print("Peli keskeytetään.")
        exit()
    else:
        return False

def peli():

    sijainti_päivitys()
    while True:
        komento = lue_komento()
        if onko_lopetus(komento):
            break
        pituus = len(komento)
        if pituus == 0:
            continue
        elif pituus == 1:
            verbi = komento[0]
            if verbi == 'katsele':
                print(paikat[sijainti]['tarina'])
            elif verbi == 'mukana':
                tulosta_inventaario(esineet)
            elif verbi == 'missä':
                missa_pelaaja()
            elif verbi == 'esineet':
                if paikat[sijainti]['esineet'] == []:
                    print('Täällä ei ole vielä mitään.')
                else:
                    print('')
                    print(', '.join([esine.capitalize() for esine in paikat[sijainti]['esineet']]))
                    print('')
            elif verbi == 'vihje':
                print('\nLager, Mallu, Hiusharja, Lomake ja Koira, nämä esineet voivat tuoda yllätyksiä.')
            elif verbi == 'komennot':
                print('\nKomennot: katsele, mukana, missä, esineet, vihje, ota + (esine), pudota + (esine), mene + (ilmansuunta), lopeta')
            else:
                print(f'En tunnista komentoa: {verbi}')
        elif pituus == 2:
            verbi = komento[0]
            objekti = komento[1]
            if verbi == 'ota':
                ota_esine(objekti)
            elif verbi == 'pudota':
                pudota_esine(objekti)
            elif verbi == 'mene':
                uusi_sijainti(objekti)
                sijainti_päivitys()
            elif verbi == 'polta' or verbi == 'silitä' or verbi == 'juo' or verbi == 'korjaa' or verbi == 'harjaa' or verbi == 'täytä':
                erikoiskomennot(verbi, objekti)
            else:
                print(f'En tunnista komentoa: {verbi}')
        else:
            print(f'Komentoa ei ole')

if __name__ == '__main__':
    alkutekstit()
    peli()
    lopputekstit()
