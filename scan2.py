import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\ma-20\developer\data\LiDAR\scan\スキャン数_1m.csv"
df = pd.read_csv(file_path, header=None)

# 第3列を数値型に変換
third_column = df.iloc[:, 2]
third_column_numeric = pd.to_numeric(third_column[1:])  # 最初の行は除外

# 幅ごとの標準偏差を計算するための関数
def calculate_std_dev(data, width):
    num_points = len(data)
    std_devs = []
    for i in range(num_points - width + 1):
        range_data = data.iloc[i:i+width]
        std_dev = np.std(range_data)
        std_devs.append(std_dev)
    return std_devs

# 標準偏差を算出する幅の範囲を指定（1から2、1から3、1から4...1から2400）
widths = range(2, 2401)  # 幅の範囲

# 各幅ごとに標準偏差を計算して保存
std_devs_by_width = []
for width in widths:
    std_devs = calculate_std_dev(third_column_numeric, width)
    std_devs_by_width.append(std_devs)

# 各幅ごとの標準偏差を含むリストを作成
result = list(zip(widths, std_devs_by_width))

# 結果を表示（例：幅1から2の標準偏差のリスト）
print(result[0])