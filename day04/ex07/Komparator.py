import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator:

    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise ValueError("Provided data is not a pandas DataFrame")
    
    def compare_box_plots(self, categorical_var, numerical_var):
        """
        Display a series  of box plots to compare the distribution of the numerical
        variable for different categories of the categorical variable. 
        """
        if categorical_var in self.data and numerical_var in self.data:
            if pd.api.types.is_numeric_dtype(self.data[numerical_var]) and \
            pd.api.types.is_categorical_dtype(self.data[categorical_var]):
                sns.boxplot(x=categorical_var, y=numerical_var, data=self.data)
                plt.show()
            else:
                print("Type Error")
        else:
            print("One or both of the colums are not found in the data.")

    def density(self, categorical_var, numerical_var):
        """
        Display the density of the numerical variable, with each subpopulation
        (based on the categorical variable) represented by a separate curve on the graph.  
        """
        if categorical_var in self.data and numerical_var in self.data:
            if pd.api.types.is_numeric_dtype(self.data[numerical_var]) and \
            pd.api.types.is_categorical_dtype(self.data[categorical_var]):
                categories = self.data[categorical_var].unique()
                for category in categories:
                    subset = self.data[self.data[categorical_var] == category]
                    if not subset[numerical_var].isna().all():
                        subset[numerical_var].plot(kind='kde', label=category)
                    else:
                        pass
                plt.legend()
                plt.show()
            else:
                print("Type Error")
        else:
            print("One or both of the colums are not found in the data.")

    def compare_histograms(self, categorical_var, numerical_var):
        """
        Plot the numerical variable in a separate histogram for each category
        of the categorical variable with overlapping histograms using a color code.
        """
        if categorical_var in self.data and numerical_var in self.data:
            if pd.api.types.is_numeric_dtype(self.data[numerical_var]) and \
            pd.api.types.is_categorical_dtype(self.data[categorical_var]):
                categories = self.data[categorical_var].unique()
                for category in categories:
                    subset = self.data[self.data[categorical_var] == category]
                    subset[numerical_var].hist(label=category, alpha=0.5, bins=50)
                plt.legend()
                plt.show()
            else:
                print("Type Error")
        else:
            print("One or both of the colums are not found in the data.")