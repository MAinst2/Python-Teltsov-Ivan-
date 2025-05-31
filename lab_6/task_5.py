import os
import pandas as pd
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'students.csv')
df = pd.read_csv(csv_path)

# готовим средние по группам
means = df.groupby('Group')['Score'].mean().sort_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 1) Гистограмма с равномерными бинами и четкими подписями
scores = df['Score']
# определяем границы бинов кратные 5
min_bin = scores.min() // 5 * 5
max_bin = (scores.max() // 5 + 1) * 5
bins = list(range(min_bin, max_bin + 1, 5))
ax1.hist(scores, bins=bins, edgecolor='black')
ax1.set_title('Распределение баллов')
ax1.set_xlabel('Score')
ax1.set_ylabel('Количество студентов')
ax1.set_xticks(bins)
ax1.set_xlim(min_bin, max_bin)

# 2) Столбчатая диаграмма среднего балла по группам
positions = list(range(len(means)))
ax2.bar(positions, means.values, width=0.6, edgecolor='black')
ax2.set_xticks(positions)
ax2.set_xticklabels(means.index)
ax2.set_title('Средний балл по группам')
ax2.set_xlabel('Group')
ax2.set_ylabel('Средний балл')

plt.tight_layout()
plt.show()
