from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    address = Column(String(50))

    def __str__(self):
        return 'Student(id=%s,name=%s,age=%s,address=%s)' % (self.id, self.name, self.age, self.address)
