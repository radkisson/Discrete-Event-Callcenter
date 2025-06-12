# Discrete-Callcenter

This project lives in the repository `Discrete-Event-Callcenter`.  The name
reflects that a discrete-event approach is used to model call centre
operations.

This repository presents a small-scale discrete-event simulation of a multi-department call centre. The implementation relies only on the Python standard library and NumPy so that the scheduling mechanics remain explicit and easy to follow.

## Queueing Model

For each department, incoming calls follow a Poisson arrival process and the handling time of every call is drawn from an exponential distribution. Inter-arrival times are sampled from ``numpy.random.exponential`` using a rate parameter ``incoming_calls / total_minutes`` per department.  Durations come from another exponential distribution whose mean ``average_call_time`` reflects the expected workload.  The setup corresponds to the well-studied $M/M/c$ queue with a finite team of agents. A Service Level Agreement (SLA) specifies the maximum waiting time permitted before service. The simulator records waiting times and utilisation so that the impact of different load scenarios can be evaluated.

## Simulation Details

The incoming call stream is produced in `data.py` by drawing inter-arrival times from `numpy.random.exponential`, yielding a separate Poisson process for each department. Call durations are sampled from another exponential distribution whose mean reflects the expected workload. These samples become `Call` objects sorted by arrival time.

`worker.py` creates `Agent` objects from predefined *skill matrices*.  Each row
of a matrix describes the primary and, optionally, secondary department for a
worker.  The first column assigns the main department while the second column
indicates where the agent can help when no specialist is free.  During
construction `build_agent_list` sets the skill level of the primary department
to the quality specified in `config.QUALITY` (``8`` by default) and grants a
helper skill of ``5`` in the secondary one.  The remaining columns are kept as
placeholders so the matrices retain a consistent shape.  Three matrices (`A`,
`B` and `C`) ship with the repository, representing different cross-training
scenarios. The `algorithm.run_simulation` function is responsible for
scheduling calls using these agents and computing metrics.

## Event Loop

Calls are processed in chronological order.  For each incoming call the simulator checks whether a specialist of the corresponding department is idle. If none are available it tries helpers instead.  When every agent is busy the call waits in queue until the next worker finishes.  Each worker maintains a schedule of assigned calls so that waiting times and utilisation can be derived after the simulation completes.

This dynamic couples the four departments together. Idle agents with secondary
skills are temporarily reassigned to overloaded queues, helping to balance the
workload across the centre.  The degree of coupling is dictated by the skill
matrices described below.

## Skill Model

Agent skills only influence the order in which workers are selected for a call.
Specialists are always tried first within their department while helpers serve
as a secondary pool.  Call duration and SLA thresholds remain unchanged by the
skill level itself.  To study how this distribution affects performance the
function `algorithm.run_simulation_detailed` returns the average waiting time for
calls handled by specialists and helpers separately.

Throughout the run the simulator records waiting times, utilisation and SLA compliance. Functions in `stats.py` average these results across multiple iterations.

### Skill Matrices

The arrays `A`, `B` and `C` in `data.py` specify how workers are trained across
departments.  Each row represents one agent: the first column stores their main
department and the second column optionally lists another area where they can
assist.  The matrices differ in how strongly departments are coupled—`B`
contains only specialists while `A` and `C` include several cross-trained
helpers.  By editing these matrices you can explore different staffing
strategies.

## Recorded Metrics

Seven key metrics are produced by each simulation run:

* **professionals** – number of calls handled by department specialists
* **helpers** – number of calls handled by cross-department helpers
* **waiting** – count of calls that had to queue before service
* **service level** – share of calls answered within five minutes (configurable)
* **SLA compliance** – proportion of calls solved before their department SLA expires
* **queue share** – fraction of all calls that waited at least once
* **average utilisation** – minutes spent on calls divided by total shift minutes

`algorithm.run_simulation_detailed` additionally reports the average waiting
times for calls served by specialists versus helpers.

## Repository Layout

* `data.py` generates arrival patterns and call durations using NumPy routines.
* `call.py` defines the `Call` class and builds the sequence of incoming calls.
* `worker.py` constructs the agent pools and tracks their schedules.
* `filter.py` provides helper functions for assigning calls to suitable agents.
* `stats.py` aggregates raw results into average metrics.

Variable names originate from an earlier prototype that used Euskera terms. They have been kept for compatibility, but comments now explain their purpose in English.

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

