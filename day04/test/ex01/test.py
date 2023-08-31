from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(youngest_fellah(data, 2004))
