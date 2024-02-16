ensimmäinen_nuotti = int(input("Ensimmäisen nuotin numero: "))
viimeinen_nuotti = int(input("Viimeisen nuotin numero: "))
intervalli = int(input("Haluttu intervalli:" ))

for i in range(ensimmäinen_nuotti, viimeinen_nuotti + 1, intervalli):
    print(i)