print('Kävelet pimeällä kadulla, vastaasi tulee ryöstäjä. Mitä teet?')
käyttäjän_vastaus = input('Anna verbi, jonka jälkeen objekti: ')
pilkottu_vastaus = käyttäjän_vastaus.split()

verbi = pilkottu_vastaus[0]
objekti = pilkottu_vastaus[1]

print(f'Verbi = "{verbi}" \nObjekti = "{objekti}"')
