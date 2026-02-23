import pandas as pd

#Series vs Dataframe
# s = pd.Series([1,2,3,4])
# print(s)

# data = {
#     "Name": ["A", "B", "C"],
#     "Score": [85, 90, 78]
# }

# df = pd.DataFrame(data)
# print(df)
# import os
# # print(os.getcwd())

# df = pd.read_csv('./data.csv')


# #Inspecting Data (First Things You Always Do)
# #df.head()
# #df.tail()
# df.shape
# #df.columns
# df.info()
# #df.describe()
# print(df['Phone'])
# print(df[['Phone','Quantity']])


# print(df.iloc[0] )       # first row
# print(df.iloc[0:3] )     # first 3 rows
# print(df.loc[0])

# #Filtering (SUPER IMPORTANT)
# print(df.isnull().sum())
# df.dropna() #Drop missing
# df.fillna(0) #Fill missing
# # df[(df["Score"] > 80) & (df["Age"] > 20)]

# #Group by

# data = {
#     "Player": ["A", "B", "C", "D"],
#     "Team": ["Red", "Blue", "Red", "Blue"],
#     "Points": [20, 15, 25, 30]
# }

# df = pd.DataFrame(data)

# print(df.groupby("Team")['Points'].mean())

# import pandas as pd

# data = {
#     "Player": ["A", "B", "C", "D"],
#     "Team": ["Red", "Blue", "Red", "Blue"],
#     "Points": [20, 15, 25, 30]
# }

# df = pd.DataFrame(data)
# print(df)

# grouped = df.groupby('Team')
# print(grouped)

# df.groupby("Team")["Points"].sum()      # Total points per team
# df.groupby("Team")["Points"].max()      # Max points per team
# df.groupby("Team")["Points"].min()      # Min points per team
# df.groupby("Team")["Points"].count()    # Number of players per team

# df.groupby("Team")["Points"].agg(["mean", "sum", "max"])

# Group by multiple columns
# df.groupby(["Team", "Player"])["Points"].sum()

#Adding New Columns (Feature Engineering)
# new = df['Double Poitns'] = df['Points'] *2
# print(new)

#MINI PROJECT — Sports Stats Analysis
import pandas as pd

data = {
    "Player": ["A", "B", "C", "D", "E"],
    "Team": ["Red", "Blue", "Red", "Blue", "Red"],
    "Points": [20, 15, 25, 30, 10],
    "Assists": [5, 7, 3, 8, 2]
}

df = pd.DataFrame(data)

top_scorer = df['Points'].max()
top_scorer = df.loc[df['Points'].idxmax()]
print(top_scorer)

print(df.sort_values(by="Points", ascending=False))
print(df.groupby('Team')['Points'].mean())

#New Feature
df["Total"] = df["Points"] + df["Assists"]
print(df.sort_values(by="Total", ascending=False))