import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'students.csv')
df = pd.read_csv(csv_path)

high_scores = df[df['Score'] > 80]
print("Студенты с баллом > 80:")
print(high_scores.to_string(index=False))
print()

sorted_high = high_scores.sort_values(by='Score', ascending=False)
print("Отсортированные по баллу (убывание):")
print(sorted_high.to_string(index=False))
print()

max_age = df['Age'].max()
min_age = df['Age'].min()

oldest = df[df['Age'] == max_age]
youngest = df[df['Age'] == min_age]

print(f"Самый старший студент (возраст {max_age}):")
print(oldest.to_string(index=False))
print()

print(f"Самый младший студент (возраст {min_age}):")
print(youngest.to_string(index=False))