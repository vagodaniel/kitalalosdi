"""
szam=int(input("Kerek egy szamot    "))
if szam%3==0 and szam%5==0: 
    print("fizbuzz")

elif szam%3==0:
    print("fizz")

elif szam%5==0:
    print("buzz")

else:
    print("nem")
"""

import random
gondolt_szam=random.randint(1,100)
tipp=int(input("szam:"))
lepes=0
kitalaltad=False
while kitalaltad==False:
    if tipp==gondolt_szam:
        lepes+=1
        #lepes=lepes+1 megszamlalas
        print(f"{lepes}-ből talaltad ki")
        kitalaltad=True
    elif tipp>gondolt_szam:
        print("adj kisebbet")
        lepes+=1
        #lepes=lepes+1 megszamlalas
        tipp=int(input())

    elif tipp<gondolt_szam:
        print("adj nagyobbat")
        lepes+=1
        #lepes=lepes+1 megszamlalas
        tipp=int(input())

        """
        adj meg egy szamot, a gep talalja ki
        """