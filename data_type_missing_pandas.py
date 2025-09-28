import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *
print("Setup complete.")

#Data type of column points
dtype = reviews.points.dtype

#convert points column entries into strings
reviews.points.astype('str')

#How many reviews in the dataset are null in the price
n_missing_prices = reviews.price.isnull().sum()

#a Series counting the number of times each value occurs in the region_1 field where missing values are replaced by "Unknown"
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
