import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

# Loading the Data
species = pd.read_csv('species_info.csv')

# print species.head()

# Inspecting the DataFrame
species_count = len(species)

#The categories of species
species_type = species.category.unique()

#The types of conservation_status
conservation_statuses = species.conservation_status.unique()

# Analyze Species Conservation Status
conservation_counts = species.groupby('conservation_status').scientific_name.count().reset_index()

# print conservation_counts

# Analyze Species Conservation Status II
species.fillna('No Intervention', inplace = True)

conservation_counts_fixed = species.groupby('conservation_status').scientific_name.count().reset_index()

# Plotting Conservation Status by Species
protection_counts = species.groupby('conservation_status')\
    .scientific_name.count().reset_index()\
    .sort_values(by='scientific_name')
    
# plt.figure(figsize=(10, 4))
# ax = plt.subplot()
# plt.bar(range(len(protection_counts)),
#        protection_counts.scientific_name.values)
# ax.set_xticks(range(len(protection_counts)))
# ax.set_xticklabels(protection_counts.conservation_status.values)
# plt.ylabel('Number of Species')
# plt.title('Conservation Status by Species')
# labels = [e.get_text() for e in ax.get_xticklabels()]
# print ax.get_title()
# plt.show()

# create a boolean is_protected col
species['is_protected'] = species.conservation_status != 'No Intervention'

# groupby category and is_protected
category_counts = species.groupby(['category', 'is_protected'])                      .scientific_name.count().reset_index()
  
# print category_counts.head()
#pivot the table
category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()

# change the T/F col names
category_pivot.columns = ['category', 'not_protected', 'protected']

# create a col with percentage protected
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

print category_pivot.head()

# create contingency table for mammals/birds
contingency = [[30, 146],
              [75, 413]]

# run chi-squared on mammals/birds
pval = chi2_contingency(contingency)[1]
print "mammal-bird p_val: %f " % pval

# create contingency table for mammals/reptiles
contingency2 = [[5, 73],
               [30, 146]]
# run chi-squared on mammals/reptiles
pval_reptile_mammal = chi2_contingency(contingency2)[1]

print "reptile mammal p_val: %f " % pval_reptile_mammal