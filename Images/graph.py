import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Load CSV files
df_area = pd.read_csv("NFD - Area burned by month - EN FR.csv", encoding="ISO-8859-1")
df_number = pd.read_csv("NFD - Number of fires by month - EN FR.csv", encoding="ISO-8859-1")


# Merge the two dataframes on common columns
df = pd.merge(df_area, df_number, on=['Year', 'ISO', 'Jurisdiction', 'Month'])

# Group data by year and sum the values
df_grouped = df.groupby('Year').sum()

# Create a subplot for the area burned
fig, ax1 = plt.subplots(figsize=(12, 8)) 

# Create the first histogram
ax1.bar(df_grouped.index, df_grouped['Area (hectares)'], color='blue', alpha=0.5, label='Area Burned')
ax1.set_ylabel('Area Burned (hectares)', color='blue')
ax1.tick_params('y', colors='blue')

# Create a twin Axes sharing the x-axis
ax2 = ax1.twinx()

# Create the second histogram
ax2.bar(df_grouped.index, df_grouped['Number'], color='red', alpha=0.5, label='Number of Fires')
ax2.set_ylabel('Number of Fires', color='red')
ax2.tick_params('y', colors='red')

# Add title
plt.title('Area Burned and Number of Fires by Year')

# Add trendline for the area burned
ax1.plot(df_grouped.index, df_grouped['Area (hectares)'], color='darkblue', alpha=0.5)

# Add trendline for the number of fires
ax2.plot(df_grouped.index, df_grouped['Number'], color='darkred', alpha=0.5)

# Show legend
fig.tight_layout()
plt.show()