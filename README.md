# Discrete-Callcenter

This repository presents a small-scale discrete-event simulation of a multi-department call centre. The implementation relies only on the Python standard library and NumPy so that the scheduling mechanics remain explicit and easy to follow.

## Queueing Model

For each department, incoming calls follow a Poisson arrival process and the handling time of every call is drawn from an exponential distribution. This configuration corresponds to the well-studied $M/M/c$ queue with a finite team of agents. A Service Level Agreement (SLA) specifies the maximum waiting time permitted before service. The simulator records waiting times and utilisation so that the impact of different load scenarios can be evaluated.

## Simulation Details

The incoming call stream is produced in `data.py` by drawing inter-arrival times from `numpy.random.exponential`, yielding a separate Poisson process for each department. Call durations are sampled from another exponential distribution whose mean reflects the expected workload. These samples become `Call` objects sorted by arrival time.

`worker.py` creates `Agent` objects from predefined skill matrices. Specialists carry a skill level of 8 while helpers range from 5 to 7. The event loop in `algorithm.run_simulation` iterates over the calls, first looking for an idle specialist in the appropriate department and then falling back to helpers. If no agent is available the call waits in queue until the next agent finishes.

## Skill Model

Agent skills only influence the order in which workers are selected for a call.
Specialists are always tried first within their department while helpers serve
as a secondary pool.  Call duration and SLA thresholds remain unchanged by the
skill level itself.  To study how this distribution affects performance the
function `algorithm.run_simulation_detailed` returns the average waiting time for
calls handled by specialists and helpers separately.

Throughout the run the simulator records waiting times, utilisation and SLA compliance. Functions in `stats.py` average these results across multiple iterations.

## Repository Layout

* `data.py` generates arrival patterns and call durations using NumPy routines.
* `call.py` defines the `Call` class and builds the sequence of incoming calls.
* `worker.py` constructs the agent pools and tracks their schedules.
* `filter.py` provides helper functions for assigning calls to suitable agents.
* `stats.py` aggregates raw results into average metrics.

Earlier versions used very short names (``A``, ``B``, ``C``, ``tSLA``) for the skill matrices and SLA thresholds. These have been renamed to ``skill_matrix_a``, ``skill_matrix_b``, ``skill_matrix_c`` and ``sla_targets`` for clarity. The old identifiers remain available as aliases so existing code continues to run.

## Requirements

* Python 3.8 or higher
* Install the dependencies with `pip install -r requirements.txt`
* Optional: set agent counts and quality in a `.env` file when using `--agents-from-env`
  (use `--env-file PATH` to load a different file)

## Command Line Interface

Run `python main.py --help` to display all available options:

```text
usage: main.py [-h] (--simulate | --stats) [--agents-from-env]
               [--env-file ENV_FILE]

options:
  -h, --help           show this help message and exit
  --simulate           Run the simulation
  --stats              Show statistics
  --agents-from-env    Load agent counts from environment variables
  --env-file ENV_FILE  Path to environment file used with --agents-from-env
```

`--simulate` and `--stats` are mutually exclusive. Use `--simulate` to
generate a `results.txt` file. To load agent counts from environment
variables, add `--agents-from-env` and optionally provide `--env-file`.

## Running the Simulation

To generate a `results.txt` file containing statistics for ten simulation runs:

```bash
python main.py --simulate
```

The command above overwrites any existing `results.txt` in the working directory.
For a more granular view run ``algorithm.run_simulation_detailed()`` from a
Python shell. This variant includes the average waiting time for calls handled
by specialists and helpers, allowing you to gauge how the skill distribution
impacts the queue.

To read agent counts from environment variables defined in a `.env` file use:

```bash
python main.py --simulate --agents-from-env
```

To load settings from a different file pass the path using `--env-file`:

```bash
python main.py --simulate --agents-from-env --env-file custom.env
```

The following variables are recognised:

* `SALES_WORKERS`
* `SALES_QUALITY`
* `LOGISTICS_WORKERS`
* `LOGISTICS_QUALITY`
* `PROGRAMMING_WORKERS`
* `PROGRAMMING_QUALITY`
* `MAINTENANCE_WORKERS`
* `MAINTENANCE_QUALITY`

Quality values express the primary skill level for each department on a
scale from 1 (novice) to 10 (expert). A level of 8 or higher designates a
specialist agent. When a specialist assists another department their skill
in that area defaults to 5.

An example configuration is provided in [`.env.example`](./.env.example).

## Analysing Results

Once a `results.txt` file is available you can compute summary statistics:

```bash
python main.py --stats
```

This command prints aggregated metrics for low, medium and high demand scenarios. The repository ships with a minimal `results.txt` so that the automated tests run successfully.

## Testing

Run the unit tests with:

```bash
PYTHONPATH=. pytest -q
```

