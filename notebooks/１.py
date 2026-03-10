import numpy as np
import matplotlib.pyplot as plt

# 乱数シードを固定（再現性の確保：実務の鉄則）
np.random.seed(42)

# 1. データの生成（平均50, 標準偏差10の正規分布を1000個）
data = np.random.normal(50, 10, 1000)

# 2. ヒストグラムと統計量の可視化
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(np.mean(data), color='red', linestyle='dashed', label=f'平均値: {np.mean(data):.2f}')
plt.axvline(np.median(data), color='green', linestyle='dotted', label=f'中央値: {np.median(data):.2f}')
plt.title('データの分布と代表値（ヒストグラム）')
plt.legend()
plt.show()

# 3. 箱ひげ図の作成（分布の広がりと外れ値の確認）
plt.figure(figsize=(6, 8))
plt.boxplot(data, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='blue'))
plt.title('外れ値検知のための箱ひげ図')
plt.ylabel('値')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 4. 四分位数の算出（統計検定2級の最重要指標）
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print(f"--- 統計要約レポート ---")
print(f"平均値 (Mean): {np.mean(data):.2f}")
print(f"中央値 (Median): {np.median(data):.2f}")
print(f"標準偏差 (Std Dev): {np.std(data):.2f}")
print(f"第1四分位数 (Q1): {q1:.2f}")
print(f"第3四分位数 (Q3): {q3:.2f}")
print(f"四分位範囲 (IQR): {iqr:.2f}")