import app
import threading
import os
mapping = {
    'Ẩm thực': 'http://ytuongsangtao.net/am-thuc-ili2/',
    'Cải cách hành chính': 'http://ytuongsangtao.net/cai-cach-hanh-chinh-ili22/',
    'Chất lượng CB-CNVC': 'http://ytuongsangtao.net/chat-luong-cb-cnvc-ili26/',
    'Công nghệ kỹ thuật': 'http://ytuongsangtao.net/cong-nghe-ky-thuat-ili4/',
    'Công nghệ thông tin': 'http://ytuongsangtao.net/cong-nghe-thong-tin-ili1/',
    'Công tác tuyên truyền': 'http://ytuongsangtao.net/cong-tac-tuyen-truyen-ili23/',
    'Du lịch - giải trí': 'http://ytuongsangtao.net/du-lich-giai-tri-ili5/',
    'Điện - điện tử': 'http://ytuongsangtao.net/dien-dien-tu-ili6/',
    'Giáo dục - Đào tạo': 'http://ytuongsangtao.net/giao-duc-dao-tao-ili8/',
    'Giao thông vận tải': 'http://ytuongsangtao.net/giao-thong-van-tai-ili7/',
    'Hiện đại hóa nền hành chính': 'http://ytuongsangtao.net/hien-dai-hoa-nen-hanh-chinh-ili25/',
    'Hoạt động đơn vị sự nghiệp công lập': 'http://ytuongsangtao.net/hoat-dong-don-vi-su-nghiep-cong-lap-ili29/',
    'Kinh doanh': 'http://ytuongsangtao.net/kinh-doanh-ili9/',
    'Môi trường': 'http://ytuongsangtao.net/moi-truong-ili10/',
    'Nông - Lâm - Ngư nghiệp': 'http://ytuongsangtao.net/nong-lam-ngu-nghiep-ili11/',
    'Quảng cáo': 'http://ytuongsangtao.net/quang-cao-ili18/',
    'Sự kiện': 'http://ytuongsangtao.net/su-kien-ili12/',
    'Tài chính công': 'http://ytuongsangtao.net/tai-chinh-cong-ili27/',
    'Thể chế và thủ tục hành chính': 'http://ytuongsangtao.net/the-che-va-thu-tuc-hanh-chinh-ili24/',
    'Thời trang': 'http://ytuongsangtao.net/thoi-trang-ili20/',
    'Thủ công mỹ nghệ': 'http://ytuongsangtao.net/thu-cong-my-nghe-ili13/',
    'Tiết kiệm': 'http://ytuongsangtao.net/tiet-kiem-ili19/',
    'Ứng dụng công nghệ thông tin': 'http://ytuongsangtao.net/ung-dung-cong-nghe-thong-tin-ili28/',
    'Văn hóa nghệ thuật': 'http://ytuongsangtao.net/van-hoa-nghe-thuat-ili14/',
    'Viễn thông': 'http://ytuongsangtao.net/vien-thong-ili15/',
    'Xã hội cộng đồng': 'http://ytuongsangtao.net/xa-hoi-cong-dong-ili16/',
    'Y tế': 'http://ytuongsangtao.net/y-te-ili17/',
    'Ý tưởng khác': 'http://ytuongsangtao.net/y-tuong-khac-ili21/',
}

fieldsname = ['STT', 'URL', 'Ho Ten', 'Dia Chi', 'Tinh', 'Mo Ta Ngan Gon', 'Mo Ta Chi Tiet', 'Ma So',
              'Ngay Dang Ki', 'Danh muc']


def initialize():
    try:
        filename = 'database.csv'
        with open(filename, 'w') as f:
            w = app.csv.DictWriter(f, fieldsname)
            w.writeheader()
    except Exception:
        print('Create file failed')
        print(app.traceback.format_exc())

def task1():
    item = "Ẩm thực"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)
    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task2():
    item = "Cải cách hành chính"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task3():
    item = "Chất lượng CB-CNVC"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task4():
    item = "Công nghệ kỹ thuật"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)
    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task5():
    item = "Công nghệ thông tin"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)
    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task6():
    item = "Công tác tuyên truyền"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)
    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task7():
    item = "Du lịch - giải trí"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task8():
    item = "Điện - điện tử"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task9():
    item = "Giáo dục - Đào tạo"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task10():
    item = "Giao thông vận tải"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task11():
    item = "Hiện đại hóa nền hành chính"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task12():
    item = "Hoạt động đơn vị sự nghiệp công lập"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task13():
    item = "Kinh doanh"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task14():
    item = "Môi trường"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task15():
    item = "Nông - Lâm - Ngư nghiệp"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task16():
    item = "Quảng cáo"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task17():
    item = "Sự kiện"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task18():
    item = "Tài chính công"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task19():
    item = "Thể chế và thủ tục hành chính"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task20():
    item = "Thời trang"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task21():
    item = "Thủ công mỹ nghệ"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task22():
    item = "Tiết kiệm"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task23():
    item = "Ứng dụng công nghệ thông tin"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task24():
    item = "Văn hóa nghệ thuật"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task25():
    item = "Viễn thông"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task26():
    item = "Xã hội cộng đồng"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

def task27():
    item = "Y tế"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()


def task28():
    item = "Ý tưởng khác"
    print("Task " + item + " assigned to thread: " + threading.current_thread().name)
    newURL = mapping[item]
    print(newURL)

    _app = app.App(newURL, item)
    _app.getIdeasFromAllPage()

if __name__ == "__main__":

    initialize()

    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    t3 = threading.Thread(target=task3, name='t3')
    t4 = threading.Thread(target=task4, name='t4')
    t5 = threading.Thread(target=task5, name='t5')
    t6 = threading.Thread(target=task6, name='t6')
    t7 = threading.Thread(target=task7, name='t7')
    t8 = threading.Thread(target=task8, name='t8')
    t9 = threading.Thread(target=task9, name='t9')
    t10 = threading.Thread(target=task10, name='t10')
    t11 = threading.Thread(target=task11, name='t11')
    t12 = threading.Thread(target=task12, name='t12')
    t13 = threading.Thread(target=task13, name='t13')
    t14 = threading.Thread(target=task14, name='t14')
    t15 = threading.Thread(target=task15, name='t15')
    t16 = threading.Thread(target=task16, name='t16')
    t17 = threading.Thread(target=task17, name='t17')
    t18 = threading.Thread(target=task18, name='t18')
    t19 = threading.Thread(target=task19, name='t19')
    t20 = threading.Thread(target=task20, name='t20')
    t21 = threading.Thread(target=task21, name='t21')
    t22 = threading.Thread(target=task22, name='t22')
    t23 = threading.Thread(target=task23, name='t23')
    t24 = threading.Thread(target=task24, name='t24')
    t25 = threading.Thread(target=task25, name='t25')
    t26 = threading.Thread(target=task26, name='t26')
    t27 = threading.Thread(target=task27, name='t27')
    t28 = threading.Thread(target=task28, name='t28')

    # starting threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()

    # # wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    t26.join()
    t27.join()
    t28.join()