CSV_PATH="../ressources/athlete_events.csv"

from FileLoader import FileLoader
import os

f = FileLoader()

df = f.load(CSV_PATH)

f.display(df, 3)
f.display(df, -3)
f.display(df, 0)
f.display(df, "lol")
