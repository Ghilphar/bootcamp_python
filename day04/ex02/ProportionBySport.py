import pandas as pd

def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str) -> float:

    if not isinstance(df, pd.DataFrame) or not isinstance(year, int) or not isinstance(gender, str) or not isinstance(gender, str):
        return None

    df_filtered = df[(df["Year"] ==  year) & (df["Sex"] == gender)]
    # If we only drop by name we will not have the correct result
    df_filtered = df_filtered.drop_duplicates(subset=["Name", "Age", "Height"])
    
    total_participants = df_filtered.shape[0]

    sport_participants = df_filtered[df_filtered["Sport"] == sport].shape[0]

    proportion = (sport_participants / total_participants)

    return proportion