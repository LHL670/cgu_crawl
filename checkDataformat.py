import getTime
import datetime


def personalinfoformat(data):
    # check id format
    rewriteData = data
    personalData = data['personalData']
    if (data['id'][7::] != 'AAAAJ' or data['id'] == ' ' or data['id'] == None):
        return False
    # check personal data format
    if(personalData['name'] == ' ' or personalData['name'] == None):
        return False

    if(personalData['university'] == ' ' or personalData['university'] == '首頁' or personalData['university'] == None):
        rewriteData['personalData']['university'] = 'None'

    if(personalData['picture'] == ' ' or personalData['picture'] == None or personalData['picture'] == '/citations/images/avatar_scholar_128.png'):
        rewriteData['personalData']['picture'] = 'https://scholar.google.com.tw/citations/images/avatar_scholar_128.png'

    if(len(personalData['label']) == 0):
        rewriteData['personalData']['label'] = 'None'
    # check updateTime format
    if(personalData['updateTime'] == '' or personalData['updateTime'] == None):
        rewriteData['personalData']['updateTime'] = getTime.currentTime()

    try:
        datetime.datetime.strptime(
            personalData['updateTime'], "%Y-%m-%d %H:%M:%S")
    except:
        rewriteData['personalData']['updateTime'] = getTime.currentTime()
    return rewriteData


def labelinfoformat(data):
    rewriteData = data
    if(len(data['userID']) == 0):
        return False
    # check updateTime format
    if(data['updateTime'] == '' or data['updateTime'] == None):
        rewriteData['personalData']['updateTime'] = getTime.currentTime()

    try:
        datetime.datetime.strptime(
            data['updateTime'], "%Y-%m-%d %H:%M:%S")
    except:
        rewriteData['updateTime'] = getTime.currentTime()
    return rewriteData
