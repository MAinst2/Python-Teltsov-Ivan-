import os
import pandas as pd

# Определяем путь к CSV относительно скрипта
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'students.csv')

# 1. Загрузка данных
df = pd.read_csv(csv_path)

# 2. Первые 5 строк
print("Первые 5 строк:")
print(df.head().to_string(index=False))
print()

# 3. Информация о данных
print("Информация о наборе данных:")
df.info()
print()

# 4. Статистика по числовым столбцам
print("Статистика по числовым столбцам:")
print(df[['Age', 'Score']].describe().to_string())
print()

# 5. Средний балл всех студентов
avg = df['Score'].mean()
print(f"Средний балл студентов: {avg:.2f}")
print()

# 6. Количество студентов по группам
print("Число студентов по группам:")
group_counts = df['Group'].value_counts().sort_index()
for grp, cnt in group_counts.items():
    print(f"  Группа {grp}: {cnt}")
print()

# 7. Средний балл по группам
print("Средний балл по группам:")
group_means = df.groupby('Group')['Score'].mean().sort_index()
for grp, m in group_means.items():
    print(f"  Группа {grp}: {m:.2f}")
