import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

import os
if not os.path.exists("../input/museum_visitors.csv"):
    os.symlink("../input/data-for-datavis/museum_visitors.csv", "../input/museum_visitors.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex2 import *
print("Setup Complete")

# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col= "Date", parse_dates = True)

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()

# Line chart showing the number of visitors to each museum over time
sns.lineplot(museum_data)

# Line plot showing the number of visitors to Avila Adobe over time
sns.lineplot(museum_data['Avila Adobe'])
