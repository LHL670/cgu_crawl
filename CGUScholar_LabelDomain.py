import time
import manageFirebase
import checkDataformat
import CGUScholarLabel


def LabelCrawl(label):  # if empty ,updatelabel is null
    print('label start')

    labellist = CGUScholarLabel.get_labelIDlist(label)
    check_labelformat = checkDataformat.labelinfoformat(labellist)

    # label list 為空或格式錯誤時回傳False,格式錯誤修正後回傳rewriteInfo
    if(check_labelformat == True):
        try:
            fix_labelformat = checkDataformat.errorfixlabelinfoformat(
                labellist)
            labellist = fix_labelformat
        except:
            print("label crawl fail!")
    else:
        print("label crawl fail!")
    manageFirebase.add_labeluserIDinfo(labellist, label)
    print('label final')
