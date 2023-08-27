import pandas as pd

# Function to filter DataFrame based on the "Year" column and save it to a new CSV file
def filter_year_and_save(input_csv_path, output_csv_path, target_year=2004):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)
    
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing',
                'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
                'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby',
                'Lacrosse', 'Polo']

    # Filter the DataFrame to only include rows where the "Year" is equal to target_year
    filtered_df = df[df['Year'] == target_year]
    filtered_df = filtered_df[filtered_df["Team"] == "United States"]
    filtered_df = filtered_df[~filtered_df["Medal"].isna()]
    filtered_df = filtered_df[filtered_df["Medal"] == "Gold"]

    final_df = pd.DataFrame()

    for sport in team_sports:
        sport_data = filtered_df[filtered_df["Sport"] == sport]
        sport_data = sport_data.head(1)
        
        filtered_df = filtered_df[filtered_df['Sport'] != sport]
        final_df = pd.concat([filtered_df, sport_data])
    
    # Save the filtered DataFrame to a new CSV file
    final_df.to_csv(output_csv_path, index=False)

filter_year_and_save("../ressources/athlete_events.csv", "./newcsv.csv", 2004)