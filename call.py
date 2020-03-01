from data import deisarrerazerrenda

# DEIAK OBJETU BEZALA DEFINITUKO DITUGU 

class Deiak:

    def __init__(self, ordua, iraupena, departamentua, sla):
        self.ordua          =  ordua # Dei bakoitza iristen den denbora minutuetan
        self.iraupena       =  iraupena # Dei bakoitzaren iraupena minutuetan
        self.departamentua  =  departamentua # Dei bakoitzaren departamentua
        self.sla            =  sla # Dei bakoitzaren SLA
        self.denbora        =  0 #Dei bakoitza atenditua den momentua (1. Deia iristen den momentuan hartuko dugu)
    
    def delta_t(self):  # Kolan egondako denbora kalkulatuko dugu:
        delta  =  self.denbora - self.ordua # Deia atenditu duten momentua- deia iritsi den momentua
        return delta
    
#Matrize bat sortuko dugu dei bakoitzaren informazioa gordez    
deiak2 = [Deiak(deisarrerazerrenda[i][0][0],deisarrerazerrenda[i][0][1],deisarrerazerrenda[i][0][2],deisarrerazerrenda[i][0][3]) for i in range(len(deisarrerazerrenda))]