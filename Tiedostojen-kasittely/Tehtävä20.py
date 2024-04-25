import json

with open('Tiedostojen-kasittely/pelaaja.json', 'r') as tiedosto:
    tiedot = json.load(tiedosto)

tiedot['pelaaja'] = 'Matti Meikalainen'
tiedot['pisteet'] = 10
tiedot['esineet'] = ['piano', 'rumpu', 'kukka']


json.dump(tiedot, open('Tiedostojen-kasittely/pelaaja.json', 'w'))

"""
Ohjelma lukee .json tiedoston kirjoittaa sen "tiedot" muuttujalle, muokkaa sitä ja kirjoittaa sen takaisin tiedostoon.
Yhdelle riville.
"""