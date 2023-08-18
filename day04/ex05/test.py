from FileLoader import FileLoader
from HowManyMedalsByCountry import how_many_medals_by_country

loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(how_many_medals_by_country(data, "Finland"))

