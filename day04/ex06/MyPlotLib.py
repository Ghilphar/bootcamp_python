import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class MyPlotLib:

    def validate_features(data, features):
        """
        Validate if the features are numerical and present in the dataframe.
        """
        valid_features = []
        for feature in features:
            if feature in data.columns and (data[feature].dtype == "float64" or data[feature].dtype == "int64"):
                valid_features.append(feature)
        return valid_features

    def histogram(data, features):
        """
        Plots one histogram for each numerical feature in the list.
        """
        valid_features = MyPlotLib.validate_features(data, features)

        if valid_features:
            data[features].hist(figsize=(12, 8), bins=20)
            plt.tight_layout()
            plt.show()
        else:
            print("No valid numerical features provided.")

    def pair_plot(data, features):
        """
        Plots a matrix  of subplots (scatter plot matrix) showing scatter plots
        of one numerical variable against another one.
        The main diagonal shows simple histograms.
        """
        valid_features = MyPlotLib.validate_features(data, features)
        if valid_features:
            sns.pairplot(data[features])
            plt.show()
        else:
            print("No valid numerical features provided.")


    def box_plot(data, features):
        """
        Displays a box plot for each numerical variable in the dataset.
        """
        valid_features = MyPlotLib.validate_features(data, features)
        if valid_features:
            data[features].boxplot(figsize=(12, 8))
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("No valid numerical features provided.")

    def density(data, features):
        """
        Plots the density curve of each numerical feature in the list. 
        """
        valid_features = MyPlotLib.validate_features(data, features)
        if valid_features:
            for feature in valid_features:
                data[feature].plot(kind='kde', label=feature)
            plt.legend()
            plt.show()
        else:
            print("No valid numerical features provided.")

data = pd.read_csv("../athlete_events.csv")

features = ['Weight', 'Height']

MyPlotLib.pair_plot(data, features)
MyPlotLib.box_plot(data, features)
MyPlotLib.histogram(data, features)
MyPlotLib.density(data, features)