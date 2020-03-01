# Agente espezializatuak eta lagundu dezaketenak sortuko ditugu
from worker import langile, langile2, langile3 # Langileak importatuko ditugu

def langile_gaitasun_departamentua(zenbakia): #Sortuko dugu agenteen lista bat ordenatuta gaitasunengatik
    return sorted(langile , key=lambda x: x.aldaketa(zenbakia), reverse=True)

def langile_gaitasun_departamentua2(zenbakia): 
    return sorted(langile2 , key=lambda x: x.aldaketa(zenbakia), reverse=True)

def langile_gaitasun_departamentua3(zenbakia): 
    return sorted(langile3 , key=lambda x: x.aldaketa(zenbakia), reverse=True)

def lehenengo_maila(departamentua): #Sortuko ditugu dei jakin baterako ditugun agente espezializatuak
    lista = langile_gaitasun_departamentua(departamentua)
    lista.reverse()
    length = len(lista)
    zenbatu = 0
    for i in range(length):
        if lista[i].aldaketa(departamentua) == 8: #Gaitasun agente matrizean 8 duten agenteak
            zenbatu = zenbatu + 1
    for j in range(length - zenbatu):
        lista.pop(0)
    lista.reverse()
    return lista

def lehenengo_maila2(departamentua): #Sortuko ditugu dei jakin baterako ditugun agente espezializatuak
    lista = langile_gaitasun_departamentua2(departamentua)
    lista.reverse()
    length = len(lista)
    zenbatu = 0
    for i in range(length):
        if lista[i].aldaketa(departamentua) == 8: #Gaitasun agente matrizean 8 duten agenteak
            zenbatu = zenbatu + 1
    for j in range(length - zenbatu):
        lista.pop(0)
    lista.reverse()
    return lista

def lehenengo_maila3(departamentua): #Sortuko ditugu dei jakin baterako ditugun agente espezializatuak
    lista = langile_gaitasun_departamentua3(departamentua)
    lista.reverse()
    length = len(lista)
    zenbatu = 0
    for i in range(length):
        if lista[i].aldaketa(departamentua) == 8: #Gaitasun agente matrizean 8 duten agenteak
            zenbatu = zenbatu + 1
    for j in range(length - zenbatu):
        lista.pop(0)
    lista.reverse()
    return lista

def bigarren_maila(departamentua): #Dei jakin baterako lagundu dezaketen agenteak
    lista = langile_gaitasun_departamentua(departamentua)
    zenbatu = 0
    for i in range(len(lista)):
            konparatu = lista[i].aldaketa(departamentua)
            if konparatu < 5 or konparatu > 7 :
                zenbatu = zenbatu + 1 # Kasu honetan kontatuko ditugu baina ezer egin gabe
    while zenbatu != 0:
        for i in range(len(lista)):
            konparatu = lista[i].aldaketa(departamentua)
            if konparatu < 5 or konparatu > 7 : # Agente gaitasun matrizean 5 eta 7 artean dagoenean deia beraiei pasako zaie
                lista.pop(i)
                zenbatu = zenbatu - 1
                break
    return lista

def bigarren_maila2(departamentua): #Dei jakin baterako lagundu dezaketen agenteak
    lista = langile_gaitasun_departamentua2(departamentua)
    zenbatu = 0
    for i in range(len(lista)):
            konparatu = lista[i].aldaketa(departamentua)
            if konparatu < 5 or konparatu > 7 :
                zenbatu = zenbatu + 1 # Kasu honetan kontatuko ditugu baina ezer egin gabe
    while zenbatu != 0:
        for i in range(len(lista)):
            konparatu = lista[i].aldaketa(departamentua)
            if konparatu < 5 or konparatu > 7 : # Agente gaitasun matrizean 5 eta 7 artean dagoenean deia beraiei pasako zaie
                lista.pop(i)
                zenbatu = zenbatu - 1
                break
    return lista

def bigarren_maila3(departamentua): #Dei jakin baterako lagundu dezaketen agenteak
    lista = langile_gaitasun_departamentua3(departamentua)
    zenbatu = 0
    for i in range(len(lista)):
            konparatu = lista[i].aldaketa(departamentua)
            if konparatu < 5 or konparatu > 7 :
                zenbatu = zenbatu + 1 # Kasu honetan kontatuko ditugu baina ezer egin gabe
    while zenbatu != 0:
        for i in range(len(lista)):
            konparatu = lista[i].aldaketa(departamentua)
            if konparatu < 5 or konparatu > 7 : # Agente gaitasun matrizean 5 eta 7 artean dagoenean deia beraiei pasako zaie
                lista.pop(i)
                zenbatu = zenbatu - 1
                break
    return lista

def denbora_iragarria(langile):  #Sortuko dugu agenteen lista bat, lan egindako denborarekin alderantziz ordenatuta 
    aldiz = sorted(langile , key=lambda x: x.landenbora(), reverse=True)
    aldiz.reverse()
    return aldiz

def denbora_iragarria2(langile2):  #Sortuko dugu agenteen lista bat, lan egindako denborarekin alderantziz ordenatuta 
    aldiz = sorted(langile2 , key=lambda x: x.landenbora(), reverse=True)
    aldiz.reverse()
    return aldiz

def denbora_iragarria3(langile2):  #Sortuko dugu agenteen lista bat, lan egindako denborarekin alderantziz ordenatuta 
    aldiz = sorted(langile2 , key=lambda x: x.landenbora(), reverse=True)
    aldiz.reverse()
    return aldiz