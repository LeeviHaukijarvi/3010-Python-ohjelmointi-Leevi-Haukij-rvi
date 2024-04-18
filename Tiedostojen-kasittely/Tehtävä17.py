def muunna_sekunneiksi(aika):
    minuutit, sekunnit = map(int, aika.split(':'))
    return minuutit * 60 + sekunnit

def muunna_minuuteiksi(aika):
    minuutit = aika // 60
    sekunnit = aika % 60
    return f'{minuutit}:{sekunnit}'

a_levyn_pituus = 0
b_levyn_pituus = 0

with open('levyt.txt', 'r') as tiedosto:
    for line in tiedosto:
        levy, pituus = line.strip().split(' ')

        if 'A' in levy:
            a_levyn_pituus = a_levyn_pituus + muunna_sekunneiksi(pituus)
        elif 'B' in levy:
            b_levyn_pituus = b_levyn_pituus + muunna_sekunneiksi(pituus)


print(f'Levy A: {muunna_minuuteiksi(a_levyn_pituus)}')
print(f'Levy B: {muunna_minuuteiksi(b_levyn_pituus)}')
print(f'Yhteensä: {muunna_minuuteiksi(a_levyn_pituus + b_levyn_pituus)}')