
"""
Created on Sat Nov 26 09:43:20 2016

@author: Ville
"""

from turtle import*

vastaus = input("e=eteen päin v=vasemmalle o=oikealle(Lopeta lopettaa): ")

while vastaus != "lopeta":
    vastaus = input("w=eteen päin d=vasemmalle a=oikealle(Lopeta lopettaa ")
    vastaus = vastaus.lower()
    if vastaus == "lopeta":
        print("loppu")
        break
    elif vastaus == "w":
        forward(50)
    elif vastaus == "d":
        left(45)
    elif vastaus == "a":
        right(45)
    else:
        print("tuntematon komento")
        
