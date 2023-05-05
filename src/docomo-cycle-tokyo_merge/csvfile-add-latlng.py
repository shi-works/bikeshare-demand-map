import pandas as pd
import datetime

# CSVファイルを読み込む
df1 = pd.read_csv('./20230503/docomo-cycle-tokyo_station_status.csv')
df2 = pd.read_csv('docomo-cycle-tokyo_station.csv')

# station_idをキーにして、データフレームをマージする
merged_df = pd.merge(df1, df2, on='station_id')

# rateカラムを追加し、少数第2位までに丸める
merged_df['rate'] = (merged_df['num_bikes_available'] / (
    merged_df['num_bikes_available'] + merged_df['num_docks_available'])).round(2)

# last_reportedをdatetime型に変換し、時間帯で丸めた後、last_reported_2カラムにunixtimeとして追加する
merged_df['last_reported_2'] = pd.to_datetime(
    merged_df['last_reported'], unit='s').apply(lambda dt: dt.replace(minute=0, second=0))
merged_df['last_reported_2'] = merged_df['last_reported_2'].apply(
    lambda dt: int(dt.timestamp()))

# カラムの順番を整理する
column_order = merged_df.columns.tolist()
column_order.insert(column_order.index('last_reported') + 1,
                    column_order.pop(column_order.index('last_reported_2')))
merged_df = merged_df[column_order]

# rateカラムを指定の位置に移動する
column_order = merged_df.columns.tolist()
column_order.insert(column_order.index('num_docks_available') +
                    1, column_order.pop(column_order.index('rate')))
merged_df = merged_df[column_order]

# 結果を新しいCSVファイルに出力する
merged_df.to_csv('./20230503/docomo-cycle-tokyo_station_status_add_latlng.csv', index=False)
