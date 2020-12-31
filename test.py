import threading
import time
import turtle

import requests

import logger
from db import execute, create_table, get_session
from entity import Student

log = logger.get()


def my_thread():
    thread = threading.current_thread()
    for n in range(5):
        print('name#{0},n#{1}'.format(thread.getName(), n))
    time.sleep(2)
    print('线程{0}执行完成'.format(thread.getName()))


def test1():
    t1 = threading.Thread(target=my_thread, name='t1')
    t1.start()
    t1.join()

    t2 = threading.Thread(target=my_thread, name='t2')
    t2.start()


def create_table_sql():
    sql = '''create table student(
                id int not null primary key ,
                name varchar(20) ,
                age int ,
                address varchar(50)
             );
          '''
    execute(sql)


def create_table_orm(): create_table()


def test_query():
    session = get_session()
    query = session.query(Student).filter(Student.age >= 13).all()
    for item in query:
        # log.info('id#%s,name#%s' % (item.id, item.name))
        log.info(item)


def paint():
    tur = turtle.Turtle()
    screen = tur.getscreen()
    tur.color('red', 'yellow')
    tur.begin_fill()
    for i in range(50):
        tur.forward(200)
        tur.left(170)
    tur.end_fill()
    screen.mainloop()


def test_request():
    # url = 'http://www.baidu.com'
    # url = 'https://www.amazon.com/s/query?k=电脑&page=2&qid=1609216438&ref=sr_pg_1'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
    cookie = {
        'session-id': '137-2269336-8203106',
        'session-id-time': '2082787201l',
        'csm-hit': 'tb:1AQZE02WRB3JT40EMKRT+s-S73NP6XHSXTYFJC3QM3Y|1609212123210&t:1609212123210&adb:adblk_no',
        'ubid-main': '134-3828777-8944234',
        'session-token': 'TW2YyjF9rmjY3rLXsyBELZrmcAgDds0xOWZl6fo7KyDEPlNV/JTmLj0JODu0UpGwKJiyJ2hOq7zGqEytdl8mXijb2fUV/Ds5R2bzO43cJs/FB2CXecxZTaU6UbdS7a1YmRp3FesTaB/EJjpKIGo6XtcMM1WvMF2KnuG2W/XLmuj+PuEjBCnzZPYqROWhFBzg',
        'lc-main': 'en_US',
        'skin': 'noskin',
    }
    url = 'https://www.amazon.com/s?k=电脑&page=3'
    r = requests.get(url, headers=head, cookies=cookie)
    r.encoding = 'utf-8'
    # log.info('url#%s' % r.url)
    # log.info('text#%s' % r.text)
    with open('C:\\Users\\xiaoxiaofei\\Desktop\\12293.txt', 'w+', encoding='utf8') as f:
        f.write(r.text)


def download(url, path='d:/'):
    try:
        filename = url.split('/')[-1]
        r = requests.get(url)
        with open(path + filename, 'wb') as f:
            f.write(r.content)
        log.info('图片下载成功')
    except Exception as e:
        log.error('下载图片失败', str(e))


if __name__ == '__main__':
    test_request()
    # pass
