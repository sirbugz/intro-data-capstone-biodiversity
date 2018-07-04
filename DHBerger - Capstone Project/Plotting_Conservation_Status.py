import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)

# sort the conservation status table by the counts in scientific_name
protection_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index().sort_values(by='scientific_name')
print protection_counts

#set up the bar char
plt.figure(figsize=(10,4))
ax = plt.subplot()
#print protection_counts.conservation_status.count()
#print protection_counts.scientific_name
plt.bar(range(protection_counts.conservation_status.count()), protection_counts.scientific_name)

# x ticks
ax.set_xticks(range(protection_counts.conservation_status.count()))
#x tick lables
ax.set_xticklabels(protection_counts.conservation_status)

# y axis label & title
plt.ylabel("Number of Species")
plt.title("Conservation Status by Species")

plt.show()
plt.savefig(conservation_status_by_species.png')