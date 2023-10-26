# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the 'universal_top_spotify_songs.csv' dataset
data = pd.read_csv('universal_top_spotify_songs.csv')

# Group the data by 'country'
grouped_data = data.groupby('country')

# Analyze and visualize the popularity of top songs by country
plt.figure(figsize=(12, 6))
#uses Kernel Density Estimation (KDE) plots to visualize the popularity distribution of top songs in different countries.
for country, group in grouped_data:
    sns.kdeplot(group['popularity'], label=country, shade=True)

#plot 
plt.xlabel('Popularity')
plt.ylabel('Song Distribution')
plt.title('Popularity Distribution of Top Songs in Different Countries')
plt.legend()
plt.show()
