# es_ldgourmet

See: [Elasticsearchチュートリアル - 不可視点](http://code46.hatenablog.com/entry/2014/01/21/115620)

### データの取得
[livedoor/datasets](https://github.com/livedoor/datasets)からデータを取得する。

```
$ cd data
$ wget https://github.com/livedoor/datasets/raw/master/ldgourmet.tar.gz
$ tar zxvf ldgourmet.tar.gz
```

### インデックス・スキーマの定義
`$ curl -XPOST localhost:9200/ldgourmet -d @mapping.json`

### インデックスの登録
`$ python add_index_from_csv.py`
