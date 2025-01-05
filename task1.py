#Make sure your Internet is connected while Executing the code.

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Fetch data from the Open Notify API
response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    print("Data fetched successfully!")
else:
    print("Failed to fetch data.")

# Extract the latitude and longitude of the ISS
latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])

# Create a DataFrame for visualization
df = pd.DataFrame({
    'Latitude': [latitude],
    'Longitude': [longitude]
})

# Step 2: Create visualizations
plt.figure(figsize=(10, 6))

# Scatter plot of the ISS position
sns.scatterplot(data=df, x='Longitude', y='Latitude', color='blue', s=100)
plt.title('Current Position of the ISS')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.show()
