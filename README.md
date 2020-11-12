# mlit-ksj-dl-tool
国土数値情報のダウンロードツール

# 使い方
mlit-ksj-tool をDLし、任意のフォルダに配置する。

必要なライブラリをインストールする
```
pip install selenium
```

OSに合わせて、[ここ](https://sites.google.com/a/chromium.org/chromedriver/home)からChromeDriverをダウンロードする。

ダウンロードしたWebDriverを __mlit-ksj-dl-tool/WebDriver__ に保存する。

[国土数値情報ダウンロードサービス](https://nlftp.mlit.go.jp/ksj/)からダウンロードしたいページのURLを取得する。

以下のコマンドを実行する。

```
$ python3 mlit_ksj_dl.py ダウンロードしたいページのURL
```

__mlit-ksj-dl-tool/download__ にダウンロードしたzipファイルが、__mlit-ksj-dl-tool/shp__ に展開したshpファイル群が保存されます。