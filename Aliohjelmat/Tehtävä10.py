def yksi_sanainen(sana):
    pilkottu_vastaus = sana.split()
    osien_määrä = len(pilkottu_vastaus)
    if osien_määrä == 2:
        print('Sana ei ole yksiosainen!')
    elif osien_määrä == 1:
        return True

def kaksi_sanainen(sana_1, sana_2):
    print(f'{sana_1} {sana_2}')