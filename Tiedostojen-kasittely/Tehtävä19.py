syöte = ''
with open('Tiedostojen-kasittely/rivit.txt', 'a') as tiedosto:
    while True:
        syöte = input('Kirjoita rivi: ')
        if syöte == 'lopeta':
            break
        tiedosto.write(syöte + '\n')

"""
Tämä luo tiedoston ja tallentaa sinne käyttäjän rivit, ymmärtääkseni, kun with agrumentista poistutaan, sulkeutuu samalla tiedosto.
"""