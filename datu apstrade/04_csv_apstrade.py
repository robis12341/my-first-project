import csv


with open("datu apstrade/edieni.csv", "r", encoding="utf-8-sig", newline="") as fails:
    dati = csv.DictReader(fails, delimiter=";")
        
# piemērs - izvadīt ēdienus, kuri pieejami
#    for rinda in dati:
#        if rinda["Pieejams"] == "Jā":
#            print(rinda["Nosaukums"], "-", rinda["Cena_EUR"], "EUR")

#1    for rinda in dati:
#        if float (rinda ["Cena_EUR"]) <= 6:
#            print(rinda["Nosaukums"], "-", rinda["Cena_EUR"], "EUR")

#2    for rinda in dati:
#        if rinda["Svars_g"] >= "300" and rinda["Kategorija"] == "Pamatēdiens":
#            print(rinda["Nosaukums"], "-", rinda["Cena_EUR"], "EUR")

#3    for rinda in dati:
#        if rinda["Kalorijas_kcal"] <= "400":
#            print(rinda["Nosaukums"], "-", rinda["Cena_EUR"], "EUR")

    





# Izvada visus lauku nosaukumus
    #print(dati.fieldnames)

# UZDEVUMI PATSTĀVĪGAI RISINĀŠANAI
# 1.	Atlasīt visus pieejamos ēdienus, kuru cena nepārsniedz 6 EUR.
# 2.	Izvadīt visus pamatēdienus, kuru svars pārsniedz 300 gramus.
# 3.	Atrast ēdienus, kuru kaloriju daudzums ir mazāks par 400 kcal.
# 4.	Izvadīt produktus, kuru pagatavošanas laiks nepārsniedz 15 minūtes.
# 5.	Atrast visdārgāko un vislētāko produktu.
# 6.	Aprēķināt visu pieejamo produktu vidējo cenu.
# 7.	Saskaitīt produktu skaitu katrā kategorijā.
# 8.	Atlasīt desertus un sakārtot tos pēc kaloriju daudzuma.
# 9.	Atrast produktus, kuru cena ir mazāka par 8 EUR un pagatavošanas laiks nepārsniedz 20 minūtes.
# 10.	Izveidot jaunu CSV failu, kurā saglabāti tikai pieejamie produkti.