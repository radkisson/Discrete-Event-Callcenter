import subprocess
import sys
import stats

n = 10

if sys.argv[1] == "1":
    for scriptInstance in range(1):
        with open('results.txt', 'w') as f:
            for i in range(n):
                subprocess.check_call(
                    ['python', 'algoritmo.py'],
                    stdout=f,
                    stderr=subprocess.STDOUT
                )
    # for scriptInstance in range(1):
    #     sys.stdout=open('med.txt','w')
    #     for i in range(n):
    #         subprocess.check_call(['python','algoritmo.py'], \
    #             stdout=sys.stdout, stderr=subprocess.STDOUT)
    # for scriptInstance in range(1):
    #     sys.stdout=open('hi.txt','w')
    #     for i in range(n):
    #         subprocess.check_call(['python','algoritmo.py'], \
    #             stdout=sys.stdout, stderr=subprocess.STDOUT)

if sys.argv[1] == "0":
    Profesionalak, Langutzaileak, Zain, SL, ASA, wait, lan_egin = stats.low(n)
    print("========= N = "+str(n)+" =========")
    print("=========LOW==============")
    print("Profesionalak")
    print(Profesionalak)
    print("Langutzaileak")
    print(Langutzaileak)
    print("Zain")
    print(Zain)
    print("SL")
    print(SL)
    print("ASA")
    print(ASA)
    print("wait")
    print(wait)
    print("lan_egin")
    print(lan_egin)

    Profesionalak, Langutzaileak, Zain, SL, ASA, wait, lan_egin = stats.med(n)
    print("=========MID==============")
    print("Profesionalak")
    print(Profesionalak)
    print("Langutzaileak")
    print(Langutzaileak)
    print("Zain")
    print(Zain)
    print("SL")
    print(SL)
    print("ASA")
    print(ASA)
    print("wait")
    print(wait)
    print("lan egin")
    print(lan_egin)

    Profesionalak, Langutzaileak, Zain, SL, ASA, wait, lan_egin = stats.hi(n)
    print("=========HI==============")
    print("Profesionalak")
    print(Profesionalak)
    print("Langutzaileak")
    print(Langutzaileak)
    print("Zain")
    print(Zain)
    print("SL")
    print(SL)
    print("ASA")
    print(ASA)
    print("wait")
    print(wait)
    print("lan egin")
    print(lan_egin)