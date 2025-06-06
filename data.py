
import numpy as np
import numpy.random as rnd #numpy paketea kargatuko dugu, ausazko zenbakiak sortzeko erabiliko dugu
import helpers

# AGENTE GAITASUN matrizeak definituko dugu

# k1 = [8, 6, 2, 1]
# k2 = [8, 2, 6, 2]
# k3 = [8, 2, 1, 1]
# k4 = [8, 2, 1, 1]
# k5 = [8, 1, 2, 2]
# l1 = [2, 8, 2, 6]
# l2 = [6, 8, 1, 2]
# l3 = [1, 8, 1, 1]
# I1 = [6, 1, 8, 2]
# I2 = [1, 2, 8, 6]
# I3 = [2, 2, 8, 1]
# I4 = [1, 2, 8, 1]
# m1 = [2, 2, 6, 8]
# m2 = [2, 6, 2, 8]
# m3 = [1, 2, 2, 8]

# k11 = [8, 2, 2, 1]
# k21 = [8, 2, 1, 2]
# k31 = [8, 2, 1, 1]
# k41 = [8, 2, 1, 1]
# k51 = [8, 1, 2, 2]
# l11 = [2, 8, 2, 2]
# l21 = [1, 8, 1, 2]
# l31 = [1, 8, 1, 1]
# I11 = [1, 1, 8, 2]
# I21 = [1, 2, 8, 1]
# I31 = [2, 2, 8, 1]
# I41 = [1, 2, 8, 1]
# m11 = [2, 2, 1, 8]
# m21 = [2, 1, 2, 8]
# m31 = [1, 2, 2, 8]

# k12 = [8, 2, 6, 1]
# k22 = [8, 3, 1, 6]
# k32 = [8, 6, 1, 1]
# k42 = [8, 2, 1, 1]
# k52 = [8, 1, 2, 2]
# l12 = [2, 8, 2, 6]
# l22 = [5, 8, 1, 2]
# l32 = [1, 8, 6, 1]
# I12 = [1, 6, 8, 2]
# I22 = [6, 2, 8, 1]
# I32 = [2, 2, 8, 6]
# I42 = [1, 2, 8, 1]
# m12 = [2, 2, 6, 8]
# m22 = [5, 1, 2, 8]
# m32 = [1, 6, 2, 8]


team_size = np.array([5, 3, 4, 3])  # Number of workers per department
ordutarte = 8 #Lanordua
minutukopuru = ordutarte*60 #Lan egin beharreko denbora minutuetan
proportzio = np.array([.35,.18,.25,.22]) #Departamentu bakoitzaren proportzioa
maxdeikopuru = [200,180,270,110] # Departamentu bakoitzeko dei kopuru maximoa
tSLA = np.array([18.0,12.0,10.0,25.0]) #SLA departamentu bakoitzeko
deikopuru = np.array([180,160,250,95]) # Departamentu bakoitzera iristen diren deiak

A = np.hstack([np.array([1,2,1,3,1,0,1,0,1,0,2,4,2,1,2,0,3,1,3,4,3,0,3,0,4,3,4,2,4,0]).reshape(15,2),np.zeros([15,2])])
B = np.hstack([np.array([1,0,1,0,1,0,1,0,1,0,2,0,2,0,2,0,3,0,3,0,3,0,3,0,4,0,4,0,4,0]).reshape(15,2),np.zeros([15,2])])
C =  np.hstack([np.array([1,2,1,3,1,0,1,0,1,0,2,4,2,1,2,0,3,1,3,4,3,0,3,0,4,3,4,2,4,0]).reshape(15,2),np.zeros([15,2])])

langileekguztira = team_size.sum()  # Total number of workers
lanminututalde = minutukopuru * team_size  # Work minutes per department
lanminutes = lanminututalde.sum() #Guztira egin beharreko lan kopurua minutuetan
minutuzama = proportzio*lanminutes #Departamentu bakoitzak lan egin beharreko denbora minutuetan proportzioa kontutan hartuz
deidenbora = [minutuzama[i]*pow(maxdeikopuru[i],-1) for i in range(4)]  #Dei bakoitzeko, departamentu bakoitzak duen denbora atenditzeko
sarreratasa = deikopuru/minutukopuru  # Departamentu bakoitzean minutuko iristen diren dei kopurua

deisarrera   = np.array([rnd.exponential(1/sarreratasa[i],deikopuru[i]) for i in range(4)])  # Ausazko zenbakiak sortuko ditugu iristen diren deien ordutegia sortzeko
deizerrenda  = np.array([ np.array([deisarrera[j][0:i].sum() for i in range(maxdeikopuru[j])]) for j in range(4)])  # Kalkulatutako ausazko zenbakiekin dei bakoitza iritsi den ordutegia zehaztuko dugu
deisarrera2   = np.array([rnd.exponential(deidenbora[i],deikopuru[i]) for i in range(4)])  # Ausazko zenbakiak sortuko ditugu iritsitako deien iraupena sortzeko
deizerrenda2  = np.array([ np.array([deisarrera2[j][0:i].sum() for i in range(maxdeikopuru[j])]) for j in range(4)])

# DEPARTAMENTU BAKOITZEKO IRISTEN DIREN DEIEN MATRIZEA(ORDUTEGIA, IRAUPENA, MOTA, SlA)

deisarreraguztia  = np.array(
    [np.array([ np.array([deizerrenda[i][j],deisarrera2[i][j],i,tSLA[i]]) for j in range(deikopuru[i])]) for i in range(4)]
)

# SLA beteko ez duten deien proportzioa, nahiz eta oso azkar atendituak izan (konponketa denbora > SLA)

overSLA = np.zeros(4) #Lista hutsa sortuko dugu

for group in range(4):
    zenbakia_deiak_gorako = 0
    for deiak_i in range(deikopuru[group]):
        if deisarreraguztia[group][deiak_i][1] > deisarreraguztia[group][deiak_i][3]:
            zenbakia_deiak_gorako = zenbakia_deiak_gorako + 1
    overSLA[group] = zenbakia_deiak_gorako/maxdeikopuru[group] # Kalkulatuko dugu departamentu bakoitzean zenbat deik SLA pasako duten nahiz eta momentuan atendituak diren.


matrizea = np.concatenate((deisarreraguztia[0],deisarreraguztia[1],deisarreraguztia[2],deisarreraguztia[3]),axis=0) # Orain arte sortu ditugun matrizeak batera jarriko ditugu

call_input_list = np.sort(
    matrizea.view("float,float,float,float"), order=["f0"], axis=0
)  # Sorted call matrix by arrival time
