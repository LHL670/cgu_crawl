import firebase_db_connect
import getTime
import queue
db = firebase_db_connect.db()


def get_updatetime(ID):
    users_ref = db.collection(u'cguscholar').document(ID)
    doc = users_ref.get()
    if doc.exists:
        checkTemp = doc.to_dict()
        Timestamp = checkTemp['updateTime']
        return Timestamp
    else:
        return ('Not found')


def get_IDqueue(label):
    # 建立佇列
    IDQueue = queue.Queue()

    # 將資料放入佇列
    label_ref = db.collection(u'Label-Domain').document(label)
    docs = label_ref.get()
    IDtemp = docs.to_dict()

    # 取五個過期或為爬過的ID
    number = 5
    ID_count = 0
    while (number != 0):
        expire_time = get_updatetime(IDtemp['userID'][ID_count])
        if(getTime.check_expires(expire_time, 1)):
            print(IDtemp['userID'][ID_count])
            IDQueue.put(IDtemp['userID'][ID_count])
            number = number - 1
        ID_count = ID_count + 1

    return IDQueue
