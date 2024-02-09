import calendar


kuukausi_numerona = int(input("Anna kuukauden numero: "))
vuosi = int(input("Anna vuosiluku: "))

kuukausi_kirjoitettuna = calendar.month_name[kuukausi_numerona]
helmikuu_karkaako = calendar.isleap(vuosi)
kuukauden_päivät = 0

if kuukausi_numerona == 1 or kuukausi_numerona == 3 or kuukausi_numerona == 5 or kuukausi_numerona == 7 or kuukausi_numerona == 9 or kuukausi_numerona == 11:
    kuukauden_päivät = 31
elif kuukausi_numerona == 4 or kuukausi_numerona == 6 or kuukausi_numerona == 8 or kuukausi_numerona == 10 or kuukausi_numerona == 12:
    kuukauden_päivät = 30
elif kuukausi_numerona == 2:
    if helmikuu_karkaako == True:
        kuukauden_päivät = 29
    else:
        kuukauden_päivät = 28

print(f'In {vuosi} {kuukausi_kirjoitettuna} there are {kuukauden_päivät} days.')