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
- 取得期間：2023年5月3日 00:00～2023年5月3日 23:59
- 頻度：30分ごと
### 取得結果
- ※ただし、30分ごとのstation_status.jsonをcsvfile-merge.pyでマージした結果になります。
#### ドコモ・バイクシェア
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/sharecycle/docomo-cycle-tokyo_merge/20230503/docomo-cycle-tokyo_station_status.csv`,1.1MB  
#### HELLOCYCLING
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/sharecycle/hellocycling_merge/20230503/hellocycling_station_status.csv`,17.9MB
### csvfile-add-latlng.py
- station_status.csvにstation.csvのステーションの位置座標を付与します。
#### 使用データ
##### ドコモ・バイクシェア
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/sharecycle/docomo-cycle-tokyo_merge/20230503/docomo-cycle-tokyo_station_status.csv`,1.1MB  
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/sharecycle/docomo-cycle-tokyo_merge/docomo-cycle-tokyo_station.csv`,83.0KB  
##### HELLOCYCLING
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/sharecycle/hellocycling_merge/20230503/hellocycling_station_status.csv`,17.9MB  
`https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/sharecycle/hellocycling_merge/hellocycling_station.csv`,2.1MB  
