import os
import sys
import types
from importlib import reload

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Provide a lightweight fake data module so worker can be imported without numpy
class DummyMatrix:
    def __getitem__(self, idx):
        return 0

dummy_data = types.SimpleNamespace(
    team_size=[],
    A=DummyMatrix(),
    B=DummyMatrix(),
    C=DummyMatrix(),
    tSLA=[],
    call_input_list=[],
)
sys.modules['data'] = dummy_data

import worker
import main
import algoritmo


def test_build_worker_list_custom_counts():
    counts = [2, 1]
    import numpy as np
    matrix = np.zeros((sum(counts), 2))
    workers = worker.build_worker_list(matrix, team_size=counts)
    assert len(workers) == 3
    assert sum(1 for w in workers if w.department == 0) == 2
    assert sum(1 for w in workers if w.department == 1) == 1


def test_cli_workers_from_env(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("WORKER_COUNTS", "1,1,1,1")
    monkeypatch.setattr(algoritmo, "run_simulation", lambda *a, **k: (0,0,0,0,0,0,0))
    monkeypatch.setattr(sys, "argv", ["main.py", "--simulate", "--workers-from-env"])

    reload(main)
    main.main()

    assert (tmp_path / "results.txt").exists()
