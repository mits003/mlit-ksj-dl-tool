import glob
import os
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import zipfile

DRIVER_PATH = '../mlit-ksj-dl-tool/WebDriver/chromedriver'
# URL = 'https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_4.html' # 行政区域
URL = 'https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-C23.html' # 海岸線
URL = 'https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A44.html' # 歴史的風致維持向上計画の重点地区

EXTENT = "*.shp"
ENCODING = "Shift_JIS"

def file_dl(driver_path, url):
    dldir_name = 'download'  # 保存先フォルダ名
    dldir_path = pathlib.Path(os.getcwd(), dldir_name)
    dldir_path.mkdir(exist_ok=True)  # 存在していてもOKとする（エラーで止めない）
    dl_dir = str(dldir_path.resolve())  # 絶対パス

    # Seleniumをあらゆる環境で起動させるChromeオプション
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--proxy-server="direct://"')
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument('--start-maximized')
    options.add_experimental_option("prefs", {
        "download.default_directory": dl_dir})
    # options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す
    # ブラウザの起動
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

    # 国土数値情報のダウンロードページにアクセスする
    driver.get(url)

    # 要素を指定する
    selector = '#menu-button'
    elements = driver.find_elements_by_css_selector(selector)
    print(str(len(elements)) + " zip file is going to be DL")

    for i, e in enumerate(elements):
        print(i)
        e.click()
        time.sleep(1)
        Alert(driver).accept()
        time.sleep(2)

    return dl_dir

def extraction(dl_dir):
    extdir_name = 'shp'  # 保存先フォルダ名
    extdir_path = pathlib.Path(os.getcwd(), extdir_name)
    extdir_path.mkdir(exist_ok=True)  # 存在していてもOKとする（エラーで止めない）
    ext_dir = str(extdir_path.resolve())  # 絶対パス
    print(ext_dir)
    zip_files = glob.glob(dl_dir + "/*.zip")
    print(zip_files)
    for z in zip_files:
        with zipfile.ZipFile(z) as existing_zip:
            existing_zip.extractall(ext_dir)

def create_cpg(extent, encoding):
    files = list(pathlib.Path(os.getcwd()).glob(EXTENT))
    pprint.pprint(files)

    for i, f in enumerate(files):
        basename = f.stem
        path = os.path.join(DIRECTORY, basename + ".cpg")
        cpg = open(path, 'w')
        cpg.write(ENCODING)
        cpg.close()

if __name__ == "__main__":
    dl_dir = file_dl(DRIVER_PATH, URL)
    extraction(dl_dir)
    # create_cpg(EXTENT, ENCODING)