
import pandas as pd
from Komparator import Komparator

# Load the data
data = pd.read_csv('../athlete_events.csv')

# Convert certain columns to categorical type for better comparison
data['Sex'] = data['Sex'].astype('category')
data['Season'] = data['Season'].astype('category')
data['Medal'] = data['Medal'].astype('category')
data = data.dropna(subset=['Medal'])

# Instantiate the Komparator class
komparator = Komparator(data)

# Test various combinations
komparator.compare_box_plots('Sex', 'Height')
komparator.compare_box_plots('Sex', 'Weight')
komparator.compare_box_plots('Medal', 'Age')
komparator.compare_box_plots('Season', 'Age')

komparator.compare_histograms('Sex', 'Height')
komparator.compare_histograms('Sex', 'Weight')
komparator.compare_histograms('Medal', 'Age')

komparator.density('Sex', 'Height')
komparator.density('Sex', 'Weight')



komparator.density('Medal', 'Age')