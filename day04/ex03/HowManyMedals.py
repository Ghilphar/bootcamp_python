import pandas as pd

def how_many_medals(df: pd.DataFrame, participant_name: str) -> dict:
    medals_dict = {}

    if not isinstance(df, pd.DataFrame) or not isinstance(participant_name, str):
        return None

    # Filter the dataframe by the participant's name
    participant_data = df[df["Name"] == participant_name]

    for _, row in participant_data.iterrows():
        year = row["Year"]
        medal = row["Medal"]
        medals_dict.setdefault(year, {'G': 0, 'S': 0, 'B': 0})
        if pd.notna(medal):
            medals_dict[year][medal[0]] += 1

    return medals_dict