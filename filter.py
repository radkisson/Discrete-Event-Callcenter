# Agente espezializatuak eta lagundu dezaketenak sortuko ditugu
from worker import workers, workers2, workers3  # Import worker lists

def workers_by_skill(number):
    """Return workers sorted by skill for the given department."""
    return sorted(workers, key=lambda x: x.aldaketa(number), reverse=True)

def workers_by_skill2(number):
    return sorted(workers2, key=lambda x: x.aldaketa(number), reverse=True)

def workers_by_skill3(number):
    return sorted(workers3, key=lambda x: x.aldaketa(number), reverse=True)

def first_level(department):
    """Return specialized agents for a given call type."""
    lista = workers_by_skill(department)
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

def first_level2(department):
    lista = workers_by_skill2(department)
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

def first_level3(department):
    lista = workers_by_skill3(department)
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

def second_level(department):
    """Return helper agents for a given call type."""
    lista = workers_by_skill(department)
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

def second_level2(department):
    lista = workers_by_skill2(department)
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

def second_level3(department):
    lista = workers_by_skill3(department)
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

def sort_by_work_time(worker_list):
    """Return workers sorted by amount of work done."""
    ordered = sorted(worker_list, key=lambda x: x.landenbora(), reverse=True)
    ordered.reverse()
    return ordered

def sort_by_work_time2(worker_list):
    ordered = sorted(worker_list, key=lambda x: x.landenbora(), reverse=True)
    ordered.reverse()
    return ordered

def sort_by_work_time3(worker_list):
    ordered = sorted(worker_list, key=lambda x: x.landenbora(), reverse=True)
    ordered.reverse()
    return ordered
