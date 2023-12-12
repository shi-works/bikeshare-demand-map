# bikeshare-demand-map
## Public Website
- https://shi-works.github.io/bikeshare-demand-map/

## データの取得
### gbfs_station_status_dl_v2.py
- pythonで下記の公共交通オープンデータセンターよりGBFS形式のデータ（station_status.json）を取得します。  
[ドコモ・バイクシェア](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-d-bikeshare/resource/06ddbb21-be3d-4163-ac92-d90127e9bf90)  
URL: `https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_status.json`  
[HELLOCYCLING](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-openstreet/resource/ccbd64b6-93f0-412e-be8a-391c72aecf61)  
URL: `https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_status.json`
#### データの取得期間、頻度
- 取得期間：2023年5月3日 00:00～2023年5月3日 23:59
- 頻度：30分ごと
#### 出力結果
- ※ただし、30分ごとのstation_status.jsonをcsvfile-merge.pyでマージした結果になります。
#### ドコモ・バイクシェア
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/docomo-cycle-tokyo_station_status.csv`,1.1MB  
#### HELLOCYCLING
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/hellocycling_station_status.csv`,17.9MB

## データの加工
### csvfile-add-latlng.py
- station_status.csvにstation.csvのステーションの位置座標を付与します。
#### 使用データ
##### ドコモ・バイクシェア
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/docomo-cycle-tokyo_station_status.csv`,1.1MB  
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/docomo-cycle-tokyo_station.csv`,83.0KB  
##### HELLOCYCLING
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/hellocycling_station_status.csv`,17.9MB  
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/hellocycling_station.csv`,2.1MB  
#### 出力結果
##### ドコモ・バイクシェア
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/docomo-cycle-tokyo_station_status_add_latlng.csv`,3.2MB
##### HELLOCYCLING
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/hellocycling_station_status_add_latlng.csv`,57.2MB

## GeoJSONからPMTilesへの変換
- Webマップ表示用にGeoJSONを[tippecanoe](https://github.com/felt/tippecanoe)で[PMTiles形式](https://github.com/protomaps/PMTiles)に変換したデータになります。
### 使用データ
#### ドコモ・バイクシェア
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/docomo_cycle_tokyo_station_status_add_latlng.geojson`,12.8MB
#### HELLOCYCLING
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/hellocycling_station_status_add_latlng.geojson`,155.2MB
#### 出力結果
#### ドコモ・バイクシェア
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/docomo_cycle_tokyo_station_status_add_latlng.pmtiles`,3.1MB
#### HELLOCYCLING
`https://xs489works.xsrv.jp/pmtiles-data/sharecycle/hellocycling_station_status_add_latlng.pmtiles`,23.5MB

## ライセンス
本データセットはCC-BY-4.0で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは公共交通オープンデータのドコモ・バイクシェア及びHELLOCYCLINGのシェアサイクルデータ（GBFS形式）を加工して作成したものです。本データセットの使用・加工にあたっては、[公共交通オープンデータセンター利用規約](https://developer.odpt.org/terms/center_use_rules.html)を必ずご確認ください。

## 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
