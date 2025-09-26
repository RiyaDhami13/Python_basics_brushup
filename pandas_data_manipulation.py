import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")

#selecting description from reviews
desc = reviews.description

#Selecting first value from the description column of reviews, assigning it to variable first_description
first_description = reviews['description'][0]

#Selecting the first row of data (the first record) from reviews, assigning it to the variable first_row
first_row = reviews.iloc[0]

#Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions
first_descriptions = reviews['description'].iloc[:10]

#Selecting the records with index labels 1, 2, 3, 5, and 8
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]

#create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100.
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]

 #Selecting rows with labels from 0 to 99 and specified column names
df = reviews.loc[:99, ['country', 'variety']]

# DataFrame italian_wines containing reviews of wines made in Italy
italian_wines = reviews[reviews.country == 'Italy'].copy()
