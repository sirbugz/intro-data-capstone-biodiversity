import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]

observations = pd.read_csv('observations.csv')

sheep_observations = observations.merge(sheep_species)

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

# set plot size and get the axis object
plt.figure(figsize=(16,4))
ax = plt.subplot()

#set up the bar chart values
x_values = range(obs_by_park.park_name.count())
y_values = obs_by_park.observations
plt.bar(x_values, y_values)

# set x_ticks and their labels
ax.set_xticks(range(obs_by_park.park_name.count()))
ax.set_xticklabels(obs_by_park.park_name)

# labels & title
plt.ylabel("Number of Observations")
plt.title("Observations of Sheep per Week")

plt.show()