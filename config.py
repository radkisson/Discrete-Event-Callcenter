from __future__ import annotations

import os
from pathlib import Path
from dotenv import load_dotenv


_DEFAULT_TEAM = [5, 3, 4, 3]
_DEFAULT_QUALITY = [8, 8, 8, 8]


def load(env_file: str = '.env') -> tuple[list[int], list[int]]:
    """Return team size and quality levels from ``env_file`` if present."""
    if Path(env_file).exists():
        load_dotenv(env_file)
    team_size = [
        int(os.getenv('SALES_WORKERS', _DEFAULT_TEAM[0])),
        int(os.getenv('LOGISTICS_WORKERS', _DEFAULT_TEAM[1])),
        int(os.getenv('PROGRAMMING_WORKERS', _DEFAULT_TEAM[2])),
        int(os.getenv('MAINTENANCE_WORKERS', _DEFAULT_TEAM[3])),
    ]
    quality = [
        int(os.getenv('SALES_QUALITY', _DEFAULT_QUALITY[0])),
        int(os.getenv('LOGISTICS_QUALITY', _DEFAULT_QUALITY[1])),
        int(os.getenv('PROGRAMMING_QUALITY', _DEFAULT_QUALITY[2])),
        int(os.getenv('MAINTENANCE_QUALITY', _DEFAULT_QUALITY[3])),
    ]
    return team_size, quality


TEAM_SIZE, QUALITY = load()
