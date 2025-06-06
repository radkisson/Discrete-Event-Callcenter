import itertools  # Helper for constructing the worker matrices
from data import team_size, A, B, C, tSLA  # Matrices generated in data.py

# Langileak objetu bezala definituko ditugu

class WorkerType:

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
    
    def __repr__(self):
        """Return a readable representation of the worker."""
        return 'WorkerType: Department {} Number {}'.format(
            self.departamentua, self.zenbakia
        )
        
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
workers = []  # Initial empty list of workers
for i in team_size:  # Build the first worker list
    for j in range(i):
        workers.append(WorkerType(dept, j, 0, 0, 0, 0, 0))
        workers[-1].sla = tSLA[dept]
    dept = dept + 1

for i in range(len(workers)):
    workers[i].komertziala = 2
    workers[i].logistika = 2
    workers[i].programazioa = 2
    workers[i].mantentze = 2

for i in range(len(workers)):
    if A[i,0] == 1:
        workers[i].komertziala = 8
    if A[i,0] == 2:
        workers[i].logistika = 8
    if A[i,0] == 3:
        workers[i].programazioa = 8
    if A[i,0] == 4:
        workers[i].mantentze = 8
    if A[i,1] == 1:
        workers[i].komertziala = 5
    if A[i,1] == 2:
        workers[i].logistika = 5
    if A[i,1] == 3:
        workers[i].programazioa = 5
    if A[i,1] == 4:
        workers[i].mantentze = 5

dept = 0
workers2 = []  # Second worker matrix
for i in team_size:  # Build the second worker list
    for j in range(i):
        workers2.append(WorkerType(dept, j, 0, 0, 0, 0, 0))
        workers2[-1].sla = tSLA[dept]
    dept = dept + 1

for i in range(len(workers2)):
    workers2[i].komertziala = 2
    workers2[i].logistika = 2
    workers2[i].programazioa = 2
    workers2[i].mantentze = 2

for i in range(len(workers2)):
    if B[i,0] == 1:
        workers2[i].komertziala = 8
    if B[i,0] == 2:
        workers2[i].logistika = 8
    if B[i,0] == 3:
        workers2[i].programazioa = 8
    if B[i,0] == 4:
        workers2[i].mantentze = 8
    if B[i,1] == 1:
        workers2[i].komertziala = 5
    if B[i,1] == 2:
        workers2[i].logistika = 5
    if B[i,1] == 3:
        workers2[i].programazioa = 5
    if B[i,1] == 4:
        workers2[i].mantentze = 5
    
dept = 0
workers3 = []  # Third worker matrix
for i in team_size:  # Build the third worker list
    for j in range(i):
        workers3.append(WorkerType(dept, j, 0, 0, 0, 0, 0))
        workers3[-1].sla = tSLA[dept]
    dept = dept + 1

for i in range(len(workers3)):
    workers3[i].komertziala = 2
    workers3[i].logistika = 2
    workers3[i].programazioa = 2
    workers3[i].mantentze = 2

for i in range(len(workers3)):
    if C[i,0] == 1:
        workers3[i].komertziala = 8
    if C[i,0] == 2:
        workers3[i].logistika = 8
    if C[i,0] == 3:
        workers3[i].programazioa = 8
    if C[i,0] == 4:
        workers3[i].mantentze = 8
    if C[i,1] == 1:
        workers3[i].komertziala = 5
    if C[i,1] == 2:
        workers3[i].logistika = 5
    if C[i,1] == 3:
        workers3[i].programazioa = 5
    if C[i,1] == 4:
        workers3[i].mantentze = 5
