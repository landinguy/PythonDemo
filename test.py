import threading
import time
import turtle

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


if __name__ == '__main__':
    # create_table_sql()
    # create_table_orm()

    # session = get_session()

    # s1 = Student(name='jack', age=12, address='上海徐汇区')
    # s2 = Student(name='peter', age=13, address='上海杨浦区')
    # s3 = Student(name='lucy', age=16, address='上海浦东新区')
    # session.add_all([s1, s2, s3])
    # session.commit()
    # session.close()
    # test_query()

    # log.info('%s %s %s %s %s %s %s' % (bool(0), bool(0.0), bool(''), bool(None), bool(()), bool([]), bool({})))
    paint()
