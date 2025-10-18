from typing import Dict

def deltas(current: Dict, baseline: Dict) -> Dict:
    out = {}
    for k, v in current.items():
        if k in baseline:
            out[k] = round(v - baseline[k], 3)
    return out

def color_flag(delta: float, soft=5.0, hard=10.0) -> str:
    # coarse placeholder thresholds (public-safe)
    if abs(delta) < soft: return 'GREEN'
    if abs(delta) < hard: return 'YELLOW'
    return 'RED'
