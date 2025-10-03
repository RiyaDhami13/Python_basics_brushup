import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex5 import *
print("Setup Complete")

# Path of the files to read
cancer_filepath = "../input/cancer.csv"

# Fill in the line below to read the file into a variable cancer_data
cancer_data = pd.read_csv(cancer_filepath,index_col = 'Id')

# Histograms for benign and maligant tumors
sns.histplot(data=cancer_data, x= 'Area (mean)',hue = 'Diagnosis')

# KDE plots for benign and malignant tumors
sns.kdeplot(data = cancer_data['Radius (worst)'],shade = True) 
