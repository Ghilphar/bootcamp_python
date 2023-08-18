from FileLoader import FileLoader
from HowManyMedals import how_many_medals

loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(how_many_medals(data, 'Kjetil Andr Aamodt'))
