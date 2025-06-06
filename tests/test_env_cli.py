import os
import sys
import subprocess
from pathlib import Path
import types
import importlib


ROOT = Path(__file__).resolve().parents[1]


def test_build_worker_list_respects_env(monkeypatch):
    dummy = types.SimpleNamespace(
        tSLA=[0, 0, 0, 0],
        team_size=[],
        A=None,
        B=None,
        C=None,
        call_input_list=[],
    )
    monkeypatch.setitem(sys.modules, 'data', dummy)
    import worker
    import numpy as np
    import importlib
    worker = importlib.reload(worker)

    team_size = [1, 2, 3, 4]
    matrix = np.zeros((sum(team_size), 2))
    workers = worker.build_worker_list(matrix, team_size)
    counts = [0, 0, 0, 0]
    for w in workers:
        counts[w.department] += 1
    assert counts == team_size


def test_cli_simulation_from_env(tmp_path):
    env = tmp_path / '.env'
    env.write_text(
        'SALES_WORKERS=5\nLOGISTICS_WORKERS=3\nPROGRAMMING_WORKERS=4\nMAINTENANCE_WORKERS=3\n'
    )
    result = subprocess.run(
        [sys.executable, str(ROOT / 'main.py'), '--simulate', '--workers-from-env'],
        cwd=tmp_path,
        check=True,
    )
    assert (tmp_path / 'results.txt').exists()
