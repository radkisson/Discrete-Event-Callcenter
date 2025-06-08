import os
import sys
import subprocess
from pathlib import Path
import types
import importlib


ROOT = Path(__file__).resolve().parents[1]


def test_build_agent_list_respects_env(monkeypatch):
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
    agents = worker.build_agent_list(matrix, team_size)
    counts = [0, 0, 0, 0]
    for w in agents:
        counts[w.department] += 1
    assert counts == team_size


def test_build_agent_list_respects_quality(monkeypatch):
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

    team_size = [1, 1, 1, 1]
    matrix = np.array([[1, 0], [2, 0], [3, 0], [4, 0]])
    quality = [9, 7, 5, 6]
    agents = worker.build_agent_list(matrix, team_size, quality)
    skills = [w.skill_for(i + 1) for i, w in enumerate(agents)]
    assert skills == quality


def test_cli_simulation_from_env(tmp_path):
    env = tmp_path / 'custom.env'
    env.write_text(
        'SALES_WORKERS=5\nSALES_QUALITY=8\n'
        'LOGISTICS_WORKERS=3\nLOGISTICS_QUALITY=8\n'
        'PROGRAMMING_WORKERS=4\nPROGRAMMING_QUALITY=8\n'
        'MAINTENANCE_WORKERS=3\nMAINTENANCE_QUALITY=8\n'
    )
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / 'main.py'),
            '--simulate',
            '--agents-from-env',
            '--env-file',
            str(env),
        ],
        cwd=tmp_path,
        check=True,
    )
    assert (tmp_path / 'results.txt').exists()


def test_cli_simulation_from_default_env(tmp_path):
    env = tmp_path / '.env'
    env.write_text(
        'SALES_WORKERS=2\nSALES_QUALITY=6\n'
        'LOGISTICS_WORKERS=2\nLOGISTICS_QUALITY=6\n'
        'PROGRAMMING_WORKERS=2\nPROGRAMMING_QUALITY=6\n'
        'MAINTENANCE_WORKERS=2\nMAINTENANCE_QUALITY=6\n'
    )
    result = subprocess.run(
        [sys.executable, str(ROOT / 'main.py'), '--simulate', '--agents-from-env'],
        cwd=tmp_path,
        check=True,
    )
    assert (tmp_path / 'results.txt').exists()
