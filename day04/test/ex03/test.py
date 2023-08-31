from FileLoader import FileLoader
from HowManyMedals import how_many_medals

loader = FileLoader()
data = loader.load("../essources/athlete_events.csv")

print(how_many_medals(data, 'Kjetil Andr Aamodt'))
