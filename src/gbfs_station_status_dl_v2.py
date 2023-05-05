import requests
import pandas as pd
from io import StringIO
import datetime
import time


def fetch_data_and_save_csv():
    # 現在の日時を取得し、指定の形式に変換
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M")

    try:
        # hellocycling
        # URLへアクセスしてデータを取得
        response_h = requests.get(
            "https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_status.json"
        )

        # ステータスコードが200の場合、データを処理
        if response_h.status_code == 200:
            text_h = response_h.text
            df_h = pd.read_json(StringIO(text_h))
            df_h_json = pd.json_normalize(df_h['data'][0])

            # 出力ファイル名を設定し、CSVに変換して出力
            output_h_filename = f"D:\交通データ\公共交通オープンデータセンター\シェアサイクルデータ\csv\hellocycling\hellocycling_station_status_" + \
                current_datetime + ".csv"

            df_h_json.to_csv(output_h_filename, encoding='utf8', index=False)
        else:
            # ステータスコードが200以外の場合、エラーメッセージを表示
            print(f"Error: hellocycling status code {response_h.status_code}")

    except Exception as e:
        # エラーが発生した場合、エラーメッセージを表示
        print(f"Error processing hellocycling data: {e}")

    try:
        # docomo-cycle-tokyo
        # URLへアクセスしてデータを取得
        response_d = requests.get(
            "https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_status.json"
        )

        # ステータスコードが200の場合、データを処理
        if response_d.status_code == 200:
            text_d = response_d.text
            df_d = pd.read_json(StringIO(text_d))
            df_d_json = pd.json_normalize(df_d['data'][0])

            # 出力ファイル名を設定し、CSVに変換して出力
            output_d_filename = f"D:\交通データ\公共交通オープンデータセンター\シェアサイクルデータ\csv\docomo-cycle-tokyo\docomo-cycle-tokyo_station_status_" + \
                current_datetime + ".csv"

            df_d_json.to_csv(output_d_filename, encoding='utf8', index=False)
        else:
            # ステータスコードが200以外の場合、エラーメッセージを表示
            print(f"Error: docomo-cycle-tokyo status code {response_d.status_code}")

    except Exception as e:
        # エラーが発生した場合、エラーメッセージを表示
        print(f"Error processing docomo-cycle-tokyo data: {e}")

    # 処理終了のメッセージを表示
    print(current_datetime + ':処理終了')

# 処理開始日時
start_datetime = datetime.datetime(2023, 5, 3, 0, 0)

# 処理終了日時
end_datetime = datetime.datetime(2023, 5, 3, 23, 59)

# 現在時刻が開始日時になるまで待機
while datetime.datetime.now() < start_datetime:
    time.sleep(1)

while datetime.datetime.now() <= end_datetime:
    fetch_data_and_save_csv()
    time.sleep(1800)  # 30分（1800秒）ごとにデータを取得
