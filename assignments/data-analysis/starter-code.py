# Starter Code: Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset (replace 'data.csv' with your file)
df = pd.read_csv('data.csv')

# 2. Display the first 5 rows
print(df.head())

# 3. Show summary statistics
print(df.describe())

# 4. Create visualizations
# Plot 1: Histogram of scores
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
df['score'].hist(bins=5, edgecolor='black')
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')

# Plot 2: Scatter plot (age vs score)
plt.subplot(1, 2, 2)
plt.scatter(df['age'], df['score'], color='blue', s=100)
plt.title('Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')

plt.tight_layout()

# Save your plots as images using plt.savefig('filename.png')
plt.savefig('plots.png')
print("Plots saved as 'plots.png'")

# Display the plots
plt.show()
