peli = True
käyttäjän_vastaus = ""

print('Tervetuloa pelaamaan! Lopeta peli kirjoittamalla "lopeta".')
while peli:

    käyttäjän_vastaus = input('Anna komento: ')

    vastaus_paranneltu = str.strip(käyttäjän_vastaus)
    pilkottu_vastaus = vastaus_paranneltu.split()

    osien_määrä = len(pilkottu_vastaus)

    if osien_määrä != 0:
        verbi = pilkottu_vastaus[0]
    if osien_määrä == 2:
        objekti = pilkottu_vastaus[1]

    if osien_määrä == 1:
        if verbi == "lopeta":
            print('Kiitos pelistä! Nähdään taas!')
            peli = False
        elif verbi == "katso":
            print('Täällä ei ole mitään erityistä nähtävää.')
        elif verbi == "mukana":
            print('Sinulla ei ole mukana mitään.')

    if osien_määrä == 2:
        if verbi == "ota":
            print(f'{objekti.capitalize()} otettu.')
        elif verbi == "pudota":
            print(f'{objekti.capitalize()} pudotettu.')

