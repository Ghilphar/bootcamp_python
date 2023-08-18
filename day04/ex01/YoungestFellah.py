import pandas as pd

def youngest_fellah(df: pd.DataFrame, year:int) -> dict:
    # Filter the dataframe for the given year
    df_year = df[df["Year"] == year]
    
    # Find the age of the youngest woman and man
    youngest_woman_age = df_year[df_year["Sex"] == "F"]["Age"].min()
    youngest_man_age = df_year[df_year["Sex"] == "M"]["Age"].min()

    return {
        'f': youngest_woman_age,
        'm': youngest_man_age
    }
