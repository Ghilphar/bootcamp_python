import pandas as pd

def how_many_medals_by_country(df: pd.DataFrame, country: str) -> dict:

    if not isinstance(df, pd.DataFrame) or not isinstance(country, str):
        return None
    
    #team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Handball', 'Water Polo', 
    #                'Hockey', 'Rowing', 'Volleyball', 'Synchronized Swimming', 
    #                'Baseball', 'Rugby', 'Lacrosse', 'Polo']
    #
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing',
                    'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
                    'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby',
                    'Lacrosse', 'Polo']


    country_medals = df[(df["Team"] == country) & (~df["Medal"].isna()) & (df["Year"] == 2004)] # TODO supprimer la fin (Year)
    #country_medals.drop_duplicates(subset=["Sport"], keep='first')

    team_sports_df = country_medals[country_medals['Sport'].isin(team_sports)]
    team_sports_df = team_sports_df.drop_duplicates(subset=['Sport', 'Event', 'Year', 'Medal'])
    non_team_sports_df = country_medals[~country_medals['Sport'].isin(team_sports)]

    #.drop_duplicates(subset=["Year", "Event", "Medal"])


    medals_dict = {}

    for _, row in non_team_sports_df.iterrows():
        year = row["Year"]
        medal = row["Medal"][0]

        if year not in medals_dict:
            medals_dict[year] = {'G': 0, 'S': 0, 'B': 0}
        medals_dict[year][medal] += 1

    return medals_dict