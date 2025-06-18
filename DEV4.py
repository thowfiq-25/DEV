import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a sample dataset
data = {
    'ID': range(1, 11),
    'Age': np.random.randint(18, 65, size=10),
    'Income': np.random.randint(30000, 90000, size=10),
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'Education': [
        'High School', 'Bachelor', 'Master', 'PhD', 'Bachelor',
        'Master', 'Bachelor', 'PhD', 'High School', 'Master'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first 5 rows
print("🔹 First 5 rows:")
print(df.head())

# Summary statistics
print("\n🔹 Descriptive statistics:")
print(df.describe())

# Check for missing values
print("\n🔹 Missing values:")
print(df.isnull().sum())

# Unique values in categorical columns
print("\n🔹 Unique Genders:", df['Gender'].unique())
print("🔹 Unique Education Levels:", df['Education'].unique())

# Selecting specific columns
print("\n🔹 Selected Columns (Age & Income):")
print(df[['Age', 'Income']].head())

# Filter: Age > 30
print("\n🔹 People with Age > 30:")
print(df[df['Age'] > 30].head())

# Filter: Males with Master's degree
print("\n🔹 Males with Master's Degree:")
print(df[(df['Gender'] == 'Male') & (df['Education'] == 'Master')].head())
plt.figure(figsize=(6, 4))
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 4))
plt.boxplot(df['Income'])
plt.title('Income Distribution')
plt.ylabel('Income')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6, 4))
gender_counts.plot(kind='bar', color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


education_counts = df['Education'].value_counts()
plt.figure(figsize=(6, 6))
education_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['gold', 'lightcoral', 'lightgreen', 'lightskyblue']
)
plt.title('Education Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()
