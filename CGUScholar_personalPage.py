import time
import threading
import queue
import manageFirebase
import CGUScholarCrawl
import checkDataformat
import getIDQueue
import CGUScholarLabel
import requests
# Worker 類別，負責處理資料


class CGUScholar(threading.Thread):
    def __init__(self, CGUqueue):
        threading.Thread.__init__(self)
        self.queue = CGUqueue

    def run(self):
        while self.queue.qsize() > 0:
            user_ID = self.queue.get()
            personalinfo = CGUScholarCrawl.get_personalpage(user_ID)
            check_personalformat = checkDataformat.personalinfoformat(
                personalinfo)

            # ID和name 為空或格式錯誤時回傳False,格式錯誤修正後回傳rewriteInfo
            if(not check_personalformat):
                personalinfo = check_personalformat
            if(check_personalformat == False):
                continue
            manageFirebase.update_personaldata(personalinfo)
            manageFirebase.add_labeldomain(
                personalinfo['personalData']['label'])

            time.sleep(1)


def LabelCrawl(type, updatelabel):  # if empty ,updatelabel is null
    print('label start')
    if(type == "empty"):
        label = manageFirebase.get_emptylabelname()  # limit
    elif(type == "reorganize"):
        label = updatelabel

    labellist = CGUScholarLabel.get_labelIDlist(label)
    check_labelformat = checkDataformat.labelinfoformat(labellist)

    # label list 為空或格式錯誤時回傳False,格式錯誤修正後回傳rewriteInfo
    if(not check_labelformat):
        labellist = check_labelformat
    if(check_labelformat == False):
        print("label crawl fail!")
    manageFirebase.add_labeluserIDinfo(labellist, label)


def CGUCrawlWorker(label):
    work_queue = getIDQueue.get_IDqueue(label)
    # 建立兩個 Worker
    CGUWorker1 = CGUScholar(work_queue)
    CGUWorker2 = CGUScholar(work_queue)

    # 讓 Worker 開始處理資料
    CGUWorker1.start()
    CGUWorker2.start()

    # 等待所有 Worker 結束
    CGUWorker1.join()
    CGUWorker2.join()

    print("Done.")


def testdocker():
    while 1:
        url = 'http://httpbin.org/ip'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }

        ip = requests.get(url, headers=headers, proxies={
            "http": "http://0.0.0.0:8888"}).text

        if ip:
            print(ip)
            time.sleep(10)
    return


# 累積到一定得筆數upload firebase
if __name__ == '__main__':
    print('start')

    # update older label then crwal user profile

    label = manageFirebase.get_labelforCGUScholar()
    LabelCrawl("reorganize", label)
    CGUCrawlWorker(label)


# label = manageFirebase.get_emptylabelname()  # limit
# LabelCrawl("empty", label)
# CGUCrawlWorker(label)

# label = manageFirebase.get_emptylabelname()  # limit
# LabelCrawl("empty", label)
# CGUCrawlWorker(label)

label = manageFirebase.get_emptylabelname()  # limit
LabelCrawl("empty", label)
CGUCrawlWorker(label)

# # add label ,userID is null
# LabelCrawl("empty", None)

# for testing
testdocker()
