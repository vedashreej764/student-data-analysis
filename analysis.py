import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Average marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Top performer
topper = df.loc[df["Average"].idxmax()]

print("Top Performer:")
print(topper)

# Subject averages
subject_avg = df[["Maths", "Science", "English"]].mean()
print("\nSubject Averages:")
print(subject_avg)

# Plot graph
subject_avg.plot(kind="bar", title="Average Marks per Subject")
plt.show()
