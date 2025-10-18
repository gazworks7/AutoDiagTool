import pandas as pd

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates()
    # clamp obviously impossible values
    if 'ECT' in df.columns:
        df['ECT'] = df['ECT'].clip(-40, 140)
    return df
