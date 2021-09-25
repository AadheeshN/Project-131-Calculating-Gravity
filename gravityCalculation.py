# Import Modules
import pandas as pd
import csv
import plotly.express as px

# Data
data = pd.read_csv("final_data.csv")
print(data)

headers = data[0]
star_data = data[1:]

# Gravity Calculation
temp_star_rows = list(star_data)

name = []
distance = []
mass = []
radius = []
gravity = []

for star_data in star_data:
    name.append(star_data[1])
    distance.append(star_data[2])
    mass.append(star_data[3])
    radius.append(star_data[4])
    gravity.append(star_data[5])


star_gravity = []
for (index, name) in enumerate(name):
  gravity = (float(mass[index])*5.972e+24) / (float(radius[index])*float(radius[index])*6371000*6371000) * 6.674e-11
  star_gravity.append(gravity)

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)
df.to_csv('Final.csv')