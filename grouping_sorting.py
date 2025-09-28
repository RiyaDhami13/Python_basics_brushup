import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *
print("Setup complete.")

#a Series whose index is the taster_twitter_handle category from the dataset, and whose values count how many reviews each person wrote
reviews_written = reviews.groupby('taster_twitter_handle').size()

# a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. Sort the values by price, ascending
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

# a DataFrame whose index is the variety category from the dataset and whose values are the min and max values thereof.
price_extremes = reviews.groupby(['variety']).price.agg([ min, max])

#a variable sorted_varieties containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
