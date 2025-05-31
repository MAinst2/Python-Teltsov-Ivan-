import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'students.csv')
df = pd.read_csv(csv_path)

group_mean = df.groupby('Group')['Score'].mean().sort_index()
group_median = df.groupby('Group')['Age'].median().sort_index()

print("Средний балл и медианный возраст по группам:")
for grp in group_mean.index:
    print(f"Группа {grp}: средний балл {group_mean[grp]:.2f}, медианный возраст {int(group_median[grp])}")
print()

df['Passed'] = (df['Score'] >= 60).astype(int)
print("Данные с добавленным столбцом Passed:")
print(df.to_string(index=False))
