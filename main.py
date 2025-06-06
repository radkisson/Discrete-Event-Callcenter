import argparse
import os
from dotenv import load_dotenv

import algoritmo
import stats


def main():
    """Entry point for the command line interface.

    Run ``python main.py --simulate`` to execute the simulation and store the
    raw metrics in ``results.txt``.  Use ``python main.py --stats`` to read the
    file and display aggregated statistics for the low, medium and high demand
    scenarios.
    """
    parser = argparse.ArgumentParser(description="Discrete call-center simulation")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simulate", action="store_true", help="Run the simulation")
    mode.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument(
        "--workers-from-env",
        action="store_true",
        help="Load worker counts from a .env file via WORKER_COUNTS",
    )
    args = parser.parse_args()

    n = 10

    if args.simulate:
        team_size = None
        if args.workers_from_env:
            load_dotenv()
            counts = os.getenv("WORKER_COUNTS")
            if counts:
                team_size = [int(x) for x in counts.split(',') if x.strip()]

        with open("results.txt", "w") as f:
            for _ in range(n):
                if team_size is not None:
                    from worker import build_worker_list, A
                    import data

                    workers = build_worker_list(A, team_size=team_size)
                    result = algoritmo.run_simulation(workers=workers, sla=data.tSLA)
                else:
                    result = algoritmo.run_simulation()

                for value in result:
                    f.write(f"{value}\n")

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

