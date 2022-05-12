import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

# print(df.head(3))
# print(df.tail(3))

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

# df = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(df)

# Read Headers
df.columns

# read each Column
# print(df[['Name','Type 1', 'HP']][0:5])
# print(df.Name)
# for index, row in df.iterrows():
#     print(index, row['Name'])
# print(df.loc[df['Type 1'] == 'Grass'])

# Read Each Row
# print(df.iloc[0:4])

# Read a specific location (R,C)
# print(df.iloc[2, 1])

#Sorting/Describing Data
# print(df.describe())
# print(df.sort_values(['Name', 'HP'], ascending=[1, 0]))

# add column
df['Total'] = df['HP']+ df['Attack']+df['Defense']+df['Sp. Atk'] + df['Speed']

# drop column
# df = df.drop(columns=['Total'])
# print(df.head(5))

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#
# cols = list(df.columns.values)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df.head(5))

# df.to_csv('modfied.csv', index=False)
# df.to_excel('modfied.xlsx', index=False)
# df.to_csv('modified.txt', index=False, sep='\t')

# print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])  and
# new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison') & (df['HP'] >70)]

# new_df.to_csv('filtered.csv', index=False)
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)

# new2_df = df.loc[~df['Name'].str.contains('Mega')]
# new2_df = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
# new2_df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

# df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = 'Fire'
# print(df)

# df = pd.read_csv('modfied.csv')
# df.loc[df['Total']<500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
# print(df)

# Agregate Statistics (Groupby)
# df = pd.read_csv('modfied.csv')
# print(df.groupby(['Type 1']).mean().sort_values('HP', ascending=False))
# df['count'] = 1
# print(df.groupby(['Type 1', 'Type 2']).count()['count'])

# work with large amounts of data:
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modfied.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, results])
print(new_df)