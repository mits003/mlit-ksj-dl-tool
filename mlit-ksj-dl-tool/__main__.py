from lxml import etree
import requests
import zipfile
import os.path
import os


    def get_zip_url(self):
        call_url = 'http://nlftp.mlit.go.jp/ksj/api/1.0b/index.php/app/getKSJURL.xml?appId=ksjapibeta1&lang=J&dataformat=%s&identifier=%s&prefCode=%s&fiscalyear=%s'%(dataformat, identifier, prefCode, fiscalyear)
        print("Connect: ", end="")
        print(callurl)

        try:
            r = requests.get(callurl, timeout=5)
        except Exception as e:
            print("erro and retry")
            r = requests.get(callurl, timeout=5)

        root = etree.fromstring(r.content)

        # APIからZIP URLが出力できていないことを表示
        for iter in root.iter('STATUS'):
            if iter.text is "1":
                print("No such a data file /  URL is not wrong")
        return root

    def download_file(self, url):
        """
        URL を指定してカレントディレクトリにファイルをダウンロードする
        """

        print("Downloading: ", end="")
        print(url)
        filename = url.split('/')[-1]
        if os.path.isfile(filename):
            print(filename + " aleready exist")
            return filename

        r = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            return filename

    def extract_zip(self, filename):
        """
        ファイル名を指定して zip ファイルをtmpディレクトリに展開する
        """
        # 作業ディレクトリ作成
        target_directory = './tmp'

        if os.path.isdir(target_directory) is False:
            os.mkdir('tmp')

        zfile = zipfile.ZipFile(filename)
        zfile.extractall(target_directory)