aloitus = input("aloitus, esimerkiksi tervehdys: ")
opettaja = input("Opettajan nimi: ")
kotitehtävä = input("Kotitehtävän tyyppi: ")
lemmikki_laji = input("Lemmikin laji: ")
lemmikki_nimi = input("Lemmikin nimi: ")
lemmikki_teki = input("Lemmikki teki (menneessä muodossa): ")

lause = f"{aloitus}, {opettaja}, en tiedä mihin se {kotitehtävä} oikein joutui. Lemmikki{lemmikki_laji}ni {lemmikki_nimi} varmaankin {lemmikki_teki} sen."

print(lause)