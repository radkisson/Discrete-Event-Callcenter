import argparse
import subprocess
import stats


def main():
    parser = argparse.ArgumentParser(description="Discrete call-center simulation")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simulate", action="store_true", help="Run the simulation")
    mode.add_argument("--stats", action="store_true", help="Show statistics")
    args = parser.parse_args()

    n = 10

    if args.simulate:
        for _ in range(1):
            with open("results.txt", "w") as f:
                for _ in range(n):
                    subprocess.check_call([
                        "python",
                        "algoritmo.py",
                    ], stdout=f, stderr=subprocess.STDOUT)
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

    elif args.stats:
        professionals, helpers, waiting, SL, ASA, wait, work_done = stats.low(n)
        print("========= N = " + str(n) + " =========")
        print("=========LOW==============")
        print("Professionals")
        print(professionals)
        print("Helpers")
        print(helpers)
        print("Waiting")
        print(waiting)
        print("SL")
        print(SL)
        print("ASA")
        print(ASA)
        print("wait")
        print(wait)
        print("work_done")
        print(work_done)

        professionals, helpers, waiting, SL, ASA, wait, work_done = stats.med(n)
        print("=========MID==============")
        print("Professionals")
        print(professionals)
        print("Helpers")
        print(helpers)
        print("Waiting")
        print(waiting)
        print("SL")
        print(SL)
        print("ASA")
        print(ASA)
        print("wait")
        print(wait)
        print("work_done")
        print(work_done)

        professionals, helpers, waiting, SL, ASA, wait, work_done = stats.hi(n)
        print("=========HI==============")
        print("Professionals")
        print(professionals)
        print("Helpers")
        print(helpers)
        print("Waiting")
        print(waiting)
        print("SL")
        print(SL)
        print("ASA")
        print(ASA)
        print("wait")
        print(wait)
        print("work_done")
        print(work_done)


if __name__ == "__main__":
    main()

