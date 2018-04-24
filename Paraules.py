import random
from contextlib import contextmanager
import sys
import os

class Paraules:

   
    def omplirLlistaParaules():

        dict_path = os.path.join(os.path.dirname(__file__),  'diccionari.txt')
        
        with open(dict_path, 'r') as f:
            #for line in f
            file_ = f.readlines()
        
         
        # list comprehension
        list_ = [line.rstrip('\n') for line in file_ if line != '\n'] #rstrip elimina algun caracter al final del string, si es deia rstrip() eliminara els espais en blanc

        

        return list_   


    def obtenirParaula(list_):

        return  (random.choice(list_)) #retorna una paraula aleatoria dins de la llista
        

    
    def separarParaula(paraula):
        return list(paraula)


    def iniciarJoc(joc):
        return [False]*len(joc)
    

    def situacioJoc(joc, caselles):
        i = 0

        for (cas, jo) in zip(caselles,joc): #zip et permet moure llistes a la vegada
            if cas:
                print(jo, end="")
            else:
                print("-", end="")
            


    def demanarLletra(lletres):


        while True:
            sys.stdin.flush()
            lletra = input("\n\nIntrodueix una lletra: ")

            if len(lletra) == 1:
                lletres.append(lletra)
                break

        return lletra, lletres


    def comprovarLletra(lletra, caselles, joc):

        i = 0

        caselles_old = []

        for(cas, jo) in zip(caselles,joc):
        
            caselles_old.insert(i, cas)
            
            if jo == lletra:
                caselles[i] = True
                
            i += 1

        
        return caselles_old != caselles
 
    def checkEqual(lst):

        trues = lst.count(True) #es pot fer un count d'una llista/tupla d'un valor en concret
            
        return trues
        