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

## Running the Simulation

To generate a `results.txt` file containing statistics for ten simulation runs:

```bash
python main.py --simulate
```

The command above overwrites any existing `results.txt` in the working directory.

### Loading worker counts from environment variables

You can override the number of workers per department by supplying the
`--workers-from-env` flag together with a `WORKER_COUNTS` variable in a
`.env` file. The value is a comma separated list of integers. For example:

```bash
echo "WORKER_COUNTS=5,3,4,3" > .env
python main.py --simulate --workers-from-env
```

A sample `.env.example` file is included in the repository. Copy it to `.env`
and adjust the numbers to match your scenario.

This mechanism allows specifying between one and four worker categories.

## Analysing Results

Once a `results.txt` file is available you can compute summary statistics:

```bash
python main.py --stats
```

This command prints aggregated metrics for low, medium and high demand scenarios. The repository ships with a minimal `results.txt` so that the automated tests run successfully.

## Using the Modules

The simulation logic lives in `algoritmo.py` and can be reused from your own
scripts. For example:

```python
from algoritmo import run_simulation
from call import calls
from worker import workers

metrics = run_simulation(calls, workers)
print(metrics)
```

Each invocation returns a tuple with the number of professionals and helpers,
the count of queued calls and several service metrics.

## Testing

Run the unit tests with:

```bash
PYTHONPATH=. pytest -q
```

