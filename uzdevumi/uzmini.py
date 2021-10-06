import random

def parbaude(skaitlis):
    solis=1
    sk = int(input("Ievadi skaitļi: "))
    while sk != skaitlis:
        if sk < skaitlis:
            solis+=1
            sk = int(input("Mini lielāku skaitli: "))
        elif sk > skaitlis:
            solis+=1
            sk =int(input("Mini mazāku skaitli: "))
    print(f"Uzmineji ar {solis}. minējumu!")
parbaude(random.randint(1,100))