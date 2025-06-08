"""Command line interface for running simulations and displaying statistics."""

import argparse
import os

from dotenv import load_dotenv

import algorithm
import stats


METRIC_LABELS = [
    "Professionals",
    "Helpers",
    "Waiting",
    "Service Level",
    "SLA Compliance",
    "Queue Share",
    "Utilisation",
]


def _load_agents_from_env(env_file: str):
    """Return custom agents defined by environment variables."""

    load_dotenv(dotenv_path=os.path.join(os.getcwd(), env_file))
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
    from worker import build_agent_list
    import data

    return build_agent_list(data.A, team_size, quality)


def _write_results(runs: int, agents=None, filename: str = "results.txt") -> None:
    """Run the simulation ``runs`` times and store metrics in ``filename``."""

    with open(filename, "w") as fh:
        for _ in range(runs):
            result = algorithm.run_simulation(agents=agents)
            for value in result:
                fh.write(f"{value}\n")


def _print_block(title: str, metrics: tuple) -> None:
    print(f"========={title}==============")
    for label, value in zip(METRIC_LABELS, metrics):
        print(label)
        print(value)


def _show_stats(runs: int) -> None:
    print(f"========= N = {runs} =========")
    _print_block("LOW", stats.low(runs))
    _print_block("MID", stats.med(runs))
    _print_block("HI", stats.hi(runs))


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
        "--agents-from-env",
        action="store_true",
        help="Load agent counts from environment variables",
    )
    parser.add_argument(
        "--env-file",
        default=".env",
        help="Path to environment file used with --agents-from-env",
    )
    args = parser.parse_args()

    n = 10

    if args.simulate:
        agents = None
        if args.agents_from_env:
            agents = _load_agents_from_env(args.env_file)

        _write_results(n, agents)

    elif args.stats:
        _show_stats(n)


if __name__ == "__main__":
    main()

