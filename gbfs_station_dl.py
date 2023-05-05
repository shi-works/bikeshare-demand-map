import json
import requests
import pandas as pd
from io import StringIO

# URLへアクセスしてデータを取得
# url = requests.get("https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json")
url = requests.get(
    "https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_information.json")

text = url.text

# 変換したいJSONファイルを読み込む
df = pd.read_json(StringIO(text))
print(df.head())

# ネスト（入れ子）構造になっている"data"という項目を展開する
df_json = pd.json_normalize(df['data'][0])

# JSONをCSVへ変換して文字コードをutf8で出力
'''
df_json.to_csv(r"D:\交通データ\公共交通オープンデータセンター\シェアサイクルデータ\csv\hellocycling\hellocycling_station.csv",
               encoding='utf8', index=False)
'''
df_json.to_csv(r"D:\交通データ\公共交通オープンデータセンター\シェアサイクルデータ\csv\docomo-cycle-tokyo\docomo-cycle-tokyo_station.csv",
               encoding='utf8', index=False)

print('処理終了')
