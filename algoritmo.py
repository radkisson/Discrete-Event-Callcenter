from call import deiak2
from filter import lehenengo_maila, bigarren_maila, denbora_iragarria, lehenengo_maila2, bigarren_maila2, denbora_iragarria2, lehenengo_maila3, bigarren_maila3, denbora_iragarria3
from worker import langile, langile2, langile3 
from data import tSLA, langitalde #Datu hauek importatuko ditugu

pro = 0
langutzailea = 0 
itxaroten = 0 # Hasierako bektoreak, ikusteko iritsi diren deietatik nola izan diren atendituak

for k in range(len(deiak2)): #Iristen den dei bakoitzeko
    dei_berria = deiak2[k] #Deia zehaztuko dugu
    mota = dei_berria.departamentua + 1 # 0 1 2 3 tik 1 2 3 4-ra pasatzeko
    lehenengo_langileak = lehenengo_maila(mota) #Agente espezializatuak
    lehenengo_langileak = denbora_iragarria(lehenengo_langileak) #Agente horien lan denborak
    bigarren_langileak = bigarren_maila(mota) #Lagundu dzaketen agenteak
    bigarren_langileak = denbora_iragarria(bigarren_langileak) # Agente horien lan denborak
    atendituak = 0
    for i in range(len(lehenengo_langileak)): #Agente espezializatu bakoitzeko
        if lehenengo_langileak[i].libre(dei_berria) == 1: #Agente hori libre badago
            lehenengo_langileak[i].ordutegia.append(dei_berria) #Deia gehituko diogu
            lehenengo_langileak[i].ordutegia[-1].denbora = dei_berria.ordua #Dei horren denbora langileari gehituko diogu
            atendituak = 1
            pro = pro + 1 #Kontagailua
            break  #Programa bukatuko da hurrengo deia iritsi arte
        else: #Ez badago agente espezializaturik libre
            continue
    if atendituak == 0:
        for i in range(len(bigarren_langileak)): #Lagundu dezaketen agente bakoitzeko
            if bigarren_langileak[i].libre(dei_berria) == 1: #Lagundu dezaketen agenteak libre daude
                bigarren_langileak[i].ordutegia.append(dei_berria) #Agente horri esleituko zaio deia
                bigarren_langileak[i].ordutegia[-1].denbora = dei_berria.ordua #Dei horren denbora langileari gehituko diogu
                atendituak = 1
                langutzailea = langutzailea + 1 #Kontagailua
                break  #Programa bukatuko da hurrengo deia iritsi arte
            else: #Ez dago agenterik libre eta deiak kolan itxarongo du
                continue
    if atendituak == 1:
        continue
    if atendituak == 0: #Deia kolan dago itxaroten
        concat = []
        for i in range(len(lehenengo_langileak)):  #Ikusiko dugu ze agente espezializatuk atenditu dezaketen deia
            concat.append(lehenengo_langileak[i])
        for j in range(len(bigarren_langileak)): #Ikusiko dugu ze bigarren mailako agentek atenditu dezaketen deia
            concat.append(bigarren_langileak[j]) 
        concat = denbora_iragarria(concat)
        itxaroten = itxaroten + 1 #Kontagailua
        dei_berria.denbora = concat[0].noizlibre() #Kalkulatuko dugu zein den libre geldituko den agentea
        concat[0].ordutegia.append(dei_berria) #Dei horren denbora langileari gehituko diogu
        
print(pro)
print(langutzailea)
print(itxaroten)

def SL():  #Ikusiko dugu zenbat deik kolan 5 minutu baino gutxiago itxaroten duten
    ekitaldiak = 0 
    for i in range(len(deiak2)):
        if deiak2[i].delta_t() < 5:
            ekitaldiak = ekitaldiak + 1
    return ekitaldiak/len(deiak2)

def ASA(): # Ikusiko dugu deien artean zenbatek SLA baina denbora gehiago behar izan duten deia soluzionatzeko
    ekitaldiak = 0 
    for i in range(len(deiak2)):
        j = int(deiak2[i].departamentua)
        if deiak2[i].denbora + deiak2[i].iraupena - deiak2[i].ordua < tSLA[j]:
                ekitaldiak = ekitaldiak + 1
    return ekitaldiak/len(deiak2)

def INVASA():
    return 1-ASA() 

def p_wait_queue(): #Ikusiko dugu zenbat deik itxaron behar izan duten kolan
    ekitaldiak = 0    
    for i in range(len(deiak2)):
        if deiak2[i].delta_t() > 0:
            ekitaldiak = ekitaldiak + 1
    return ekitaldiak/len(deiak2)

def lan_egin_batezbesteko(): # Ikusiko dugu agenteen okupazioa
    lan_egin = 0
    for zenbatu in range(len(langile)):
        lan_egin = lan_egin + langile[zenbatu].landenbora()
    lan_egin = lan_egin/(len(langile)*8*60)
    return lan_egin

print('{}'.format(SL()))
print('{}'.format(ASA()))
print('{}'.format(p_wait_queue()))
print('{}'.format(lan_egin_batezbesteko()))

pro = 0
langutzailea = 0 
itxaroten = 0 # Hasierako bektoreak, ikusteko iritsi diren deietatik nola izan diren atendituak

for k in range(len(deiak2)): #Iristen den dei bakoitzeko
    dei_berria = deiak2[k] #Deia zehaztuko dugu
    mota = dei_berria.departamentua + 1 # 0 1 2 3 tik 1 2 3 4-ra pasatzeko
    lehenengo_langileak = lehenengo_maila2(mota) #Agente espezializatuak
    lehenengo_langileak = denbora_iragarria2(lehenengo_langileak) #Agente horien lan denborak
    bigarren_langileak = bigarren_maila2(mota) #Lagundu dzaketen agenteak
    bigarren_langileak = denbora_iragarria2(bigarren_langileak) # Agente horien lan denborak
    atendituak = 0
    for i in range(len(lehenengo_langileak)): #Agente espezializatu bakoitzeko
        if lehenengo_langileak[i].libre(dei_berria) == 1: #Agente hori libre badago
            lehenengo_langileak[i].ordutegia.append(dei_berria) #Deia gehituko diogu
            lehenengo_langileak[i].ordutegia[-1].denbora = dei_berria.ordua #Dei horren denbora langileari gehituko diogu
            atendituak = 1
            pro = pro + 1 #Kontagailua
            break  #Programa bukatuko da hurrengo deia iritsi arte
        else: #Ez badago agente espezializaturik libre
            continue
    if atendituak == 0:
        for i in range(len(bigarren_langileak)): #Lagundu dezaketen agente bakoitzeko
            if bigarren_langileak[i].libre(dei_berria) == 1: #Lagundu dezaketen agenteak libre daude
                bigarren_langileak[i].ordutegia.append(dei_berria) #Agente horri esleituko zaio deia
                bigarren_langileak[i].ordutegia[-1].denbora = dei_berria.ordua #Dei horren denbora langileari gehituko diogu
                atendituak = 1
                langutzailea = langutzailea + 1 #Kontagailua
                break  #Programa bukatuko da hurrengo deia iritsi arte
            else: #Ez dago agenterik libre eta deiak kolan itxarongo du
                continue
    if atendituak == 1:
        continue
    if atendituak == 0: #Deia kolan dago itxaroten
        concat = []
        for i in range(len(lehenengo_langileak)):  #Ikusiko dugu ze agente espezializatuk atenditu dezaketen deia
            concat.append(lehenengo_langileak[i])
        for j in range(len(bigarren_langileak)): #Ikusiko dugu ze bigarren mailako agentek atenditu dezaketen deia
            concat.append(bigarren_langileak[j]) 
        concat = denbora_iragarria(concat)
        itxaroten = itxaroten + 1 #Kontagailua
        dei_berria.denbora = concat[0].noizlibre() #Kalkulatuko dugu zein den libre geldituko den agentea
        concat[0].ordutegia.append(dei_berria) #Dei horren denbora langileari gehituko diogu
        
print(pro)
print(langutzailea)
print(itxaroten)
print('{}'.format(SL()))
print('{}'.format(ASA()))
print('{}'.format(p_wait_queue()))
print('{}'.format(lan_egin_batezbesteko()))


pro = 0
langutzailea = 0 
itxaroten = 0 # Hasierako bektoreak, ikusteko iritsi diren deietatik nola izan diren atendituak

for k in range(len(deiak2)): #Iristen den dei bakoitzeko
    dei_berria = deiak2[k] #Deia zehaztuko dugu
    mota = dei_berria.departamentua + 1 # 0 1 2 3 tik 1 2 3 4-ra pasatzeko
    lehenengo_langileak = lehenengo_maila3(mota) #Agente espezializatuak
    lehenengo_langileak = denbora_iragarria3(lehenengo_langileak) #Agente horien lan denborak
    bigarren_langileak = bigarren_maila3(mota) #Lagundu dzaketen agenteak
    bigarren_langileak = denbora_iragarria3(bigarren_langileak) # Agente horien lan denborak
    atendituak = 0
    for i in range(len(lehenengo_langileak)): #Agente espezializatu bakoitzeko
        if lehenengo_langileak[i].libre(dei_berria) == 1: #Agente hori libre badago
            lehenengo_langileak[i].ordutegia.append(dei_berria) #Deia gehituko diogu
            lehenengo_langileak[i].ordutegia[-1].denbora = dei_berria.ordua #Dei horren denbora langileari gehituko diogu
            atendituak = 1
            pro = pro + 1 #Kontagailua
            break  #Programa bukatuko da hurrengo deia iritsi arte
        else: #Ez badago agente espezializaturik libre
            continue
    if atendituak == 0:
        for i in range(len(bigarren_langileak)): #Lagundu dezaketen agente bakoitzeko
            if bigarren_langileak[i].libre(dei_berria) == 1: #Lagundu dezaketen agenteak libre daude
                bigarren_langileak[i].ordutegia.append(dei_berria) #Agente horri esleituko zaio deia
                bigarren_langileak[i].ordutegia[-1].denbora = dei_berria.ordua #Dei horren denbora langileari gehituko diogu
                atendituak = 1
                langutzailea = langutzailea + 1 #Kontagailua
                break  #Programa bukatuko da hurrengo deia iritsi arte
            else: #Ez dago agenterik libre eta deiak kolan itxarongo du
                continue
    if atendituak == 1:
        continue
    if atendituak == 0: #Deia kolan dago itxaroten
        concat = []
        for i in range(len(lehenengo_langileak)):  #Ikusiko dugu ze agente espezializatuk atenditu dezaketen deia
            concat.append(lehenengo_langileak[i])
        for j in range(len(bigarren_langileak)): #Ikusiko dugu ze bigarren mailako agentek atenditu dezaketen deia
            concat.append(bigarren_langileak[j]) 
        concat = denbora_iragarria(concat)
        itxaroten = itxaroten + 1 #Kontagailua
        dei_berria.denbora = concat[0].noizlibre() #Kalkulatuko dugu zein den libre geldituko den agentea
        concat[0].ordutegia.append(dei_berria) #Dei horren denbora langileari gehituko diogu
        
print(pro)
print(langutzailea)
print(itxaroten)
print('{}'.format(SL()))
print('{}'.format(ASA()))
print('{}'.format(p_wait_queue()))
print('{}'.format(lan_egin_batezbesteko()))
