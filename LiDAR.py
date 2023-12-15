import pandas as pd
import matplotlib.pyplot as plt

distance = 3  # 距離の設定
# CSVファイルの読み込み
file_path = r"C:\Users\ma-20\developer\data\LiDAR\scan\スキャン数_%dm.csv" % distance  # ファイルパスを設定
df = pd.read_csv(file_path, header=None)

# 第3列を数値型に変換
third_column = df.iloc[:, 2]
third_column_numeric = pd.to_numeric(third_column, errors='coerce')  # 数値変換できない値はNaNに変換

# 範囲を広げながら標準偏差を計算
std_devs = [third_column_numeric.iloc[0:i].std() for i in range(2, len(third_column_numeric) + 1)]

# 範囲を広げながら標準偏差の標準偏差を計算
std_devs_of_std_devs = [pd.Series(std_devs[0:i]).std() for i in range(2, len(std_devs) + 1)]

# 2つのグラフをプロット
plt.figure(figsize=(15, 6))

# 標準偏差のグラフ
plt.subplot(1, 2, 1)
plt.plot(std_devs)
plt.title(f'Standard Deviation for {distance}m Distance')  # 距離をタイトルに含める
plt.xlabel('Range End Index')
plt.ylabel('Standard Deviation')
plt.grid(True)

# 標準偏差の標準偏差のグラフ
plt.subplot(1, 2, 2)
plt.plot(std_devs_of_std_devs)
plt.title(f'Standard Deviation of Standard Deviations for {distance}m Distance')  # 距離をタイトルに含める
plt.xlabel('Range End Index')
plt.ylabel('Standard Deviation of Standard Deviations')
plt.grid(True)

plt.tight_layout()

# グラフをSVGフォーマットで保存
plt.savefig(r"C:\Users\ma-20\developer\data\LiDAR\scan\%dm.svg" % distance, bbox_inches='tight', pad_inches=0.05)

plt.show()

