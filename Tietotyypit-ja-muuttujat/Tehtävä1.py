energia_perusmaksu_kk = 1.98
energia_energiamaksu_snt = 7.09

siirto_perusmaksu_kk = 4.77
siirto_siirtomaksu_kWh = 2.9264
siirto_vero_kWh = 2.79372

lokakuu = 642.934
marraskuu = 674.345
joulukuu = 757.599

sähköenergia_kulutus_yhteensä_kWh = lokakuu + marraskuu + joulukuu
sähköenergia_kulutus_yhteensä_snt = (sähköenergia_kulutus_yhteensä_kWh * energia_energiamaksu_snt)
+ energia_perusmaksu_kk

siirto_kulutus_yhteensä_snt = (siirto_siirtomaksu_kWh * sähköenergia_kulutus_yhteensä_kWh) + (siirto_vero_kWh * sähköenergia_kulutus_yhteensä_kWh)
+ siirto_perusmaksu_kk

lasku_loppusumma = sähköenergia_kulutus_yhteensä_snt + siirto_kulutus_yhteensä_snt

print(lasku_loppusumma)