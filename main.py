"""Command line interface for running simulations and displaying statistics."""

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
        help="Load worker counts from environment variables",
    )
    parser.add_argument(
        "--env-file",
        default=".env",
        help="Path to environment file used with --workers-from-env",
    )
    args = parser.parse_args()

    n = 10

    if args.simulate:
        custom_workers = None
        if args.workers_from_env:
            load_dotenv(dotenv_path=os.path.join(os.getcwd(), args.env_file))
            team_size = [
                int(os.getenv("SALES_WORKERS", 0)),
                int(os.getenv("LOGISTICS_WORKERS", 0)),
                int(os.getenv("PROGRAMMING_WORKERS", 0)),
                int(os.getenv("MAINTENANCE_WORKERS", 0)),
            ]
            quality = [
                int(os.getenv("SALES_QUALITY", 8)),
                int(os.getenv("LOGISTICS_QUALITY", 8)),
                int(os.getenv("PROGRAMMING_QUALITY", 8)),
                int(os.getenv("MAINTENANCE_QUALITY", 8)),
            ]
            from worker import build_worker_list
            import data

            custom_workers = build_worker_list(data.A, team_size, quality)

        with open("results.txt", "w") as f:
            for _ in range(n):
                result = algoritmo.run_simulation(workers=custom_workers)
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

