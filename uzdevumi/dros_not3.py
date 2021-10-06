def drosibas_noteikumi():
    drosnot = [
        "Ieiet kabinetā tikai ar skolotāja atļauju pa vienam, negrūstoties, pēc tam ieņemot savu darba vietu.",
        "Nedrīkst veikt datorā esošās informācijas maiņu",
        "Nedrīkst spēlēt datorspēles",
        "Nebojāt vadu izolāciju un citas darba vietā izvietotās iekārtas.",
        "Ieslēgt datortehniku, ielogoties vai sākt darbu tikai ar skolotāja atļauju.",
        "Darbs bez pārtraukuma nedrīkst būt ilgāks par 60 minūtēm.",
        "Ja darba laikā rodas elektrobojājumi (dzirksteļošana, dūmu vai liesmu parādīšanās), nekavējoties jāpārtrauc darbs, datortehnika jāatslēdz no elektriskā tīkla, par radušos situāciju jāinformē skolotājs.",
        "Jāsēž pretī monitora ekrānam, jāseko, lai darba laikā attālums no acīm līdz monitora ekrānam būtu 45-75 cm.",
    ]
    cipari = [1,2,3,4,5,6,7,8]
    skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    while (skaitlis != "Exit"):
        if (skaitlis in cipari):
            print(drosnot[skaitlis+1])
        else:
            print("Nekorekts ievads, ievadam jābut no 1. līdz 8.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    print("Paldies!")


drosibas_noteikumi()
