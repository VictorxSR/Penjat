from Paraules import *
import sys
import os

llista = []
joc = []
caselles = []
i = 0
oportunitats = 6
clear = lambda: os.system('clear') 
won = None
lletres = []
trues = 0

clear()

llista = Paraules.omplirLlistaParaules()

paraula = Paraules.obtenirParaula(llista)

joc = Paraules.separarParaula(paraula)

caselles = Paraules.iniciarJoc(joc)



while True:

    if oportunitats > 0: 
        print("Oportunitats restants: %i" % oportunitats)
        print("Lletres utilitzades: %s\n" % lletres)
        print(paraula)

        Paraules.situacioJoc(joc, caselles)
        lletra, lletres = Paraules.demanarLletra(lletres)
        trobat = Paraules.comprovarLletra(lletra, caselles, joc)

        if not trobat:
            oportunitats -= 1
        

      
        trues = Paraules.checkEqual(caselles)


        if trues == len(caselles): #caselles totes a True
            won = True
            break


        clear()
    else:
        won = False
        break  
    
clear()   

print("Oportunitats restants: %i" % oportunitats)  
print("Lletres utilitzades: %s\n" % lletres) 

Paraules.situacioJoc(joc, caselles)

if won:
    print("\n\nHas guanyat")
else:
    print("\n\nHas perdut, la paraula era: %s" % paraula)
    

    


