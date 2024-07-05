import pandas as pd

# Считываем содержимое файла в переменную data:
data = pd.read_csv("bikes.csv", header=0)
data['Rachel1'] = data['Rachel1'].apply(lambda x: int(x))
s = sum(data['Rachel1'])
print(s)
