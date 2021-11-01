import time
import threading
import queue
import manageFirebase
import CGUScholarCrawl
import checkDataformat
import getIDQueue
import CGUScholarLabel

# Worker 類別，負責處理資料


class CGUScholar(threading.Thread):
    def __init__(self, queue, num):
        threading.Thread.__init__(self)
        self.queue = queue
        self.num = num

    def run(self):
        while self.queue.qsize() > 0:
            user_ID = self.queue.get()
            personalinfo = CGUScholarCrawl.get_personalpage(user_ID)
            check_personalformat = checkDataformat.personalinfoformat(
                personalinfo)

            # ID和name 為空或格式錯誤時回傳False,格式錯誤修正後回傳rewriteInfo
            if(check_personalformat != False):
                manageFirebase.update_personaldata(personalinfo)
                manageFirebase.update_labeldomain(
                    personalinfo['personalData']['label'])
            else:
                rewrite_personalinfo = check_personalformat
                manageFirebase.update_personaldata(rewrite_personalinfo)
                manageFirebase.update_labeldomain(
                    rewrite_personalinfo['personalData']['label'])

            time.sleep(1)


def LabelCrawl():
    print('label start')
    label = manageFirebase.get_lastupdatelabel()  # limit
    labellist = CGUScholarLabel.get_labelIDlist(label)
    check_labelformat = checkDataformat.labelinfoformat(labellist)

    # label list 為空或格式錯誤時回傳False,格式錯誤修正後回傳rewriteInfo
    if(check_labelformat != False):
        manageFirebase.update_labelinfo(labellist, label)
        print('label done')
    else:
        rewrite_labelinfo = check_labelformat
        manageFirebase.update_labelinfo(rewrite_labelinfo, label)
        print('label done')


def CGUCrawlWorker(label):
    work_queue = getIDQueue.get_IDqueue(label)
    # 建立兩個 Worker
    CGUWorker1 = CGUScholar(work_queue, 1)
    CGUWorker2 = CGUScholar(work_queue, 2)

    # 讓 Worker 開始處理資料
    CGUWorker1.start()
    CGUWorker2.start()

    # 等待所有 Worker 結束
    CGUWorker1.join()
    CGUWorker2.join()
    print("Done.")


# 累積到一定得筆數upload firebase
if __name__ == '__main__':
    print('start')
    label = manageFirebase.get_labelforCGUScholar()
    CGUCrawlWorker(label)
    LabelCrawl()
