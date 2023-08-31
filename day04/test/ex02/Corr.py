from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

CSV_PATH="../ressources/athlete_events.csv"


loader = FileLoader()
data = loader.load(CSV_PATH)

print("")

print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n")
# output is "0.02307"

print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
# output is  "0.03284"

print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
# output is "0.00659"