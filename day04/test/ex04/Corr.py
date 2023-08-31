import pandas as pd
from SpatioTemporalData import SpatioTemporalData

CSV_PATH="../ressources/athlete_events.csv"


df = pd.read_csv(CSV_PATH)
sp = SpatioTemporalData(df)

print(sp.where(2000))
# output is: ['Sydney']

print(sp.where(1980))
# output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.

print(sp.when('London'))
# output is: [2012, 1948, 1908]