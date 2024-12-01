# Let's import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Let's load the dataset
data = pd.read_csv('C:\\Users\\User\\OneDrive\\Desktop\\Homework-3-Data-Visualization-1\\data\\vibration_data.csv')

#Let' preview the data
print(f"Dataset shape: {data.shape}")
print(data.head())

# Let's calculate vibration magnitude
data['Magnitude'] = np.sqrt(data['x']**2 + data['y']**2 + data['z']**2)

# Static Visualization 1: Line Plot of Vibration Magnitude Over Sample Index

# Display only the first 1000 points for clarity
plt.figure(figsize=(10, 6))
plt.plot(data['Magnitude'][:1000], label='Magnitude', color='blue', linewidth=2, alpha=0.8)  # Dispay only the first 1000 points for clarity
plt.axhline(data['Magnitude'].mean(), color='red', linestyle='--', label='Mean Magnitude')
plt.title('Vibration Magnitude Over Sample Index', fontsize=14, fontweight='bold')
plt.xlabel('Sample Index', fontsize=12)
plt.ylabel('Magnitude (m/s²)', fontsize=12)
plt.legend()
plt.grid(alpha=0.5)
plt.show()

# Static Visualization 2: Histogram of Magnitude Distribution
plt.figure(figsize=(10, 6))
plt.hist(data['Magnitude'], bins=50, color='green', alpha=0.7, edgecolor='black', linewidth=1.2)
plt.axvline(data['Magnitude'].mean(), color='red', linestyle='--', label='Mean Magnitude')
plt.axvline(data['Magnitude'].mean() + data['Magnitude'].std(), color='orange', linestyle='--', label='1 Std Dev')
plt.axvline(data['Magnitude'].mean() - data['Magnitude'].std(), color='orange', linestyle='--')
plt.title('Histogram of Vibration Magnitudes', fontsize=14, fontweight='bold')
plt.xlabel('Magnitude (m/s²)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(alpha=0.5)
plt.show()



