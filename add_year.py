import csv
import requests
import sys

from bs4 import BeautifulSoup
import geopandas
import pandas

YEAR = {
    '大正': 1912,
    '昭和': 1926,
    '平成': 1989,
    '令和': 2019
}

def years_to_csv():
    url = sys.argv[1]
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    table = soup.find(class_="mb30 responsive-table")
    with open("years.csv", "w") as f:
        writer = csv.writer(f)
        tablerows = table.find_all("tr")
        for i in range(1, len(tablerows)):
            zipname = tablerows[i].find_all(class_="txtCenter")[3].text
            jp_year = tablerows[i].find_all(class_="txtCenter")[1].text
            w_year = convert_wj(jp_year)
            writer.writerow([zipname, w_year])

def convert_wj(jp_year):
    for era in YEAR.keys():
        if era == jp_year[:2]:
            begin = YEAR[era]
            w_year = int(jp_year[2:4]) + begin -1
    return w_year

def add_year():
    filename = "sample.shp"
    years.csv

    # shpファイルを読み込みGeoDataFrameオブジェクトを取得
    gdf = gpd.read_file(filename, encoding='shift_jis')

    # 新規にカラムを追加し、属性を付与する
    gdf["year"] = year

    # shpファイルに書き込む
    gdf.to_file()

if __name__ == "__main__":
    years_to_csv()