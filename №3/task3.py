import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Товар': ['Ноутбук','Смартфон','Планшет','Наушники','Смартфон','Ноутбук','Планшет','Колонка'],
    'Цена': [1000, 800, None, 100, np.nan, 1200, 300, 150],
    'Количество': [5, 2, 1500, 0, 10, 1, 5, 1200]
}

df = pd.DataFrame(data)
df['Цена'] = df['Цена'].fillna(df['Цена'].median())
df = df[(df['Количество'] >= 1) & (df['Количество'] <= 1000)]
df['Общая_стоимость'] = df['Цена'] * df['Количество']

revenue = df.groupby('Товар')['Общая_стоимость'].sum().reset_index()

plt.figure()
plt.bar(revenue['Товар'], revenue['Общая_стоимость'])
plt.xlabel('Товар')
plt.ylabel('Выручка')
plt.title('Выручка по товарам')
plt.tight_layout()
plt.savefig('result.png')
plt.show()

print(revenue)
