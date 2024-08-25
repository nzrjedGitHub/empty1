import pandas as pd 


# Крок 1. Завантаження та очищення даних
df = pd.read_csv('titanic.csv')

print(df.head())