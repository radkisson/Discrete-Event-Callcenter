import itertools # Pakete hau kargatuko dugu gero matrizeak errezago lotzeko
from data import langitalde, A, B, C, tSLA # Data fitxerotik kargatuko ditugun matrizeak

# Langileak objetu bezala definituko ditugu

class Langileak_mota:

    def __init__(self,departamentua,zenbakia,komertziala, logistika, programazioa, mantentze, sla):  #Definituko ditugun aldagaiak
        self.departamentua = departamentua # Agente bakoitzaren departamentua.
        self.zenbakia      = zenbakia # Agente bakoitzaren zenbakia (departamentu bakoitzean 3-5 agente daude)
        self.ordutegia     = [] # Agente bakoitzak egiten duen lan denbora ikusteko lista hutsa sortuko dugu
        self.komertziala   = komertziala # Departamentu komertziala definituko dugu
        self.logistika     = logistika # Departamentu logistikoa definituko dugu
        self.programazioa  = programazioa  # Departamentu informatikoa definituko dugu
        self.mantentze     = mantentze # Departamentu mantenimendukoa definituko dugu
        self.sla           = 0 # SLA definituko dugu hasierako bektore bat bezala
        self.tracer        = "Kaixo" # Hasierako bektorea
    
    def __repr__(self):   # Lortuko dugu agente bakoitza sailkatzea, departamentu eta zenbaki jakin batekin
         return 'Langileak_mota: Departamentua {} Zenbakia {}'.format(self.departamentua,self.zenbakia) 
        
    def noizlibre(self):  # Ikusiko dugu ea agentea libre dagoen edo noiz geldituko den libre
        if len(self.ordutegia) == 0: # Libre dago
            return 0
        else:
            available = self.ordutegia[-1].ordua + self.ordutegia[-1].iraupena + self.ordutegia[-1].delta_t()
            # Ez badago libre kalkulatu dezakegu noiz geldituko den libre
            return available
    
    def libre(self,deiak): #Ikusiko dugu ea agentea libre dagoen eta deia har dezakeen
        if self.noizlibre() == 0: # Libre dago agentea
            return 1
        if self.noizlibre() < deiak.ordua :  # Gainera behar dugu lehenego agentea libre gelditzea deia iristen den momentuan
            return 1
        else: # Ez dago libre
            return 0
        
    def landenbora(self):  # Kalkulatuko dugu agente bakoitzak lan egindako denbora
        time = 0
        for i in range(len(self.ordutegia)):
            time = time + self.ordutegia[i].iraupena
        return time
    
    def aldaketa(self, zenbakia):  # Dei sarrera zerrenda matrizean zenbaki bakoitza departamentu bakoitzari egokituko zaio
        if zenbakia == 1:
            return self.komertziala
        if zenbakia == 2:
            return self.logistika
        if zenbakia == 3:
            return self.programazioa
        if zenbakia == 4:
            return self.mantentze

dept = 0
langile = [] # Hasteko lista hutsa sortuko dugu
for i in langitalde: #Langileen matrizea sortuko dugu
    for j in range(i):
        langile.append(Langileak_mota(dept,j,0,0,0,0,0))
        langile[-1].sla = tSLA[dept]
    dept = dept + 1

for i in range(len(langile)):
    langile[i].komertziala  = 2
    langile[i].logistika  = 2
    langile[i].programazioa  = 2
    langile[i].mantentze  = 2

for i in range(len(langile)):
    if A[i,0] == 1:
        langile[i].komertziala  = 8
    if A[i,0] == 2:
        langile[i].logistika  = 8
    if A[i,0] == 3:
        langile[i].programazioa  = 8
    if A[i,0] == 4:
        langile[i].mantentze  = 8
    if A[i,1] == 1:
        langile[i].komertziala  = 5
    if A[i,1] == 2:
        langile[i].logistika  = 5
    if A[i,1] == 3:
        langile[i].programazioa  = 5
    if A[i,1] == 4:
        langile[i].mantentze  = 5

dept = 0
langile2 = [] # Hasteko lista hutsa sortuko dugu
for i in langitalde: #Langileen matrizea sortuko dugu
    for j in range(i):
        langile2.append(Langileak_mota(dept,j,0,0,0,0,0))
        langile2[-1].sla = tSLA[dept]
    dept = dept + 1

for i in range(len(langile2)):
    langile2[i].komertziala  = 2
    langile2[i].logistika  = 2
    langile2[i].programazioa  = 2
    langile2[i].mantentze  = 2

for i in range(len(langile2)):
    if B[i,0] == 1:
        langile2[i].komertziala  = 8
    if B[i,0] == 2:
        langile2[i].logistika  = 8
    if B[i,0] == 3:
        langile2[i].programazioa  = 8
    if B[i,0] == 4:
        langile2[i].mantentze  = 8
    if B[i,1] == 1:
        langile2[i].komertziala  = 5
    if B[i,1] == 2:
        langile2[i].logistika  = 5
    if B[i,1] == 3:
        langile2[i].programazioa  = 5
    if B[i,1] == 4:
        langile2[i].mantentze  = 5
    
dept = 0
langile3 = [] # Hasteko lista hutsa sortuko dugu
for i in langitalde: #Langileen matrizea sortuko dugu
    for j in range(i):
        langile3.append(Langileak_mota(dept,j,0,0,0,0,0))
        langile3[-1].sla = tSLA[dept]
    dept = dept + 1

for i in range(len(langile3)):
    langile3[i].komertziala  = 2
    langile3[i].logistika  = 2
    langile3[i].programazioa  = 2
    langile3[i].mantentze  = 2

for i in range(len(langile3)):
    if C[i,0] == 1:
        langile3[i].komertziala  = 8
    if C[i,0] == 2:
        langile3[i].logistika  = 8
    if C[i,0] == 3:
        langile3[i].programazioa  = 8
    if C[i,0] == 4:
        langile3[i].mantentze  = 8
    if C[i,1] == 1:
        langile3[i].komertziala  = 5
    if C[i,1] == 2:
        langile3[i].logistika  = 5
    if C[i,1] == 3:
        langile3[i].programazioa  = 5
    if C[i,1] == 4:
        langile3[i].mantentze  = 5