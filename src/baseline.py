import json, os
from typing import Dict

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '_baselines')
BASE_DIR = os.path.abspath(BASE_DIR)
os.makedirs(BASE_DIR, exist_ok=True)

def save(vehicle_id: str, stats: Dict):
    path = os.path.join(BASE_DIR, f"{vehicle_id}.json")
    with open(path, 'w') as f:
        json.dump(stats, f, indent=2)

def load(vehicle_id: str) -> Dict:
    path = os.path.join(BASE_DIR, f"{vehicle_id}.json")
    with open(path) as f:
        return json.load(f)
