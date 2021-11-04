import firebase_db_connect
import getTime
import queue
import manageFirebase
db = firebase_db_connect.db()


def get_IDqueue(label):
    # 建立佇列
    IDQueue = queue.Queue()

    # 將資料放入佇列
    label_ref = db.collection(u'Label-Domain').document(label)
    docs = label_ref.get()
    IDtemp = docs.to_dict()

    ID_count = 0
    for i in IDtemp['userID']:
        expire_time = manageFirebase.get_userupdatetime(i[ID_count])
        if(getTime.check_expires(expire_time, 30)):
            print(i[ID_count])
            IDQueue.put(i[ID_count])
            number = number - 1
        ID_count = ID_count + 1
    # # 取五個過期或為爬過的ID
    # number = 100
    # ID_count = 0
    # while (number != 0):
    #     expire_time = manageFirebase.get_userupdatetime(
    #         IDtemp['userID'][ID_count])
    #     if(getTime.check_expires(expire_time, 30)):
    #         print(IDtemp['userID'][ID_count])
    #         IDQueue.put(IDtemp['userID'][ID_count])
    #         number = number - 1
    #     ID_count = ID_count + 1

    return IDQueue
