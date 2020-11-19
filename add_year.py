import csv

import geopandas
import pandas



def get_years():
    pass

def add_year():
    filename = "sample.shp"
    years

    # shpファイルを読み込みGeoDataFrameオブジェクトを取得
    gdf = gpd.read_file(filename, encoding='shift_jis')

    # 新規にカラムを追加し、属性を付与する
    gdf["year"] = year

    # shpファイルに書き込む
    gdf.to_file()