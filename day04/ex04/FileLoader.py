import pandas as pd

class FileLoader:
    def load(self, path):
        try:
            df=pd.read_csv(path)
            print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
            return df
        except Exception as e:
            print(f"Error {e}")
            return None
    
    def display(self, df, n):
        if isinstance(df, pd.DataFrame):
            if n > 0:
                print(df.head(n))
            else:
                print(df.tail(abs(n)))
        else:
            print("Provided data is not valid pandas Dataframe")