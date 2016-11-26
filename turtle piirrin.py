# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 09:43:20 2016

@author: Ville
"""

import turtle
while vastaus != "lopeta":
    print("sinuulla on", voitot ,"pistettä")
    vastaus = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
    vastaus = vastaus.lower()
    if vastaus == "lopeta":
        print("Pelasit", laskuri, "kierrosta, joista voitit", voitot, "ja pelasit tasan", tasapelit, "peliä.")
        break
    if vastaus == ""
    elif
    elif vastaus == "ydinase" and tietokone == "jalka":
        print("Voitit!")
        voitot = voitot + 1
        laskuri = laskuri + 1
    elif vastaus == "torakka" and tietokone == "ydinase":
        print("Voitit!")
        voitot = voitot + 1
        laskuri = laskuri + 1
    else:
        print("Hävisit!")
        laskuri = laskuri + 1