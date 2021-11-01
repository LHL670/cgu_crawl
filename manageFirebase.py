import firebase_db_connect
import jsonTransfer
db = firebase_db_connect.db()


def update_personaldata(personalData):
    items = jsonTransfer.jsontransform(personalData)
    print(items)
    ref = db.collection(u'cguscholar').document((items['id']))
    ref.collection(u'updateTime').document(
        (items['personalData']['updateTime'])).set(items['cited'])
    ref.set(items['personalData'])


def update_labelinfo(item, label):
    items = jsonTransfer.jsontransform(item)
    print(items)
    ref = db.collection(u'Label-Domain').document(label)
    ref.set(items)


def update_labeldomain(label):
    for i in label:
        ref = db.collection(u'Label-Domain').document(i)
        doc = ref.get()
        if doc.exists:
            print('exist')
        else:
            ref.set({u'updateTime': None})


def get_lastupdatelabel():
    lastlabel = ''
    query = db.collection(
        u'Label-Domain').where(u'updateTime', '==', None).limit(1)
    results = query.stream()
    for r in results:
        lastlabel = r.id
    return lastlabel


def get_labelforCGUScholar():
    label = ''
    query = db.collection(
        u'Label-Domain').where(u'updateTime', u'>', '').limit(1)
    results = query.stream()
    for r in results:
        label = r.id
    return label
