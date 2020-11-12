from bs4 import BeautifulSoup
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


DRIVER_PATH = '../mlit-ksj-dl-tool/WebDriver/chromedriver'
# URL = 'https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_4.html' # 行政区域
URL = 'https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-C23.html' # 海岸線

EXTENT = "*.shp"
ENCODING = "Shift_JIS"

def file_dl(driver_path, url):
    # Seleniumをあらゆる環境で起動させるChromeオプション
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--proxy-server="direct://"')
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument('--start-maximized')
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
    file_dl(DRIVER_PATH, URL)
    # create_cpg(EXTENT, ENCODING)