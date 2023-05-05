# bikeshare-demand-map
## Public Website
- https://shi-works.github.io/bikeshare-demand-map/

## データの取得
### gbfs_station_status_dl_v2.py
- pythonで下記の公共交通オープンデータセンターよりGBFS形式のデータ（station_status.json）を取得します。  
[ドコモ・バイクシェア](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-d-bikeshare/resource/f114f7d1-11c8-4f03-98e1-2a6d2fd53e2e)  
URL: `https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_status.json`  
[HELLOCYCLING](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-openstreet/resource/ccbd64b6-93f0-412e-be8a-391c72aecf61)  
URL: `https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_status.json`
### データの取得期間、頻度
- 取得期間：2023年5月3日 00:00～2023年5月3日23:59
- 頻度：30分ごと
### 取得結果
#### ドコモ・バイクシェア
`https://github.com/shi-works/bikeshare-map/blob/main/data/docomo-cycle-tokyo_station.csv`
#### HELLOCYCLING
`https://github.com/shi-works/bikeshare-map/blob/main/data/hellocycling_station.csv`  
#### ※CSVからGeoJSONへの変換にはQGISを使用します。
