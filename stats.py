def low(n):
    with open('results.txt', 'r') as f:
        count = 0
        professionals = 0
        for line in f:
            if count % 21 == 0: #this is the remainder operator
                line = line.strip('\n')
                professionals = professionals + float(line)
            count+=1
        professionals = professionals / n

    with open('results.txt', 'r') as f:
        count = 0
        L = 0
        for line in f:
            if count % 21 == 1: #this is the remainder operator
                line = line.strip('\n')
                L = L + float(line)
            count+=1
        helpers = L / n

    with open('results.txt', 'r') as f:
        count = 0
        waiting = 0
        for line in f:
            if count % 21 == 2:  # this is the remainder operator
                line = line.strip('\n')
                waiting = waiting + float(line)
            count+=1
        waiting = waiting / n

    with open('results.txt', 'r') as f:
        count = 0
        SL = 0
        for line in f:
            if count % 21 == 3: #this is the remainder operator
                line = line.strip('\n')
                SL = SL + float(line)
            count+=1
        SL = SL/n

    with open('results.txt', 'r') as f:
        count = 0
        ASA = 0
        for line in f:
            if count % 21 == 4: #this is the remainder operator
                line = line.strip('\n')
                ASA = ASA + float(line)
            count+=1
        ASA = ASA/n

    with open('results.txt', 'r') as f:
        count = 0
        wait = 0
        for line in f:
            if count % 21 == 5: #this is the remainder operator
                line = line.strip('\n')
                wait = wait + float(line)
            count+=1
        wait = wait/n

    with open('results.txt', 'r') as f:
        count = 0
        work_done = 0
        for line in f:
            if count % 21 == 6: #this is the remainder operator
                line = line.strip('\n')
                work_done = work_done + float(line)
            count+=1
        work_done = work_done/n
    
    return professionals, helpers, waiting, SL, ASA, wait, work_done

def med(n):
    with open('results.txt', 'r') as f:
        count = 0
        professionals = 0
        for line in f:
            if count % 21 == 7: #this is the remainder operator
                line = line.strip('\n')
                professionals = professionals + float(line)
            count+=1
        professionals = professionals/n

    with open('results.txt', 'r') as f:
        count = 0
        L = 0
        for line in f:
            if count % 21 == 8: #this is the remainder operator
                line = line.strip('\n')
                L = L + float(line)
            count+=1
        helpers = L/n

    with open('results.txt', 'r') as f:
        count = 0
        waiting = 0
        for line in f:
            if count % 21 == 9: #this is the remainder operator
                line = line.strip('\n')
                waiting = waiting + float(line)
            count+=1
        waiting = waiting/n

    with open('results.txt', 'r') as f:
        count = 0
        SL = 0
        for line in f:
            if count % 21 == 10: #this is the remainder operator
                line = line.strip('\n')
                SL = SL + float(line)
            count+=1
        SL = SL/n

    with open('results.txt', 'r') as f:
        count = 0
        ASA = 0
        for line in f:
            if count % 21 == 11: #this is the remainder operator
                line = line.strip('\n')
                ASA = ASA + float(line)
            count+=1
        ASA = ASA/n

    with open('results.txt', 'r') as f:
        count = 0
        wait = 0
        for line in f:
            if count % 21 == 12: #this is the remainder operator
                line = line.strip('\n')
                wait = wait + float(line)
            count+=1
        wait = wait/n

    with open('results.txt', 'r') as f:
        count = 0
        work_done = 0
        for line in f:
            if count % 21 == 13: #this is the remainder operator
                line = line.strip('\n')
                work_done = work_done + float(line)
            count+=1
        work_done = work_done/n
    
    return professionals, helpers, waiting, SL, ASA, wait, work_done

def hi(n):
    with open('results.txt', 'r') as f:
        count = 0
        professionals = 0
        for line in f:
            if count % 21 == 14: #this is the remainder operator
                line = line.strip('\n')
                professionals = professionals + float(line)
            count+=1
        professionals = professionals/n

    with open('results.txt', 'r') as f:
        count = 0
        L = 0
        for line in f:
            if count % 21 == 15: #this is the remainder operator
                line = line.strip('\n')
                L = L + float(line)
            count+=1
        helpers = L/n

    with open('results.txt', 'r') as f:
        count = 0
        waiting = 0
        for line in f:
            if count % 21 == 16: #this is the remainder operator
                line = line.strip('\n')
                waiting = waiting + float(line)
            count+=1
        waiting = waiting/n

    with open('results.txt', 'r') as f:
        count = 0
        SL = 0
        for line in f:
            if count % 21 == 17: #this is the remainder operator
                line = line.strip('\n')
                SL = SL + float(line)
            count+=1
        SL = SL/n

    with open('results.txt', 'r') as f:
        count = 0
        ASA = 0
        for line in f:
            if count % 21 == 18: #this is the remainder operator
                line = line.strip('\n')
                ASA = ASA + float(line)
            count+=1
        ASA = ASA/n

    with open('results.txt', 'r') as f:
        count = 0
        wait = 0
        for line in f:
            if count % 21 == 19: #this is the remainder operator
                line = line.strip('\n')
                wait = wait + float(line)
            count+=1
        wait = wait/n

    with open('results.txt', 'r') as f:
        count = 0
        work_done = 0
        for line in f:
            if count % 21 == 20: #this is the remainder operator
                line = line.strip('\n')
                work_done = work_done + float(line)
            count+=1
        work_done = work_done/n
    
    return professionals, helpers, waiting, SL, ASA, wait, work_done
