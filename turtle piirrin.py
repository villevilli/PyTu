
"""
Created on Sat Nov 26 09:43:20 2016

@author: Ville
"""

import turtle
forward(200)

vastaus = input("e=eteen päin v=vasemmalle o=oikealle(Lopeta lopettaa): ")

while vastaus != "lopeta":
    vastaus = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
    vastaus = vastaus.lower()
    if vastaus == "lopeta":
        print("loppu")
        break
    elif vastaus == "e":
        forward(50)
    elif vastaus == "v":
        left(90)
    elif vastaus == "o":
        right(90)
    else:
        print("tuntematon komento")
        