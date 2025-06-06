from call import calls
from filter import (
    first_level,
    second_level,
    sort_by_work_time,
    first_level2,
    second_level2,
    sort_by_work_time2,
    first_level3,
    second_level3,
    sort_by_work_time3,
)
from worker import workers, workers2, workers3
from data import tSLA, team_size  # Imported data

professionals = 0
helpers = 0
waiting = 0  # Counters to track call handling statistics

for k in range(len(calls)):
    call_item = calls[k]
    mota = call_item.departamentua + 1  # departments are 1-indexed
    lehenengo_langileak = first_level(mota)  # specialized agents
    lehenengo_langileak = sort_by_work_time(lehenengo_langileak)
    bigarren_langileak = second_level(mota)  # helper agents
    bigarren_langileak = sort_by_work_time(bigarren_langileak)
    atendituak = 0
    for i in range(len(lehenengo_langileak)):
        if lehenengo_langileak[i].libre(call_item) == 1:
            lehenengo_langileak[i].ordutegia.append(call_item)
            lehenengo_langileak[i].ordutegia[-1].denbora = call_item.ordua
            atendituak = 1
            professionals = professionals + 1
            break  #Programa bukatuko da hurrengo deia iritsi arte
        else: #Ez badago agente espezializaturik libre
            continue
    if atendituak == 0:
        for i in range(len(bigarren_langileak)):
            if bigarren_langileak[i].libre(call_item) == 1:
                bigarren_langileak[i].ordutegia.append(call_item)
                bigarren_langileak[i].ordutegia[-1].denbora = call_item.ordua
                atendituak = 1
                helpers = helpers + 1
                break  #Programa bukatuko da hurrengo deia iritsi arte
            else: #Ez dago agenterik libre eta deiak kolan itxarongo du
                continue
    if atendituak == 1:
        continue
    if atendituak == 0:  #Deia kolan dago itxaroten
        concat = []
        for i in range(len(lehenengo_langileak)):
            concat.append(lehenengo_langileak[i])
        for j in range(len(bigarren_langileak)):
            concat.append(bigarren_langileak[j])
        concat = sort_by_work_time(concat)
        waiting = waiting + 1
        call_item.denbora = concat[0].noizlibre()
        concat[0].ordutegia.append(call_item)
        
print(professionals)
print(helpers)
print(waiting)

def SL():  #Ikusiko dugu zenbat deik kolan 5 minutu baino gutxiago itxaroten duten
    ekitaldiak = 0 
    for i in range(len(calls)):
        if calls[i].wait_time() < 5:
            ekitaldiak = ekitaldiak + 1
    return ekitaldiak / len(calls)

def ASA(): # Ikusiko dugu deien artean zenbatek SLA baina denbora gehiago behar izan duten deia soluzionatzeko
    ekitaldiak = 0 
    for i in range(len(calls)):
        j = int(calls[i].departamentua)
        if calls[i].denbora + calls[i].iraupena - calls[i].ordua < tSLA[j]:
            ekitaldiak = ekitaldiak + 1
    return ekitaldiak / len(calls)

def INVASA():
    return 1-ASA() 

def p_wait_queue(): #Ikusiko dugu zenbat deik itxaron behar izan duten kolan
    ekitaldiak = 0    
    for i in range(len(calls)):
        if calls[i].wait_time() > 0:
            ekitaldiak = ekitaldiak + 1
    return ekitaldiak / len(calls)

def lan_egin_batezbesteko():  # Average worker utilisation
    lan_egin = 0
    for zenbatu in range(len(workers)):
        lan_egin = lan_egin + workers[zenbatu].landenbora()
    lan_egin = lan_egin / (len(workers) * 8 * 60)
    return lan_egin

print('{}'.format(SL()))
print('{}'.format(ASA()))
print('{}'.format(p_wait_queue()))
print('{}'.format(lan_egin_batezbesteko()))
