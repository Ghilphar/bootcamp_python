from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(proportion_by_sport(data, 2004, "Tennis", "F"))
