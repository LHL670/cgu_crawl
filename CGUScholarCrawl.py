import get_requests
import getTime

# personal detail


# personal detail
def get_userprofile(soup):
    info = {}
    d = soup.find('div', id='gsc_prf_i')

    # name
    try:
        info['name'] = d.find('div', id='gsc_prf_in').text
    except:
        print('None')
    # university
    try:
        info['university'] = d.find('a', class_='gsc_prf_ila').text
    except:
        info['university'] = ' '
    # picture
    try:
        info['picture'] = soup.find('div', id='gsc_prf_pua').find('img')['src']
    except:
        info['picture'] = 'https://scholar.google.com.tw/citations/images/avatar_scholar_128.png'
    label = []
    for p in soup.find_all('a', class_='gsc_prf_inta gs_ibl'):
        ptemp = p.text.replace(" ", "_")
        label.append(ptemp)
    info['label'] = label
    info['updateTime'] = getTime.currentTime()
    return info


def get_CiteBy(soup):
    citeBy = {}
    citations = {}
    h_index = {}
    i10_index = {}

    def cited(status, value):
        if status / 2 < 1:
            if status % 2 == 0:
                citations['All'] = value
            else:
                citations['Since2016'] = value
            citeBy['citations'] = citations
        if status / 2 < 2:
            if status % 2 == 0:
                h_index['All'] = value
            else:
                h_index['Since2016'] = value
            citeBy['h_index'] = h_index
        if status / 2 < 3:
            if status % 2 == 0:
                i10_index['All'] = value
            else:
                i10_index['Since2016'] = value
            citeBy['i10_index'] = i10_index

    count_d = 0
    for d in soup.find_all('td', class_='gsc_rsb_std'):
        cited(count_d, d.text)
        count_d = count_d + 1

    return citeBy


def profileresult(soup, ID):
    infos = {}
    infos['id'] = ID
    infos['personalData'] = get_userprofile(soup)
    infos['cited'] = get_CiteBy(soup)

    return infos


def get_personalpage(id):
    url = 'https://scholar.google.com.tw/citations?hl=zh-TW&user=' + id
    soup = get_requests.urlcontent(url)
    return profileresult(soup, id)
