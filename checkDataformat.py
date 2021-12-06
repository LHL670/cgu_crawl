import getTime
import datetime


def personalinfoformat(data):
    # check id format
    if (data['id'][7::] != 'AAAAJ' or data['id'] == ' ' or data['id'] == None):
        return False
    # check personal data format
    if(data['personalData']['name'] == ' ' or data['personalData']['name'] == None):
        return False
    else:
        return True


def errorfixpersonalinfoformat(data):
    rewriteData = data
    personalData = data['personalData']
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
    if(len(data['userID']) == 0):
        return False
    else:
        return True


def errorfixlabelinfoformat(data):
    rewriteData = data
    # check updateTime format
    if(data['updateTime'] == '' or data['updateTime'] == None):
        rewriteData['personalData']['updateTime'] = getTime.currentTime()
    try:
        datetime.datetime.strptime(
            data['updateTime'], "%Y-%m-%d %H:%M:%S")
    except:
        rewriteData['updateTime'] = getTime.currentTime()
    return rewriteData
