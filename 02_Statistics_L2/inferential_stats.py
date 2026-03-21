import pandas as pd
import numpy as np
from scipy import stats

def calculate_confidence_interval(data, confidence=0.95):

    """
    データから標本平均の信頼区間を算出する
    """
    n = len(data)
    mean = np.mean(data)
    # 標準誤差 (SEM): 標本から母集団を推測する際の「誤差の物差し」
    sem = stats.sem(data)

    n = len(data)
    mean = np.mean(data)
    
    # t分布を用いた信頼区間の算出
    # (自由度 n-1, 平均 loc, 尺度 scale)
    ci = stats.t.interval(confidence, n-1, loc=mean, scale=sem)
    return mean, ci

if __name__=="__main__":

    # 1. データの読み込み
    # 本来は data/ 配下のクレンジング済みCSVを読み込みますが
    # まずは動作確認用に昨日のクレンジング結果に近いサンプル値を使用
    sample_data = [10.2, 9.8, 10.5, 11.0, 9.5, 10.1, 10.3, 9.9, 10.2, 10.0]

    # 2. 推測統計の実行
    mean, ci = calculate_confidence_interval(sample_data)

    # 3. 結果のアウトプット（ビジネスサイドへの報告を意識）
    print("="*40)
    print("【推測統計:母平均の推定】")
    print(f"標本平均: {mean:.3f}")
    print(f"95%信頼区間: {ci[0]:.3f} ~ {ci[1]:.3f}")
    print("_"*40)
    print(f"解釈: 新しい取得されるデータも、95%の確率でこの範囲に")
    print(f"      真の平均値が存在すると数学的に推定")
    print("="*40)

    mean, ci = calculate_confidence_interval(sample_data)