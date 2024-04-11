def ota_esine(esine):
    if esine in esineet:
        print(f'Sinulla on jo mukana esine: {esine.capitalize()}')
        return
    if esine in paikan_esineet:
        global pisteet
        if len(esineet) >= 5:
            print('Sinulla on jo liikaa esineitä mukana.')
            return
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

# Tämä koodi on otettu suoraan Lopputyö.py-tiedostosta, koska olin tehnyt sen jo valmiiksi ennen tätä tehtävää.
# Lisäsin koodiin tuon max 5 esinettä ominaisuuden.
# Tässä koodissa tarkistetaan onko esine siellä missä pelaajakin on.