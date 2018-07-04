import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')
print observations.head(10)

#create boolean col if species is_sheep
species["is_sheep"] = species.apply(lambda row: 
                                   'Sheep' in row["common_names"], axis=1) 

#print species.head(10)

# create new table just for sheep
species_is_sheep = species[species.is_sheep]
#print species_is_sheep.head(10)

# again, but only get the mammals
sheep_species = species[(species.is_sheep) & (species.category == "Mammal")]
print sheep_species.head(10)

# merge sheep and observation data
sheep_observations = pd.merge(sheep_species, observations, left_on='scientific_name', right_on='scientific_name', suffixes=['sheep_species', 'observations'])

print sheep_observations.head(10)

# get the sheep sightings for each park
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
print obs_by_park
