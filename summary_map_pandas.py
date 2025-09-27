import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()

#the median of the points column in the reviews DataFrame
median_points = reviews.points.median()

#countries are represented in the dataset without duplication
countries = reviews.country.unique()

#a Series mapping countries to the count of wine reviews from that country
reviews_per_country = reviews.country.value_counts()

#centered_price containing a version of the price column with the mean price subtracted
centered_price = reviews.price - reviews.price.mean()

#Which wine is the "best bargain"? Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

#Is a wine more likely to be "tropical" or "fruity"? Create a Series descriptor_counts counting how many times each of these two words appears in the description column in the dataset
descriptor_counts = pd.Series({
    'tropical':reviews.description.str.contains("tropical").sum(),
    'fruity':reviews.description.str.contains("fruity").sum()
})

# Convert wine review scores (80–100 points) into a simpler star rating system:
# - Canadian wines always get 3 stars
# - 95+ points = 3 stars
# - 85–94 points = 2 stars
# - Below 85 points = 1 star
def assign_stars(row):
    if row.country == "Canada":
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(assign_stars, axis='columns')
