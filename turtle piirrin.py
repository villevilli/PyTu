# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 09:43:20 2016

@author: Ville
"""

from turtle inport
while vastaus != "lopeta":
    vastaus = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
    vastaus = vastaus.lower()
    if vastaus == "lopeta":
        print("loppu")
        break
    if vastaus == "e":
        forward(50)
    elif vastaus == "v":
        left(90)
    elif vastaus == "o":
        right(90)
    else:
        print("tuntematon komento")
        