import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)

# create a boolean is_protected col
species['is_protected'] = species.conservation_status != 'No Intervention'

# groupby category and is_protected
category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()

#pivot the table
category_pivot = category_counts.pivot(columns='is_protected',
                      index='category',
                      values='scientific_name')\
                      .reset_index()

# change the T/F col names
category_pivot.columns = ["category",	"not_protected","protected"]
print category_pivot

# create a col with percentage protected
category_pivot["percent_protected"] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)
print category_pivot