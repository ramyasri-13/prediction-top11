import os
import pandas as pd 
import matplotlib as plt

file_path = "top11_player_performance.csv"

if os.stat(file_path).st_size == 0:
    print("ERROR: The CSV file is empty!")
else:
    df = pd.read_csv(file_path)
    print("File loaded successfully.")
    print(df.head())

# Fill missing values (in case any are there)
df.fillna(0, inplace=True)

# Calculate a performance score
df['Performance_Score'] = (
    df['runs_x'] * 0.5 +
    df['wickets'] * 10 -
    df['economy'] * 2
)

# Sort and select top 11 performers
top_11 = df.sort_values(by='Performance_Score', ascending=False).head(11)

# Print the result
print("🏏 Top 11 Players Based on Performance:\n")
print(top_11[['name_x', 'runs_x', 'wickets', 'economy', 'Performance_Score']])

# Plot the results
plt.figure(figsize=(12, 6))
plt.bar(top_11['name_x'], top_11['Performance_Score'], color='teal')
plt.title("Top 11 Player Performance Score")
plt.xlabel("Player Name")
plt.ylabel("Performance Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
