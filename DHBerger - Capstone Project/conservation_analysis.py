import codecademylib

# get the libraries
import pandas as pd
from matplotlib import pyplot as plt

# pull in the data
species = pd.read_csv("species_info.csv")

# check out the first couple rows of the data
print species.head(20)

#The number of species
species_count = species.scientific_name.nunique()
print species_count

#The categories of species
species_type = species.category.unique()
print species_type

#The types of conservation_status
conservation_statuses = species.conservation_status.unique()
print conservation_statuses

# Conservation Counts for (unique) species (misses NaN)
conservation_counts = species.groupby("conservation_status").scientific_name.nunique().reset_index()
print conservation_counts

# replace NaNs in species df with "No Intervention"
species.fillna('No Intervention', inplace = True)

# Conservation Counts for (unique) species now with "No Intervention" as a status
conservation_counts_fixed = species.groupby("conservation_status").scientific_name.nunique().reset_index()
print conservation_counts_fixed