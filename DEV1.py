import pandas as pd 
import matplotlib.pyplot as plt 

data = { 
'Name': ['John', 'Jane', 'Mike', 'Emily', 'Alex'], 
'Age': [25, 30, 22, 28, 35], 
'Score': [90, 85, 78, 95, 88] 
} 

df = pd.DataFrame(data) 
 
print("DataFrame:") 
print(df) 
 
print("\nData Analysis:") 
print("Mean Age:", df['Age'].mean()) 
print("Maximum Score:", df['Score'].max()) 
print("Minimum Score:", df['Score'].min()) 

plt.figure(figsize=(8, 4)) 
plt.bar(df['Name'], df['Score']) 
plt.xlabel('Name') 
plt.ylabel('Score') 
plt.title('Scores of Students') 
plt.show()