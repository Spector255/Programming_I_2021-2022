skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
while ((skaitlis != "exit") and (skaitlis != "EXIT") and (skaitlis != "Exit")):
    if (skaitlis == "1"):
        print("Ieiet kabinetā tikai ar skolotāja atļauju pa vienam, negrūstoties, pēc tam ieņemot savu darba vietu.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    elif (skaitlis == "2"):
        print("Nedrīkst veikt datorā esošās informācijas maiņu")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    elif (skaitlis == "3"):
        print("Nedrīkst spēlēt datorspēles")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    elif (skaitlis == "4"):
        print("Nebojāt vadu izolāciju un citas darba vietā izvietotās iekārtas.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    elif (skaitlis == "5"):
        print("Ieslēgt datortehniku, ielogoties vai sākt darbu tikai ar skolotāja atļauju.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    elif (skaitlis == "6"):
        print("Darbs bez pārtraukuma nedrīkst būt ilgāks par 60 minūtēm.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    elif (skaitlis == "7"):
        print("Ja darba laikā rodas elektrobojājumi (dzirksteļošana, dūmu vai liesmu parādīšanās), nekavējoties jāpārtrauc darbs, datortehnika jāatslēdz no elektriskā tīkla, par radušos situāciju jāinformē skolotājs.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    elif (skaitlis == "8"):
        print("Jāsēž pretī monitora ekrānam, jāseko, lai darba laikā attālums no acīm līdz monitora ekrānam būtu 45-75 cm.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
    else:
        print("Nekorekts ievads, ievadam jābut no 1. līdz 8.")
        skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
print("Paldies!")