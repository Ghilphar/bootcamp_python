import pandas as pd

def how_many_medals_by_country(df: pd.DataFrame, country: str) -> dict:
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Handball', 'Water Polo', 
                    'Hockey', 'Rowing', 'Volleyball', 'Synchronized Swimming', 
                    'Baseball', 'Rugby', 'Lacrosse', 'Polo']
    
    country_medals = df[(df["Team"] == country) & (~df["Medal"].isna())]
    country_medals = country_medals.drop_duplicates(subset=["Year", "Event", "Medal"])

    medals_dict = {}

    for _, row in country_medals.iterrows():
        year = row["Year"]
        medal = row["Medal"][0]

        if year not in medals_dict:
            medals_dict[year] = {'G': 0, 'S': 0, 'B': 0}
        medals_dict[year][medal] += 1

    return medals_dict