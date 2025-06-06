# Discrete-Callcenter

This repository presents a small-scale discrete-event simulation of a multi-department call centre. The implementation relies only on the Python standard library and NumPy so that the scheduling mechanics remain explicit and easy to follow.

## Queueing Model

For each department, incoming calls follow a Poisson arrival process and the handling time of every call is drawn from an exponential distribution. This configuration corresponds to the well-studied $M/M/c$ queue with a finite team of agents. A Service Level Agreement (SLA) specifies the maximum waiting time permitted before service. The simulator records waiting times and utilisation so that the impact of different load scenarios can be evaluated.

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
* Optional: set worker counts in a `.env` file when using `--workers-from-env`

## Running the Simulation

To generate a `results.txt` file containing statistics for ten simulation runs:

```bash
python main.py --simulate
```

The command above overwrites any existing `results.txt` in the working directory.

To read worker counts from environment variables defined in a `.env` file use:

```bash
python main.py --simulate --workers-from-env
```

The following variables are recognised:

* `SALES_WORKERS`
* `LOGISTICS_WORKERS`
* `PROGRAMMING_WORKERS`
* `MAINTENANCE_WORKERS`

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

