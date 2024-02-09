käyttäjän_vastaus = input('Anna komento: ')
pilkottu_vastaus = käyttäjän_vastaus.split()
osien_määrä = len(pilkottu_vastaus)

if osien_määrä == 2:
    objekti = pilkottu_vastaus[1]

verbi = pilkottu_vastaus[0]

if osien_määrä == 1 and not verbi == "lopeta":
    print(f'"{verbi}" mitä? En ymmärtänyt.')
elif verbi == "lopeta":
    print('OK, kiitos pelistä! Nähdään taas!')
else:
    print(f'Ahaa, siis "{käyttäjän_vastaus}".')

