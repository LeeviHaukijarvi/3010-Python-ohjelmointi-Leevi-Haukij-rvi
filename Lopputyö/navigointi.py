from Lopputyö import *
suunta = ''
"""
def voiko_liikkua(suunta):
    if sijainti == 'koti' and suunta == 'ita':
        return hiekkatie
    elif sijainti == 'hiekkatie' and suunta == 'itä':
        return mummola
    elif sijainti == 'hiekkatie' and suunta == 'etelä':
        return maantie
    elif sijainti == 'maantie' and suunta == 'länsi':
        return 'kaatopaikka'
    elif sijainti == 'mummola' and suunta == 'itä':
        return valintatalo
    elif sijainti == 'valintatalo' and suunta == 'etelä':
        return täti
    else:
        print ('Täällä ei voi liikkua tuohon suuntaan.')

def uusi_sijainti(uusi = voiko_liikkua(suunta)):
    if uusi == sijainti:
        print(f'Olet jo täällä ({sijainti})')
    else:
        sijainti = uusi

"""
tarina = False
"""
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

"""
def koti(tarina):
    global paikan_esineet
    paikan_esineet = ['läppäri', 'kynttilä', 'koira', 'haalarimerkki',
                    'aurinkolasit', 'takki', 'pipo', 'puhelin']
    if tarina == True:
        print('Kotona on etupihalla rikkinäinen auto, josta puuttuu akku, istuimet, jousitus ja jarrut.\n'
            'Etsi nämä osat ja korjaa auto.')

def hiekkatie(tarina):
    global paikan_esineet
    paikan_esineet = ['rengas', 'tölkki', 'hiekkaa', 'jäkälää', 'kolikko',
                    'nuuskakiekko', 'roska', 'peura']
    if tarina == True:
        print('Hiekkainen polku, joka kulkee läpi metsien ja niittyjen. Hiekkatie on mutkainen ja seikkailunhaluisille sopiva reitti, joka tarjoaa mahdollisuuden tutkia luonnon monimuotoisuutta ja nauttia ulkoilmasta. Polulla voi kohdata erilaisia eläimiä ja kasveja, ja sen varrella voi löytää mielenkiintoisia kohteita tutkittavaksi.')

def mummola(tarina):
    paikan_esineet = ['kahvi', 'keksi', 'pulla', 'vesi', 'tippaleipä', 'sudoku', 'hevonen', 'faksi']

def valintatalo(tarina):
    paikan_esineet = ['marlboron aski', 'lager', 'lonkero', 'irtokarkkeja', 'saludo',
                    'jauhelihapaketti', 'maito', 'ketsuppi']

def täti(tarina):
    paikan_esineet = ['vanhoja valokuvia', 'korurasia', 'lusikkakokoelma',
                    'ohjauspyörä', 'suklaarasia', 'silmälasikotelo', 'kirjekuori', 'villapaita']

def kirjasto(tarina):
    paikan_esineet = ['kirja', 'tietosanakirja', 'kynä ja muistivihko', 'kirjaston kortti',
                    'moottoriöljy', 'kahvimuki', 'kuulokkeet', 'kirjastonhoitaja']

def kebab_ravintola(tarina):
    paikan_esineet = ['kebab-ateria', 'renkaat', 'salaattikulho', 'ranskalainen',
                    'kebabveitsi', 'limupullo', 'kassakone', 'kastikepullo']

def parturi(tarina):
    paikan_esineet = ['hiusharja', 'partasuti', 'shampoopullo',
                    'partakone', 'hiustenleikkauskone', 'peili', 'pyyhe', 'hiustenkuivaaja', 'istuimet']

def ylöjärven_keskusta(tarina):
    paikan_esineet = ['kauppakeskuslahjakortti', 'jarrut', 'kaupunkikartta',
                    'kävelykengät', 'istuimet', 'avainnauha', 'aurinkovarjo', 'katuliittymäkartta']

def tampereen_keskustori(tarina):
    paikan_esineet = ['tampere-muki', 'torikukkakimppu', 'mansikkalaatikko',
                    'kangaskassi', 'reseptivihko', 'musiikkiesityslippu', 'vanhoja postikortteja', 'piirros', 'pakoputki']

def moottoritie(tarina):
    paikan_esineet = ['muovipussi', 'kuluneet ajovalot', 'rikkinäinen jousi',
                    'pysäköintimaksu lippu', 'vaihteisto', 'kahvimainos', 'talonavain', 'kuponki']

def armeija_alue(tarina):
    paikan_esineet = ['huivi', 'kypärä', 'käsiheittopommi', 'sotilaspassi',
                    'kompassi', 'maastopuku', 'ruokarasia', 'jousitus']

def sotilaskoti(tarina):
    paikan_esineet = ['sotilaskoulutuksen käsikirja', 'sotilaslehti', 'sotilasnauha',
                    'sotilasnimikortti', 'patjoja', 'ruoanlaittovälineitä', 'akku', 'leivänpaahdin']

def maantie(tarina):
    paikan_esineet = ['renkaan pumppu', 'maantien kartta', 'kännykän laturi',
                    'aurinkolasit', 'ilmansuodatin', 'jalkapallo', 'kukkaseppele', 'piknikpeite']

def kaatopaikka(tarina):
    paikan_esineet = ['romuraudan pala', 'vanha kännykkä', 'rikkinäinen leluauto',
                    'tyhjä spraymaalisäiliö', 'jäähdytin', 'romumetallin niput', 'kulunut matkalaukku', 'kierrätyspussi']

def kyläpubi(tarina):
    paikan_esineet = ['kaasutin', 'dartsi-peli', 'pubilasku',
                    'karamellipussi', 'pokerikortit', 'ravintola-annoskuponki', 'karaoke mikki', 'tuoppi']

def kela(tarina):
    paikan_esineet = ['asiakaspalautekysely', 'kelakortti', 'puhelinnumero-opas', 'kalenteri',
                    'postikortti', 'moottorin suodatin', 'leimasin', 'muki']

def ratikka(tarina):
    paikan_esineet = ['sähköjärjestelmä', 'aikataulut', 'ratikkakartta',
                    'istuin', 'hanskat', 'mukiteline', 'infotaulu', 'lippu']

def takamaa(tarina):
    paikan_esineet = ['veitsi', 'lamppu', 'kartta', 'teltta', 'ohjausvaijeri',
                    'kirves', 'kompassi', 'ruokapaketti']

def jarppa_setä(tarina):
    paikan_esineet = ['valokuva-albumi', 'puutarhakirves', 'päiväkirja', 'nahkatakki', 'puskurit',
                    'kalastusreppu', 'kiikarit', 'metsästyskivääri']


Täti: Pieni kodikas mökki metsän keskellä, jossa asuu ystävällinen vanha täti. Mökin ympärillä kohoavat korkeat puut ja talon sisällä on tunnelma kuin suoraan menneiden vuosikymmenten ajalta. Tädin keräämät esineet ja muistot menneisyydestä, kuten vanhat vinyylikokoelmat ja käsintehdyt villasukat, tuovat lämpimiä muistoja menneiltä ajoilta.
Kirjasto: Hiljainen ja rauhallinen tila, joka on täynnä kirjahyllyjä ja lukunurkkauksia. Kirjaston seinillä on vanhoja tauluja ja seinäkello tikittää rauhallisesti. Kirjastossa voi uppoutua vanhojen kirjojen maailmaan ja löytää itsensä seikkailemasta menneisyyden tarinoiden parissa.
Kebab: Värikäs ja vilkas ravintola, jossa tarjoillaan herkullisia kebab-annoksia ja muita välimerellisiä herkkuja. Ravintolan seinillä on eloisia värejä ja kiinnostavia kuvia, ja tunnelma on rento ja mukaansatempaava. Ruokailijat voivat nauttia ruoastaan istuimilla istuen ja seurata kiireistä menoa ympärillään.
Parturi: Tyylikäs parturiliike, jossa asiakkaat voivat rentoutua ja hemmotella itseään. Liikkeen sisällä soi mukaansatempaava musiikki ja seinillä on kiinnostavia kuvia ja julisteita. Parturi hoitaa asiakkaiden hiukset ja parrat taitavasti, luoden samalla rennon ilmapiirin.
Ylöjärven keskusta: Pieni mutta vilkas kaupunkikeskus, jossa kadut ovat täynnä erilaisia liikkeitä ja kahviloita. Ihmiset kulkevat kaduilla iloisesti keskustellen ja nauttien ympäröivästä tunnelmasta. Kahvilat tarjoavat asiakkaille herkullisia välipaloja ja juomia, ja kaupat ovat täynnä kiinnostavia tuotteita.
Tampereen keskustori: Historiallinen tori täynnä erilaisia kojuja ja myyntipisteitä. Torilla vallitsee iloinen puheensorina ja musiikki soi taustalla. Vierailijat voivat tutustua erilaisiin tuotteisiin ja nauttia tunnelmasta.
Moottoritie: Halki maiseman kiemurteleva valtatie, jonka varrella on erilaisia pysähdyspaikkoja ja levähdysalueita. Matkaajat voivat nauttia kauniista maisemista ja pysähtyä lepäämään matkan varrella.
Armeija-alue: Tiukasti vartioidut alueet, joilla harjoitetaan erilaisia sotilaallisia toimintoja. Alueilla on erilaisia rakennuksia ja varusteita, ja sotilaat valvovat tarkasti alueita.
Sotilaskoti: Kodikas ja lämminhenkinen ympäristö, jossa sotilaat voivat levätä ja viettää aikaa yhdessä. Sotilaskodissa on erilaisia tiloja ja palveluita, ja siellä vallitsee rento ja ystävällinen ilmapiiri.
Maantie: Pitkä ja mutkainen tie, joka kulkee läpi erilaisten maisemien. Tienvarsilla on erilaisia pysähdyspaikkoja ja nähtävyyksiä, ja matkaajat voivat nauttia kauniista maisemista.
Kaatopaikka: Laaja alue, jonne kerätään ja käsitellään erilaisia jätteitä. Alueella on erilaisia jäteläjiä ja kasoja, ja siellä vallitsee erilainen tunnelma kuin muualla.

Kyläpubi: Kodikas ja perinteinen paikka, jossa ihmiset kokoontuvat nauttimaan hyvästä seurasta ja virvokkeista. Pienet puupöydät ja tuolit täyttävät tilan, ja seinillä roikkuu vanhoja valokuvia ja muistoesineitä menneiltä ajoilta. Tunnelma on rento ja ystävällinen, ja paikalliset jakavat mielellään tarinoitaan ja kuulumisiaan.
Kela: Virallinen toimipaikka, jossa hoidetaan erilaisia viranomaisasioita ja tukiasioita. Tilat ovat neutraaleja ja käytännöllisiä, ja asiakkaat odottavat kärsivällisesti vuoroaan vanhojen puisten penkkien ääressä. Kela tarjoaa avun tarvitseville ja varmistaa, että kaikilla on mahdollisuus saada tarvitsemaansa tukea ja apua.
Ratikka: Kaupungin joukkoliikenneväline, joka tarjoaa kätevän ja ympäristöystävällisen tavan liikkua kaupungin sisällä. Ratikka on vanhanaikaisesti sisustettu ja siinä on istumapaikkoja matkustajille. Matkustajat voivat nauttia maisemista ikkunoista ja jakaa matkansa muiden kanssa.
Takamaa: Syrjäinen ja luonnonkaunis alue, jossa voi kokea rauhaa ja hiljaisuutta. Takamaalla on laajoja metsiä ja avara taivas, ja siellä voi vaeltaa ja tutkia ympäristöä rauhassa. Alueella vallitsee erityinen tunnelma, joka houkuttelee ihmisiä pysähtymään hetkeksi ja nauttimaan luonnon tarjoamasta kauneudesta.
Jarppa-setä: Karismaattinen vanha mies, joka asuu yksinäisellä maatilalla. Jarppa-setä tunnetaan ympäristössään viisaana ja ystävällisenä hahmona, joka on aina valmis auttamaan muita ja jakamaan tarinoitaan menneiltä vuosikymmeniltä. Hänen maatilallaan vieraileminen on kuin matka menneisyyteen, jossa arvostetaan yksinkertaisia iloja ja elämän viisauksia.
Hiekkatie: Hiekkainen polku, joka kulkee läpi metsien ja niittyjen. Hiekkatie on mutkainen ja seikkailunhaluisille sopiva reitti, joka tarjoaa mahdollisuuden tutkia luonnon monimuotoisuutta ja nauttia ulkoilmasta. Polulla voi kohdata erilaisia eläimiä ja kasveja, ja sen varrella voi löytää mielenkiintoisia kohteita tutkittavaksi.
Mummola: Viehättävä maalaistalo, jossa asuu ystävällinen isoäiti tai isoäiti. Mummolan ympärillä on vehreä puutarha ja kukkivia pensaita, ja talo itsessään on täynnä lämpöä ja rakkautta. Mummolassa vieraileminen on kuin paluu lapsuuden muistoihin ja menneiden kesien tunnelmaan, ja siellä voi rentoutua ja nauttia hyvästä seurasta ja herkullisista herkuista.
Valintatalo: Paikallinen ruokakauppa, jossa pelaaja voi käydä ostoksilla ja löytää tarvitsemiaan tavaroita ja ruokaa matkansa varrelle. Valintatalo tarjoaa laajan valikoiman erilaisia tuotteita ja palveluita, ja siellä voi tavata tuttuja ja vaihtaa kuulumisia. Kaupassa vallitsee tuttu ja turvallinen ilmapiiri, joka houkuttelee asiakkaita palaamaan yhä uudelleen.
