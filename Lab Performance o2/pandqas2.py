import pandas as pd
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, None],
    'C': [1, None, None, 4, 5]
}
df = pd.DataFrame(data)
df_filled = df.fillna(df.mean())

print(df_filled)