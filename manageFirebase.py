from itertools import count
import firebase_db_connect
import jsonTransfer
db = firebase_db_connect.db()

# 更新userprofile


def update_personaldata(personalData):
    items = jsonTransfer.jsontransform(personalData)
    try:
        print(items['userID'])
    except:
        print("None")
    ref = db.collection(u'cguscholar').document((items['id']))
    ref.collection(u'updateTime').document(
        (items['personalData']['updateTime'])).set(items['cited'])
    ref.set(items['personalData'])

# labellist加入label domain


def add_labeluserIDinfo(item, label):
    items = jsonTransfer.jsontransform(item)
    print(len(items['userID']))
    ref = db.collection(u'Label-Domain').document(label)
    ref.set(items)

# 新增未被爬過的label


def add_labeldomain(label):
    for i in label:
        ref = db.collection(u'Label-Domain').document(i)
        doc = ref.get()
        if not doc.exists:
            ref.set({u'updateTime': None})

# user profile updatetime


def get_userupdatetime(ID):
    users_ref = db.collection(u'cguscholar').document(ID)
    doc = users_ref.get()
    if doc.exists:
        checkTemp = doc.to_dict()
        Timestamp = checkTemp['updateTime']
        return Timestamp
    else:
        return ('Not found')

# 內容為空的labelname


def get_emptylabelname():
    lastlabel = ''
    limitcount = 1
    while(1):
        try:
            query = db.collection(
                u'Label-Domain').where(u'updateTime', '==', None).limit(limitcount)
            results = query.stream()
            for r in results:
                lastlabel = r.id
            break
        except:
            limitcount = limitcount + 1
            continue
    print(lastlabel)
    return lastlabel

# 取得最久沒更新的label


def get_labelforCGUScholar():
    label = ''
    query = db.collection(
        u'Label-Domain').where(u'updateTime', u'>', '').limit(1)
    results = query.stream()
    for r in results:
        label = r.id
    return label
