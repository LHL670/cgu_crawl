import requests
from bs4 import BeautifulSoup
import getTime


def get_labelIDlist(label):
    print(label)
    url = 'https://scholar.google.com.tw/citations?view_op=search_authors&hl=zh-TW&mauthors=label:' + label
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    searchPage = True
    tempList = []
    Label = {}
    page = int('0')

    while searchPage == True:
        for i in soup.find_all('div', class_='gsc_1usr'):
            #tag = []

            id = i.find('a')['href'].split('user=')[1]
            id.replace(" ", "_")
            tempList.append(id)
            #temp['label'] = tag

        Label['userID'] = tempList
        try:
            # split nextpage after_author
            afterAuthor = soup.find('div', id='gsc_authors_bottom_pag').find(
                'button', class_='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx')['onclick'].split('author\\x3d')[1].split('\\x26')[0]
            page = str(int(page) + 10)

            url = 'https://scholar.google.com.tw/citations?view_op=search_authors&hl=zh-TW&mauthors=label:' + \
                label+'&after_author='+afterAuthor+'&astart='+page
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")

        except:
            searchPage == False
            break
    Label['updateTime'] = getTime.currentTime()
    return Label
