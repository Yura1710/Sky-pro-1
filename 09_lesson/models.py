# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_URL

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    grade = Column(Float)

    def __repr__(self):
        return (
            f"<Student(id={self.id}, name='{self.name}', "
            f"age={self.age}, grade={self.grade})>"
        )


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
