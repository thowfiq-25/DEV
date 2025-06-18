import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create sample data and save to CSV
data = {
    'sender': ['alice@example.com', 'bob@example.com', 'alice@example.com'],
    'receiver': ['bob@example.com', 'alice@example.com', 'carol@example.com'],
    'subject': ['Hello', 'Meeting Reminder', 'Project Update'],
    'timestamp': ['2023-08-01 10:00:00', '2023-08-02 14:30:00', '2023-08-03 09:15:00'],
    'content': [
        'Hi Bob,\n\nHow are you?',
        'Hi Alice,\n\nDon\'t forget the meeting at 3 PM.',
        'Hi Carol,\n\nHere\'s the latest project update.'
    ]
}
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.to_csv('emails.csv', index=False)
print("CSV file created successfully.")

# Step 2: Load the data and inspect
df = pd.read_csv("emails.csv")
print(df.info())

# Step 3: Data preprocessing
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.dropna(inplace=True)

# Step 4: Add a new column for email length
df['email_length'] = df['content'].apply(len)

# Step 5: Plot distribution of email lengths
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='email_length', bins=30, kde=True)
plt.xlabel('Email Length')
plt.ylabel('Count')
plt.title('Distribution of Email Lengths')
plt.show()

# Step 6: Top 10 email senders
top_senders = df['sender'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_senders.index, y=top_senders.values)
plt.xticks(rotation=45)
plt.xlabel('Sender')
plt.ylabel('Number of Emails')
plt.title('Top 10 Email Senders')
plt.tight_layout()
plt.show()

# Step 7: Top 10 email receivers
top_receivers = df['receiver'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_receivers.index, y=top_receivers.values)
plt.xticks(rotation=45)
plt.xlabel('Receiver')
plt.ylabel('Number of Emails')
plt.title('Top 10 Email Receivers')
plt.tight_layout()
plt.show()

# Step 8: Email activity over time
df['year_month'] = df['timestamp'].dt.to_period('M')
email_activity = df.groupby('year_month').size()

plt.figure(figsize=(12, 6))
email_activity.plot(kind='line', marker='o')
plt.xlabel('Year-Month')
plt.ylabel('Number of Emails')
plt.title('Email Activity Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
