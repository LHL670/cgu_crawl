import get_requests
import getTime
import time


def get_labelIDlist(label):
    print(label)
    url = 'https://scholar.google.com.tw/citations?view_op=search_authors&hl=zh-TW&mauthors=label:' + label
    soup = get_requests.urlcontent(url)

    searchPage = True
    tempList = []
    Label = {}
    page = int('0')

    while searchPage == True:
        for i in soup.find_all('div', class_='gsc_1usr'):
            id = i.find('a')['href'].split('user=')[1]
            id.replace(" ", "_")
            # print(id)
            tempList.append(id)

        Label['userID'] = tempList
        try:
            # split nextpage after_author
            try:
                afterAuthor = soup.find('div', id='gsc_authors_bottom_pag').find('button', class_='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx')[
                    'onclick'].split('after_author\\x3d')[1].split('\\x26astart')[0]
            except:
                afterAuthor = soup.find('div', id='gsc_authors_bottom_pag').find('button', class_='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx')[
                    'onclick'].split('after_author\\x3d')[1].split('\\x26astart')[0]
            page = str(int(page) + 10)

            # running check

            if (int(page) % 100 == 0):
                print(page)

            url = 'https://scholar.google.com.tw/citations?view_op=search_authors&hl=zh-TW&mauthors=label:' + \
                label+'&after_author='+afterAuthor+'&astart='+page

            soup = get_requests.urlcontent(url)
        except:
            searchPage == False
            print('test')
            break
        time.sleep(2)
    Label['updateTime'] = getTime.currentTime()
    return Label
