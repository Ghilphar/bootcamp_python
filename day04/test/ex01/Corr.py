from FileLoader import FileLoader
from YoungestFellah import youngest_fellah
CSV_PATH="../ressources/athlete_events.csv"


loader = FileLoader()
data = loader.load(CSV_PATH)

print(youngest_fellah(data, 1992))
print(youngest_fellah(data, 2004))
print(youngest_fellah(data, 2010))
print(youngest_fellah(data, 2003))
