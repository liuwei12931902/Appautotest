import requests
import re
import zipfile
import os
from config import globelsetting


def Load_App():
    release_id = ''
    url = 'http://download.fir.im/apps/5b9b773d959d6968cbf9a75c/install?download_token=ffc957358219b1d9475df1f787f8c882&release_id='+release_id

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }

    r = requests.get(url, headers=headers)
    print(r.status_code)
    down_url = re.findall(r'CDATA\[(.*?)\]', r.text)[0]
    print(down_url)
    r = requests.get(down_url)
    app_path = globelsetting.app_path
    app = os.path.join(globelsetting.app_path, 'XZTenant.zip')
    with open(app, 'wb') as code:
        code.write(r.content)
    my_zipfile = zipfile.ZipFile(app)
    my_zipfile.extractall(app_path)
    my_zipfile.close()


if __name__ == '__main__':
    Load_App()
