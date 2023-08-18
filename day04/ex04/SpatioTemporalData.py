import pandas as pd

class SpatioTemporalData:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("The provided dataset should be a pandas DataFrame.")
        self.df = df

    def when(self, location):
        if not isinstance(location, str):
            raise TypeError("The provided location should be a string.")
        years = self.df[self.df["City"] == location]["Year"].unique().tolist()
        return years

    def where(self, date):
        if not isinstance(date, int):
            raise TypeError("The provided date should be an integer.")
        location = self.df[self.df["Year"] == date]["City"].unique().tolist()
        return location