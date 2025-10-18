import pandas as pd

def simple_stats(df: pd.DataFrame) -> dict:
    # compute basic means as a placeholder
    keys = [c for c in [
        'RPM','MAP','ECT','LTFT1','STFT1','O2S11','TP','VSS','IAT','BARO','VPWR'
    ] if c in df.columns]
    return {k: float(df[k].mean()) for k in keys if not df.empty}
