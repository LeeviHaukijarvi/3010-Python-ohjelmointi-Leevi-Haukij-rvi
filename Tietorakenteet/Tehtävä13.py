def on_palindromi(lause):
    uusi_lause = ""
    lause = lause.lower()
    for i in lause:
        if i.isalpha():
            i = i.lower()
            uusi_lause += i
    uusi_lause_takaperin = ''.join(list(reversed(uusi_lause)))

    return uusi_lause == uusi_lause_takaperin


ehdokkaat = [
    'A man, a plan, a canal: Panama.',
    'Iso rikas sika sökösakissa kirosi.',
    '"Aa, viinaa sitruksilla", kallis kurtisaani ivaa.',
    'Joku satunnainen lause'
]
for e in ehdokkaat:
    tulos = 'EI OLE'
    if on_palindromi(e):
        tulos = 'ON'
    print(f'"{e}": {tulos} palindromi')