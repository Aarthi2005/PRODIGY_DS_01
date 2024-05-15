import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a DataFrame
df = pd.read_csv("C:\\Users\\aarth\\Downloads\\heart_failure_clinical_records_dataset.csv")

# Group by 'sex' and count the number of death events for each gender
death_counts = df.groupby('sex')['DEATH_EVENT'].sum()

# Plotting the bar chart
plt.figure(figsize=(8, 6))
death_counts.plot(kind='bar', color=['lightblue', 'pink'])
plt.title('Distribution of Death Events by Gender')
plt.xlabel('Gender (0: Female, 1: Male)')
plt.ylabel('Number of Deaths')
plt.xticks(ticks=[0, 1], labels=['Female', 'Male'], rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Extract ages of individuals who experienced death due to heart failure
deaths_age = df[df['DEATH_EVENT'] == 1]['age']

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(deaths_age, bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Ages for Death due to Heart Failure')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
