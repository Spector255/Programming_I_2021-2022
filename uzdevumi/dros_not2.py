drosnot = {
    "1":"Ieiet kabinetā tikai ar skolotāja atļauju pa vienam, negrūstoties, pēc tam ieņemot savu darba vietu.",
    "2":"Nedrīkst veikt datorā esošās informācijas maiņu",
    "3":"Nedrīkst spēlēt datorspēles",
    "4":"Nebojāt vadu izolāciju un citas darba vietā izvietotās iekārtas.",
    "5":"Ieslēgt datortehniku, ielogoties vai sākt darbu tikai ar skolotāja atļauju.",
    "6":"Darbs bez pārtraukuma nedrīkst būt ilgāks par 60 minūtēm.",
    "7":"Ja darba laikā rodas elektrobojājumi (dzirksteļošana, dūmu vai liesmu parādīšanās), nekavējoties jāpārtrauc darbs, datortehnika jāatslēdz no elektriskā tīkla, par radušos situāciju jāinformē skolotājs.",
    "8":"Jāsēž pretī monitora ekrānam, jāseko, lai darba laikā attālums no acīm līdz monitora ekrānam būtu 45-75 cm.",
}
skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
while ((skaitlis != "exit") and (skaitlis != "EXIT") and (skaitlis != "Exit")):
    print(drosnot.get(skaitlis))
    skaitlis = input("Ievadiet drošibas noteikumu numuru: ")
print("Paldies!")