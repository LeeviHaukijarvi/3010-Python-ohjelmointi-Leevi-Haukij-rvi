sanat = []
käyttäjän_sana = '1'
yhteispituus = 0
lyhyin_sana = ''
pisin_sana = ''
lyhyin_sana_pituus = 10000
pisin_sana_pituus = 0

while käyttäjän_sana != '':
    käyttäjän_sana = input()
    if len(käyttäjän_sana) == 1 or len(käyttäjän_sana) == 0:
        continue
    else:
        sanat.append(käyttäjän_sana)

for i in sanat:
    if len(i) > pisin_sana_pituus:
        pisin_sana_pituus = len(i)
        pisin_sana = f'Pisin sana: {i}, {len(i)} merkkiä'
    if len(i) < lyhyin_sana_pituus:
        lyhyin_sana_pituus = len(i)
        lyhyin_sana = f'Lyhin sana: {i}, {len(i)} merkkiä'
    yhteispituus += len(i)

sanat.sort()
print(sanat)
print(lyhyin_sana)
print(pisin_sana)
print(f'Kaikkien sanojen yhteispituus: {yhteispituus} merkkiä')

"""
Minun toteutuksessani saman pituisista sanoista se, joka ensin syötetään se tulostetaan.
Tilannetta voisi parantaa lisäämällä ehto, joka tekee uuden listan missä saman pituiset sanat ovat
ja ne tulostettaisiin erikseen käyttäjälle.
"""