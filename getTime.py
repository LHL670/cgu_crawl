import datetime


def currentTime():
    now = datetime.datetime.now()
    currentTime = now.strftime("%Y-%m-%d %H:%M:%S")
    return currentTime


def check_expires(lastUpdate, expires):
    if lastUpdate == 'Not found':
        compare = True
    else:
        expires_format = datetime.datetime.strptime(
            lastUpdate, "%Y-%m-%d %H:%M:%S")
        compare_date = expires_format + datetime.timedelta(days=expires)
        current_date = datetime.datetime.now()

        compare = compare_date < current_date
    # print(compare)
    return compare  # compare result
    # 過期或Not found為true
