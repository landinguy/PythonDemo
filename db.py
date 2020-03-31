import logging.config

from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column
from sqlalchemy.orm import sessionmaker

logging.config.fileConfig('log.conf')
log = logging.getLogger('db')


def get_engine(): return create_engine('mysql+pymysql://root:root@localhost/titanic')


def execute(sql): get_engine().connect().execute(sql)


def get_session():
    engine = get_engine()
    db_session = sessionmaker(bind=engine)
    return db_session()


def create_table():
    engine = get_engine()
    meta_data = MetaData(engine)

    Table('student', meta_data,
          Column('id', Integer, primary_key=True),
          Column('name', String(20)),
          Column('age', Integer),
          Column('address', String(50)))

    meta_data.create_all(engine)
