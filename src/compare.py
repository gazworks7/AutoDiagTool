# src/compare.py
from typing import Dict

PID_THRESH = {
    "RPM":   (50.0, 100.0),
    "MAP":   (5.0, 10.0),
    "LTFT1": (3.0, 8.0),
    "STFT1": (5.0, 10.0),
    "O2S11": (0.2, 0.4),
    "ECT":   (3.0, 6.0),
    "IAT":   (3.0, 6.0),
    "TP":    (3.0, 6.0),
    "VSS":   (2.0, 5.0),
    "VPWR":  (0.3, 0.6),
    "BARO":  (1.0, 2.0),
}

def deltas(current: Dict, baseline: Dict) -> Dict:
    out = {}
    for k, v in current.items():
        if k in baseline:
            out[k] = round(v - baseline[k], 3)
    return out

def color_flag(delta: float, pid: str) -> str:
    soft, hard = PID_THRESH.get(pid, (5.0, 10.0))
    if abs(delta) < soft: return 'GREEN'
    if abs(delta) < hard: return 'YELLOW'
    return 'RED'
