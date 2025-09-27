import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'students.csv')
df = pd.read_csv(csv_path)

print("Пропуски до обработки:")
print(df.isnull().sum(), end="\n\n")

# Заполнение пропусков в Score (если бы они были)
mean_score = df['Score'].mean()
df['Score'] = df['Score'].fillna(mean_score)

# Удаление строк с пропусками в Group (если бы они были)
df = df.dropna(subset=['Group'])

print("Пропуски после обработки:")
print(df.isnull().sum())
