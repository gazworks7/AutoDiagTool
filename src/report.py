from typing import Dict

def text_report(vehicle: str, deltas: Dict) -> str:
    lines = [f"AutoDiagTool Report — Vehicle: {vehicle}", ""]
    for k, d in sorted(deltas.items()):
        lines.append(f"{k}: delta {d}")
    return "\n".join(lines)
