#MAP
def kvadrats(sk):
    return sk**2

print(kvadrats(2))
skaitlis = [1,2,3,4,5,59,48]
print(map(kvadrats,skaitlis)) #nelīdz, jo nepieciešama iterācija

#1. variants
for i in map(kvadrats,skaitlis):
    print (i)

#2. variants
print(list(map(kvadrats,skaitlis)))

def paris(vards):
    if (len(vards)%2==0):
        return  "Pāris"
    else:
        return vards[0:1]
print(paris("Skola"))
vardi = ["programma", "stunda", "zvans", "roze", "stunda", "zvans", "roze"]

print(list(map(paris,vardi)))

#from math import*
import math
def laukums (radius):
    return(math.pi*radius**2) #math.pi = pi
radiusi=[2,3,8,14,9]
print(list(map(laukums,radiusi)))
############# filter
def paris(sk):
    return sk%2==0
print(paris(15))

skaitli = [1,2,3,4,5,6]
print(list(filter(paris,skaitli))) #Pievieno listā tādās vertības, kuri atgriež True
#vai
for i in filter(paris, skaitli):
    print(i)

def laukums2 (radius):
    S=math.pi*radius**2 #math.pi = pi
    return S > 100

radiusi=[2,3,8,14,9,3.5]
print(list(filter(laukums2,radiusi)))

############## lambda expression (jeb anonīma funkcija)
def kvadrats1(sk):
    rezultats=sk**2
    return rezultats

def kvadrats2(sk):
    return sk**2

def kvadrats3(sk):return sk**2
#noņem funkcijas definīciju un aizstāj ar lambda
rezultats2 = lambda sk:sk**2
print(rezultats2(15))

#sakombinē ar map
print(list(map(lambda sk:sk**2,radiusi)))

#sakombīne ar filter
print(list(filter(lambda sk:sk%2==0,skaitli)))