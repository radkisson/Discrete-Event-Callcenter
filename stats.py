"""Utilities for computing statistics from simulation results."""

from typing import Iterable, List, Sequence


def load_results(filename: str = "results.txt") -> List[float]:
    """Return all numeric values stored in ``filename``.

    Each line of the file must contain a single number. Blank lines are ignored.
    """
    with open(filename, "r") as fh:
        return [float(line.strip()) for line in fh if line.strip()]


def _compute_stats(data: Sequence[float], offset: int) -> tuple:
    """Compute aggregated statistics starting at ``offset``.

    ``data`` must contain groups of 21 consecutive numbers. Each group
    represents results for the low, medium and high scenarios in that order.
    ``offset`` should be 0 for low, 7 for medium and 14 for high.
    """
    if len(data) % 21 != 0:
        raise ValueError("Results data length must be a multiple of 21")

    runs = len(data) // 21
    metrics = [0.0] * 7
    for run in range(runs):
        base = run * 21 + offset
        for i in range(7):
            metrics[i] += data[base + i]
    return tuple(value / runs for value in metrics)


def low(n: int | None = None, data: Iterable[float] | None = None) -> tuple:
    """Return average statistics for the low scenario.

    ``n`` is ignored and kept for backwards compatibility.  ``data`` may be
    provided to avoid reloading the file multiple times.
    """
    if data is None:
        data = load_results()
    return _compute_stats(list(data), 0)


def med(n: int | None = None, data: Iterable[float] | None = None) -> tuple:
    """Return average statistics for the medium scenario."""
    if data is None:
        data = load_results()
    return _compute_stats(list(data), 7)


def hi(n: int | None = None, data: Iterable[float] | None = None) -> tuple:
    """Return average statistics for the high scenario."""
    if data is None:
        data = load_results()
    return _compute_stats(list(data), 14)

